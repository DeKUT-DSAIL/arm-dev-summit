import os
import pickle
import librosa
import argparse
import numpy as np
import pandas as pd
import configparser
from time import sleep
from queue import Queue
import sounddevice as sd
from collections import Counter
import features_generation as fg
import Jetson.GPIO as GPIO


parser = argparse.ArgumentParser(description='Test trained models')
parser.add_argument('-m',
                        '--model',
                        type=str,
                        required=True,
                        metavar='',
                        help='Model to test rf, mlp, svm or svm-rbf')
parser.add_argument('-md',
                        '--models_dir',
                        type=str,
                        required=True,
                        metavar='',
                        help='Directory containing saved models')
parser.add_argument('-c',
                        '--channels',
                        type=int,
                        default=1,
                        metavar='',
                        help='Number of channels (>=1)')
parser.add_argument('-n',
                        '--noise_dir',
                        type=str,
                        required=True,
                        metavar='',
                        help='Directory containing noise files')
parser.add_argument('-i',
                        '--input',
                        type=str,
                        default='stream',
                        metavar='',
                        help="File or streamed audio('file' for saved audio file, 'stream' for a streamed audio)")
parser.add_argument('-f',
                        '--test_file_path',
                        type=str,
                        required=False,
                        metavar='',
                        help="path to the test file.")
parser.add_argument('-a',
                        '--annotation_csv_path',
                        type=str,
                        required=True,
                        metavar='',
                        help="path to the annotation csv file.")

args = parser.parse_args()


q = Queue()


df_annotation = pd.read_csv(args.annotation_csv_path)
species = list(set(df_annotation['label']))
species.sort()

GPIO.setwarnings(False)


def audio_callback(indata, frames, time, status):
    if status:
        print(status)

    q.put(indata.copy())

def calibration(num_calibration_blocks):
        """Returns the mean and standard deviation
        of the energies of blocks of sound samples
        for calibration in setting still
        condition for the purpose of activity detection"""

        l = []
        print('Calibrating')
        for _ in range(num_calibration_blocks):
            block = q.get()
            block = block.flatten()
            energy = np.sum(block ** 2)
            l.append(energy)
        std_dev = np.std(l)
        mean = np.mean(l)

        print('Done Calibrating')
        return mean, std_dev


def block_energy():
    """ Returns a block of audio samples and its energy
    The block is fetched from a queue containing the audio blocks"""

    my_block = q.get()
    my_block = my_block.flatten()
    energy = np.sum(my_block ** 2)
    return energy, my_block


def pin_blink(pin):
    """Drives different GPIO pins high to light up leds to indicate the
       detected species
       Args: pin- pin number (board mode)
    """


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

    try:
        GPIO.output(pin, GPIO.HIGH)
        sleep(2)
        GPIO.output(pin, GPIO.LOW)

    except KeyboardInterrupt:
        GPIO.output(pin, GPIO.LOW)




def main():
    """load and tests trained model
    """

    # Get parameters from configuration file
    config = configparser.ConfigParser()
    config.read('parameters.ini')

    win_len_ms = int(config['audio']['win_len_ms'])
    overlap = float(config['audio']['overlap'])
    sampling_rate = int(config['audio']['sampling_rate'])
    duration = float(config['audio']['duration'])
    num_mels = float(config['audio']['num_mels'])

    calibration_len_s = int(config['stream']['calibration_len_s']) #length of stream in secs to be used to calibrate the system
    block_len_ms = int(config['stream']['block_len_ms']) #block length to process for activity detection
    stream_len_s = int(config['stream']['stream_len_s']) #len in seconds to stream for prediction
    stream_samplerate = int(config['stream']['stream_samplerate']) #sampling rate of the stream
    channels = int(config['stream']['channels'])



    # Derive audio processing values
    win_len = int((win_len_ms * sampling_rate) / 1000) #window size to perform FFT on
    hop_len = int(win_len * (1 - overlap))
    nfft = int(2 ** np.ceil(np.log2(win_len)))
    num_frame = int((0.5 * duration * sampling_rate) / hop_len)

    #derive streaming values
    block_len = int((block_len_ms * stream_samplerate) / 1000) #blocksize to process for activity detection
    stream_frames = int((stream_samplerate / block_len) * stream_len_s) #number of blocks to process for prediction
    num_calibration_blocks = int(calibration_len_s / (block_len_ms / 1e3)) #number of blocks to set the still condition

    if args.model == 'svm':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))

    if args.model == 'svm-rbf':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))


    if args.model == 'mlp':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))

    if args.model == 'rf':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))

    if args.model == 'rf64bit':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))

    if args.input == 'file':
        try:
            audio,_ = librosa.load(args.test_file_path, sr=sampling_rate)
            feature = fg.features_extraction(audio,
                                         nfft,
                                         hop_len,
                                         args.noise_dir,
                                         sampling_rate,
                                         duration,
                                         win_length,
                                         hop_length,
                                         num_mels)
            # X = fg.all_summary_features(feature, num_frame)

            # print('predicting')
            # predicted = clf.predict(X)
            # print(predicted)

            X = fg.all_summary_features(feature, num_frame)
            #print(X.shape)
            if X.size:
                #print('predicting')
                predicted = clf.predict(X)
                predictions = [species[int(i)] for i in predicted]
                if len(predictions) == 1:

                    predicted_species = predictions[0]
                    print('predicted species is: ', predicted_species)

                elif len(predictions) == 2:
                    if predictions[0] == predictions[1]:
                        predicted_species = predictions[0]
                        print('predicted species is: ', predicted_species)

                    else:
                        print('Unclear')

                elif len(predictions) >= 3:
                    num_birds = Counter(predictions)
                    most_frequent = num_birds.most_common(4)

                    if len(most_frequent) == 1:
                        predicted_species = predictions[0]
                        print('predicted species is: ', predicted_species)


                    else:
                        # counts = [count[1] for count in most_frequent]
                        if most_frequent[0][1] > most_frequent[1][1]:
                            predicted_species = most_frequent[0][0]
                            print('predicted species is: ', predicted_species)

                        else:
                            print('Unclear')

            else:
                print('Unclear')        

        except Exception as e:
            print(e)

    else:
        try:
            with sd.InputStream(samplerate = stream_samplerate,
                                blocksize = block_len,
                                device=11,
                                channels = channels,
                                callback = audio_callback):

                mean, std_dev = calibration(num_calibration_blocks)

                while True:
                    energy, my_block = block_energy()
                    std_deviation = energy - mean

                    if std_deviation >= 4 * std_dev:
                        print('Activity detected')
                        audio = np.array(my_block)
                        for _ in range(stream_frames - 1):
                            my_block = q.get()
                            my_block = my_block.flatten()
                            audio = np.concatenate((audio, my_block))
                        print(audio.shape)

                        audio = librosa.resample(audio, stream_samplerate, sampling_rate)

                        print(audio.shape)

                        feature = fg.features_extraction(audio,
                                                     nfft,
                                                     hop_len,
                                                     args.noise_dir,
                                                     sampling_rate,
                                                     duration,
                                                     win_len,
                                                     hop_len,
                                                     num_mels)


                        # feature = np.log(feature + 1e-8)

                        # features = np.concatenate((np.mean(feature, axis=1),
                        #                                     np.std(feature, axis=1))).reshape(1, -1)



                        X = fg.all_summary_features(feature, num_frame)
                        #print(X.shape)
                        if X.size:
                            #print('predicting')
                            predicted = clf.predict(X)
                            predictions = [species[int(i)] for i in predicted]
                            if len(predictions) == 1:

                                predicted_species = predictions[0]
                                print('predicted species is: ', predicted_species)

                            elif len(predictions) == 2:
                                if predictions[0] == predictions[1]:
                                    predicted_species = predictions[0]
                                    print('predicted species is: ', predicted_species)

                                else:
                                    print('Unclear')

                            elif len(predictions) >= 3:
                                num_birds = Counter(predictions)
                                most_frequent = num_birds.most_common(4)

                                if len(most_frequent) == 1:
                                    predicted_species = predictions[0]
                                    print('predicted species is: ', predicted_species)


                                else:
                                    # counts = [count[1] for count in most_frequent]
                                    if most_frequent[0][1] > most_frequent[1][1]:
                                        predicted_species = most_frequent[0][0]
                                        print('predicted species is: ', predicted_species)

                                    else:
                                        print('Unclear')

                        else:
                            print('Inaudible')


                         
                        # print('predicting')
                        # predicted = clf.predict(features)
                        # predicted = species[int(predicted[:])]
                        # print(predicted)

                        if predicted_species == 'grey-backed camaroptera':
                            pin = 19

                        elif predicted_species == 'hartlaub\'s turaco':
                            pin = 21

                        elif predicted_species == 'tropical boubou':
                            pin = 23

                        pin_blink(pin)


        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
