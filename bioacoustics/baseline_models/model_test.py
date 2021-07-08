import pickle
import os
import librosa
import argparse
import numpy as np
import configparser
import pandas as pd
from queue import Queue
import sounddevice as sd
import features_extraction as fe


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

std_dev = 0.0004
mean = 0.076
df_annotation = pd.read_csv(args.annotation_csv_path)
species = list(set(df_annotation['label']))
species.sort()

def audio_callback(indata, frames, time, status):
    if status:
        print(status)

    q.put(indata.copy())


def block_energy():
    """ Returns a block of audio samples and its energy
    The block is fetched from a queue containing the audio blocks"""

    my_block = q.get()
    my_block = my_block.flatten()
    energy = np.sum(my_block ** 2)
    return energy, my_block


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
                    
    duration = float(config['baseline']['duration'])
    num_mels = float(config['baseline']['num_mels'])

    # Derive audio processing values
    win_len = int((win_len_ms * sampling_rate) / 1000)
    hop_len = int(win_len * (1 - overlap))
    nfft = int(2 ** np.ceil(np.log2(win_len)))
    num_frame = int((0.5 * duration * sampling_rate) / hop_len)
    stream_frames = int((sampling_rate / win_len) * stream_len) #number of blocks to save as a single file

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
            features = fe.features_extraction(audio,
                                    nfft,
                                    hop_len,
                                    args.noise_dir,
                                    sampling_rate,
                                    duration,
                                    win_len,
                                    hop_len,
                                    num_mels,
                                    num_frame)
            print('predicting')
            predicted = clf.predict(features)
            print(predicted)
        except Exception as e:
            print(e)
               
    else:   
        try:
            with sd.InputStream(samplerate = sampling_rate,
                                blocksize = win_len,
                                channels = args.channels,
                                callback = audio_callback):
                while True:
                    energy, my_block = block_energy()
                    std_deviation = energy - mean

                    if std_deviation >= 2 * std_dev:
                        print('Activity detected')
                        audio = np.array(my_block)
                        for _ in range(stream_frames - 1):
                            my_block = q.get()
                            my_block = my_block.flatten()
                            audio = np.concatenate((audio, my_block))
                        print(audio.shape)
                        
                        features = fe.features_extraction(audio,
                                                          nfft,
                                                          hop_len,
                                                          args.noise_dir,
                                                          sampling_rate,
                                                          duration,
                                                          win_len,
                                                          hop_len,
                                                          num_mels,
                                                          num_frame)
                        
                        print('predicting')
                        predicted = clf.predict(features)
                        print('predicted is: ', predicted)
                    
        except Exception as e:
            print(e)
            

if __name__ == '__main__':
    main()