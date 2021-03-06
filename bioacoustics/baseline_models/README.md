# Baseline models

A baseline model is a simple model that provides reasonable results and doesn't require much expertise and time to build. In this repo, we will use `Random Forest classifier`, `Multilayer Perceptron`, `Linear Support Vector Classifier` and `Support Vector Classifier`. The baseline models exhibited good performance on the train-validation data. 

The models were trained and then saved for testing. An input pipeline that continously 'listen' to determine presence of acoustic activity was developed to test the models. The pipeline captures bird recordings playback and pass segments of length 10 second to the models for classification. The Random Forest Classifier model exhibited the best performance of above 95% accuracy on the audio playbacks used. The acoustic enviroment is not a trivial factor. The models performed very well in a noiseless environment compared to a noisy environment.

The models were trained and saved on a computer. They were then loaded into a Raspberry Pi for testing. The Raspberry Pi runs on a 32-bit OS and therefore unpacking a Random Forest Model trained on a 64-bit computer is not possible (at the time of writing this). Therefore, the Random Forest Classifier had to be trained and saved on the Raspberry Pi. To train and saver the Random Forest Classifier on the Raspberry Pi, run the `raspi_model_test.py` program. To spice up the setup, LEDs of different color connected to Raspberry Pi GPIO pin have been used to indicate different species detected in a playback as shown below:

<p align="center">
  <img width="auto" height="300" src="/assets/img/24 jetson-model-setup.jpg">
  <img width="auto" height="300" src="/assets/img/25 hand-drawn-jetson-schematic.jpg"> 
</p>

<p align="center"> 
  <em>Figure 1: A setup to test trained classification models on the Jetson Nano (left) and a schematic of LEDs connection to the Jetson Nano (right)</em>
</p>

