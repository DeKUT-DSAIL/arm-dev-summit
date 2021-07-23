#import necessary libraries
import os
import pickle
import random
import warnings
import argparse
import numpy as np
import pandas as pd
import configparser
import librosa.display
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.utils import to_categorical
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score


parser = argparse.ArgumentParser(description='Train a Random Forest Classifier')
parser.add_argument('-pd',
                        '--param_dir',
                        type=str,
                        required=True,
                        metavar='',
                        help='Directory to save Random Forest Classifier a range of n_estimators')
parser.add_argument('-md',
                        '--models_dir',
                        type=str,
                        required=True,
                        metavar='',
                        help='Directory to save the trained model')
parser.add_argument('-a',
                        '--annotation_csv',
                        type=str,
                        required=True,
                        metavar='',
                        help='Path to annotation csv')
parser.add_argument('-m',
                        '--mels_dir',
                        type=str,
                        required=True,
                        metavar='',
                        help='Directory containing melspectrograms')

args = parser.parse_args()



if not os.path.exists(args.param_dir):
    os.makedirs(args.param_dir)

np.save(os.path.join(args.param_dir, 'rf.npy'), np.arange(200, 2000, 200)) #n_estimators for Random Forest Classifier

warnings.filterwarnings('ignore')


# Get parameters from configuration file
config = configparser.ConfigParser()
config.read('parameters.ini')

win_len_ms = int(config['audio']['win_len_ms'])
overlap = float(config['audio']['overlap'])
sampling_rate = int(config['audio']['sampling_rate'])
duration = float(config['neural-net']['input_duration_s'])
rnd_seed = int(config['neural-net']['seed'])


# Derive audio processing values
win_len = int((win_len_ms * sampling_rate) / 1000)
hop_len = int(win_len * (1 - overlap))
num_frame = int((0.5 * duration * sampling_rate) / hop_len)



labels = []
df_annotation = pd.read_csv(args.annotation_csv)

species = list(set(df_annotation['label']))
species.sort()
species_dict = dict(zip(species, range(len(species))))
species_dict
for file_species in list(df_annotation['label']):
    labels.append(species_dict[file_species])   
filelist = list(df_annotation.name)
for indx, filename in enumerate(filelist):
    filelist[indx] = os.path.join(args.mels_dir, filename)
    
annotation_dict = dict(zip(filelist, labels))



def compute_feature_mean_std(file_list):
    """Compute the mean and standard deviation of all the features
    in file_list for use in normalisation
    Args:
        file_list: list of complete path to file to get features from
    Returns:
        mean: mean of all channels
        std: standard deviation of all channels
    """
    all_feature = np.array([])

    for filename in filelist:

        curr_feature = np.load(filename)
        curr_feature = np.log(curr_feature + 1e-8)


        if all_feature.size:
            all_feature = np.vstack((all_feature, curr_feature.T))
        else:
            all_feature = curr_feature.T


    fmean = np.mean(all_feature, axis=0)
    fstd = np.std(all_feature, axis=0)
    
    np.save('fmean.npy', fmean)
    np.save('fstd.npy', fstd)
    
    return fmean, fstd


def all_summary_features(feature, filename, annotation_dict, fmean, fstd, num_frame):
    """Performs features standardization and data augmentation. 
    Args:feature- melspectrogram
         filename- file name of the melspectrogram
         annotation_dict- a dictionary containing file names and labels
         fmean- mean of the entire melspectrograms dataset channels
         fstd- standard deviation of the entire melspectrograms dataset channels
         num_frame- number of frames.
    """

    file_features = []
    file_labels = []
    
    feature = ((feature.T - fmean) /
                   (fstd + 1e-8)).T

    if feature.shape[1] > 2 * num_frame + 1:

        for indx in range(num_frame, feature.shape[1] - num_frame - 1, num_frame):

            current_feature = feature[:, indx - num_frame: indx + num_frame + 1]


            file_features.append(np.concatenate((np.mean(current_feature, axis=1),
                                            np.std(current_feature, axis=1))))


            file_labels.append(annotation_dict[filename])

    return np.array(file_features), np.array(file_labels)


def train_val_split():
    """Returns training and validation files and labels"""
    
    np.random.seed(rnd_seed)
    random.seed(rnd_seed)

    
    all_features = np.array([])
    all_labels = np.array([])
    
    feature_mean, feature_std = compute_feature_mean_std(filelist)
    
    for filename in filelist:
        file_labels = []

        feature = np.load(filename)
        feature = np.log(feature + 1e-8)
        file_features, file_labels = all_summary_features(feature,
                                                            filename,
                                                            annotation_dict,
                                                            feature_mean,
                                                            feature_std,
                                                            num_frame)
        
        if all_features.size:
            all_features = np.vstack((all_features, file_features))
        else:
            all_features = file_features
        all_labels = np.concatenate((all_labels, file_labels))
        
    X_train, X_val, y_train, y_val = train_test_split(all_features, all_labels, test_size=0.3)
    
    return X_train, X_val, y_train, y_val   


def main():
    
    param_file = os.path.join(args.param_dir, 'rf.npy')
    parameters = np.load(param_file, allow_pickle=True)

    clf = RandomForestClassifier(max_depth=None, random_state=0)
        
        
    val_accuracy = []
    mean_f1_score = []
    
    params = tqdm(parameters)
    for param in params:
        params.set_description("n_estimators=param = %s" % param)
        clf.set_params(n_estimators=param)
            
        X_train, X_val, y_train, y_val = train_val_split()

        clf.fit(X_train, y_train)
        val_accuracy.append(sum(clf.predict(X_val) == y_val) / X_val.shape[0])
        mean_f1_score.append(np.mean(f1_score(y_val, clf.predict(X_val), average=None)))
        
        
        
    best_param = parameters[np.argmax(mean_f1_score)]


    clf.set_params(n_estimators=best_param)

    clf.fit(X_train, y_train)
    
    if not os.path.exists(args.models_dir):
        os.makedirs(args.models_dir)
        
    path = os.path.join(args.models_dir,  'rf.pickle') #path to save model
    pickle.dump(clf, open(path, 'wb'))
    
    
    species_f1_score = f1_score(y_val, clf.predict(X_val), average=None)
    species_precision_score = precision_score(y_val, clf.predict(X_val), average=None)
    species_recall_score = recall_score(y_val, clf.predict(X_val), average=None)
    df_species_metrics = pd.DataFrame(list(zip(species,
                                               species_precision_score,
                                               species_recall_score,
                                               species_f1_score)),
                                      columns=['Species', 'Precision', 'Recall', 'F1 Score'])
    df_species_metrics = df_species_metrics.sort_values(['F1 Score'], ascending=False)
    df_species_metrics = df_species_metrics.reset_index(drop=True)

    print('Mean F1 score:', np.mean(species_f1_score))
    print(df_species_metrics.round(2))



if __name__ == '__main__':
    main()
