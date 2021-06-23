# Acoustic Classification of Bird Species

Welcome to our session on acoustic classification of bird species. During this session, we will be discussing on how we can classify birds from their vocalizations and set up hardware that we will use for this task. Let us dive into the task and feel free to direct any question at me.

## Why are we really doing this?

Automatic acoustic classification of bird species offers a tool to study our ecosystems for biodiversity conservation. it will help in continous and remote monitoring of our ecosystems. It can also be interesting for bird watchers and ornithologists. 

## What is the idea?

The idea behind automatic acoustic classification is that animals and especially birds produce characteristic calls/songs that are unique to their species. We can be able to tell different species of birds by just listening to the sound they produce. A lot of data is collected from deploying acoustic sensors in our ecosystems. Manual classification of this data may turn to be a difficult task. However, we can automate the process of acoustic classification of bird species using machine learning. Using digital signal processing (DSP) techniques, we can be able to analyze different sound recordings on digital computers and be able to tell the different sounds from different bird species. Of interest is the frequency component of the recordings. By analyzing the spectrum of bird recordings, we can be able to tell different species of birds.

## How does it work?

Different sounds sound differently to our ears due to the different frequency components contained in each sound. If we can extract the frequency components of a sound, we can be able to describe that sound and also differentiate it from another sound by comparing their frequency components. Sounds produced by birds of the same species will have frequency components that are similar but different from sounds from another species. We can visualize the frequency components of a sound using a spectrogram. A spectrogram is a plot of frequency against time.

<p align="center">
  <img width="460" height="300" src="/assets/img/grey-backed.png">
  <img width="460" height="300" src="/assets/img/hartlaub's-turacos-spectrogram.png">
  
</p>

<p align="center"> 
  <em>Figure 1: SpectrogramS of a Grey-backed Camaroptera (left) and Hartlaub's Turacos (right)</em>
</p>

Figure 1 above shows spectrograms of a Greybacked Camaroptera and Hartlaub's Turacos. By looking at the two spectrograms, we can see that the spectrum of the sounds from the two birds are different. We can then treat the spectrograms as images and feed them to a machine learning model for classification. Therefore, by computing spectrograms of different bird species' sounds we can train a machine learning model that will be used in acoustic classification of birds. 

<p align="center">
  <img width="auto" height="300" src="/assets/img/dsp-ml.png"> 
</p>

<p align="center"> 
  <em>Figure 2: A flow diagram of how acoustic classification of bird species is acheived.</em>
</p>

After training a model, we can then deploy it on an acoustic sensor (a Raspberry Pi based acoustic sensor will be used for our case) for automatic acoustic classification of birds in the ecosystems. 

During this session, we will go through the steps of acquiring acoustic data of birds, preprocess the data, extract features from the data (compute spectrograms), train machine learning models using the spectrograms, test the models and then deploy the models on the Raspberry Pi.

## Requirements
<ol>
<li>Installing Python</li>
 <p> 
  For this task, we will be using Python programming language so let's begin with installing it on our computers. If you have Python installed on your computer you can skip to the second requirement. For computers running on windows, go to the - [Python page](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe) 
</p>

</ol>
