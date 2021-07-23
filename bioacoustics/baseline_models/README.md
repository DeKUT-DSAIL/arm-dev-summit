# Baseline models

A baseline model is a simple model that provides reasonable results and doesn't require much expertise and time to build. In this repo, we will use `Random Forest classifier`, `Multilayer Perceptron`, `Linear Support Vector Classifier` and `Support Vector Classifier`. The baseline models exhibited good performance on the train-validation data. 

The models were trained and then saved for testing. An input pipeline that continously 'listen' to determine presence of acoustic activity was developed to test the models. The pipeline captures bird recordings playback and pass segments of length 10 second to the models for classification. The Random Forest Classifier model exhibited the best performance of above 95% accuracy on the audio playbacks used.

The models were trained and saved on a computer. They were then loaded into a Raspberry Pi for testing. The Raspberry Pi runs on a 32-bit OS and therefore unpacking a Random Forest Model trained on a 64-bit computer is not possible (at the time of writing this). Therefore, the Random Forest Classifier had to be trained and saved on the Raspberry Pi. To spice up the setup, LEDs of different color connected to Raspberry Pi GPIO pin have been used to indicate different species detected in a playback.
