import os
import busio
import board
import pickle
import librosa
import argparse
import digitalio
import numpy as np
import pandas as pd
import configparser
from time import sleep
from queue import Queue
import sounddevice as sd
from collections import Counter
import features_generation as fg
import preprocessing_functions as pf

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

#std_dev = 0.0004
#mean = 0.076
df_annotation = pd.read_csv(args.annotation_csv_path)
species = list(set(df_annotation['label']))
species.sort()


grey_backed_camaroptera = digitalio.DigitalInOut(board.D18) #Set the GPIO PIN 18 as a digital pin
grey_backed_camaroptera.direction = digitalio.Direction.OUTPUT #Set GPIO PIN 18 as an output pin

hartlaubs_turaco = digitalio.DigitalInOut(board.D23) #Set the GPIO PIN 18 as a digital pin
hartlaubs_turaco.direction = digitalio.Direction.OUTPUT #Set GPIO PIN 18 as an output pin

tropical_boubou = digitalio.DigitalInOut(board.D24) #Set the GPIO PIN 18 as a digital pin
tropical_boubou.direction = digitalio.Direction.OUTPUT #Set GPIO PIN 18 as an output pin



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
        std_dev = np.std(l[200:])
        mean = np.mean(l[200:])
#         l = []
#         l.extend((date, mean, std_dev))

#         with open('calibration.csv', mode = 'a') as file:
#             create = csv.writer(file)
#             create.writerow(l)
#        print(mean, std_dev)
        print('Done Calibrating')
        return mean, std_dev


def block_energy():
    """ Returns a block of audio samples and its energy
    The block is fetched from a queue containing the audio blocks"""

    my_block = q.get()
    my_block = my_block.flatten()
    energy = np.sum(my_block ** 2)
    return energy, my_block


def species_gpio(predicted_species):
    """Drives different GPIO pins high to light up leds to indicate the
    detected species"""

    if predicted_species == 'grey-backed camaroptera':
        grey_backed_camaroptera.value = True
        sleep(5)
        grey_backed_camaroptera.value = False

    elif predicted_species == 'hartlaub\'s turaco':
        hartlaubs_turaco.value = True
        sleep(5)
        hartlaubs_turaco.value = False

    elif predicted_species == 'tropical boubou':
        tropical_boubou.value = True
        sleep(5)
        tropical_boubou.value = False
def main():
    """Returns an array of audio samples
    Args: audio_file- True if a saved audio will be used False if a streamed audio will be used
    """

    # Get parameters from configuration file
    config = configparser.ConfigParser()
    config.read('parameters.ini')

    win_len_ms = int(config['audio']['win_len_ms'])
    overlap = float(config['audio']['overlap'])
    stream_len = float(config['audio']['stream_len'])
    channels = int(config['audio']['channels'])
    sampling_rate = int(config['audio']['sampling_rate'])
    calibration_duration = int(config['audio']['calibration_duration'])

    duration = float(config['baseline']['duration'])
    num_mels = float(config['baseline']['num_mels'])

    # Derive audio processing values
    win_len = int((win_len_ms * sampling_rate) / 1000)
    hop_len = int(win_len * (1 - overlap))
    nfft = int(2 ** np.ceil(np.log2(win_len)))
    num_frame = int((0.5 * duration * sampling_rate) / hop_len)
    stream_frames = int((sampling_rate / win_len) * stream_len) #number of blocks to save as a single file
    num_calibration_blocks = int(calibration_duration / (win_len_ms / 1e3)) #number of blocks to set the still condition

    if args.model == 'svm':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))

    if args.model == 'svm-rbf':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))


    if args.model == 'mlp':
        clf = pickle.load(open(os.path.join(args.models_dir, args.model + '.pickle'), 'rb'))

    if args.model == 'rf':
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
            X = pf.all_summary_features(feature, num_frame)

            print('predicting')
            predicted = clf.predict(X)
            print(predicted)
        except Exception as e:
            print(e)

    else:
        try:
            with sd.InputStream(samplerate = sampling_rate,
                                blocksize = win_len,
                                channels = args.channels,
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

                        feature = fg.features_extraction(audio,
                                                     nfft,
                                                     hop_len,
                                                     args.noise_dir,
                                                     sampling_rate,
                                                     duration,
                                                     win_len,
                                                     hop_len,
                                                     num_mels)
                        X = pf.all_summary_features(feature, num_frame)
                        #print(X.shape)
                        if X.size:
                            #print('predicting')
                            predicted = clf.predict(X)
                            predictions = [species[int(i)] for i in predicted]
                            if len(predictions) == 1:

                                predicted_species = predictions[0]
                                print('predicted species is: ', predicted_species)
                                species_gpio(predicted_species)

                            elif len(predictions) == 2:
                                if predictions[0] == predictions[1]:
                                    predicted_species = predictions[0]
                                    print('predicted species is: ', predicted_species)
                                    species_gpio(predicted_species)

                                else:
                                    print('Unclear')

                            elif len(predictions) >= 3:
                                num_birds = Counter(predictions)
                                most_frequent = num_birds.most_common(4)

                                if len(most_frequent) == 1:
                                    predicted_species = predictions[0]
                                    print('predicted species is: ', predicted_species)
                                    species_gpio(predicted_species)


                                else:
                                    # counts = [count[1] for count in most_frequent]
                                    if most_frequent[0][1] > most_frequent[1][1]:
                                        predicted_species = most_frequent[0][0]
                                        print('predicted species is: ', predicted_species)
                                        species_gpio(predicted_species)

                                    else:
                                        print('Unclear')

                        else:
                            print('Inaudible')



        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
