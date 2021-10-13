# Acoustic Monitoring of Ecosystems

Welcome to our session on acoustic monitoring of ecosystems. During this session, we will be discussing on how we can leverage machine learning to perform automatic acoustic classification of birds in order to monitor our parks, conservancies and reserves. We will make a setup to demonstrate classification of bird from their vocalizations. Let us dive into the task and feel free to direct any question at me.

## Why are we really doing this?


Acoustic monitoring of ecosystems is an efficient and non invasive method that allow us to collect data continuously and remotely. Birds vocalize a lot and also respond quickly to enviromental changes making them to be an ideal indicator species for acoustic monitoring of the biosphere.

## What is the idea?


The idea behind automatic acoustic classification is that birds produce characteristic calls/songs that are unique to their species. We can be able to tell different species of birds by just listening to the sound they produce. Acoustic data is collected by deploying acoustic sensors in the field. From analysis of this data, we can assess the state of our ecosystems. A lot of data is collected by the acoustic sensors. Manual classification of this data may turn to be a difficult task. However, we can automate the process by using acoustic sensors that automatically classify the recordings they capture. These sensors are loaded with machine learning models that have been pretrained on birds acoustic data for the classification.

## How does it work?

Sound produced by a given bird species sounds differently from sound from another species due to difference in frequency components of these sounds. If we can extract the frequency components of a sound, we can be able to describe that sound and also differentiate it from another sound by comparing their frequency components. Sounds produced by birds of the same species will have frequency components that are unique to that species. We can visualize the frequency components of a sound using a spectrogram. A spectrogram is a plot of frequency against time.

<p align="center">
  <img width="460" height="300" src="/assets/img/18 grey-backed.png">
  <img width="460" height="300" src="/assets/img/19 hartlaub's-turacos-spectrogram.png">
  
</p>

<p align="center"> 
  <em>Figure 1: SpectrogramS of a Grey-backed Camaroptera (left) and Hartlaub's Turacos (right)</em>
</p>

Figure 1 above shows spectrograms of a Greybacked Camaroptera and Hartlaub's Turacos. By looking at the two spectrograms, we can see that the spectrum of the sounds from the two birds are different. We can then treat the spectrograms as images and feed them to a machine learning model for classification. Therefore, by computing spectrograms of different bird species' sounds we can train a machine learning model that will be used for acoustic classification of birds. 

<p align="center">
  <img width="auto" height="300" src="/assets/img/17 dsp-ml.png"> 
</p>

<p align="center"> 
  <em>Figure 2: A flow diagram of how acoustic classification of bird species is acheived.</em>
</p>

After training a model, we can then deploy it on an acoustic sensor (a Raspberry Pi based acoustic sensor will be used for our case) for automatic acoustic classification of birds in the ecosystems. 

During this session, we will go through the steps of preparing a setup to demonstrate acoustic classification of birds.


# Pre-Workshop Instructions

Execute the following instructions before the Workshop day.

<details>
  <summary>Click to expand!</summary>

### Requirements

<details>
  <summary>Click to expand!</summary>

1. Jetson Nano Developer Kit and its power supply(5V, 3A).
2. An SD card of at least 32GB.
3. Ethernet cable
4. USB microphone
5. 3 220/470 ohms resistors
6. 3 LEDs
7. 4 male-female jumper cables
8. 4 connecting wires
9. Breadboard
10. A reliable Wi-Fi connection
11. Personal computer
12. A monitor, HDMI cable, mouse and keyboard (optional)
  
</details>


### Writing image in the SD Card

<details>
  <summary>Click to expand!</summary>

The Jetson Nano needs an operating system for its operation. The following steps outline the process of writing an image in an SD Card to be used with the Jetson Nano. 

  #### Step 1
      
  Download the [Jetson Nano Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-2gb-sd-card-image) and note where it is saved.
      
  #### Step 2
Follow the instructions outlined [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#write) to write the image in the SD Card for Windows, MacOS and Linux.
  

</details>

### Accessing Jetson Nano command line using SSH
  
<details>
  <summary>Click to expand!</summary>
  
Insert the SD Card into the Jetson Nano SD card slot and a USB wifi adapter. If you have a keyboard, mouse, monitor and monitor, follow the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#setup) to access the Jetson Nano full desktop on a monitor. 
  
In this section, we will access the commandline of the Jetson Nano using SSH and an extra computer. The guide is for computers operating on Windows OS. 

#### Step 1
Connect your computer to the Jetson Nano's micro USB port. Connect the power to the Nano's power micro-USB power port and switch it on.  
  
#### Step 2
Download and install PuTTy [here](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.76-installer.msi).

#### Step 3
With the cursor at the windows icon, right click and open the `Device Manager` option. Under `Ports(COM & LPT)`, right click on the options and select properties. In the window that pops up, go to the `Details` option and under `Property` select `Hardware id`. If the value is of the form shown in the diagram below, that's is the COM port of our interest. For my case it is COM4. Take note of the COM port for your case.

<p align="center">
  <img width="auto" height="auto" src="/assets/img/9 device-manager.jpg"> 
</p>

  
#### Step 4
Launch PuTTy and under `Connection type`, select serial. Enter the COM port noted above and change the speed to 115200 as shown below and click on `Open'.
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/10 putty.jpg"> 
</p>
  
You should see the following window:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/11 first-window.jpg"> 
</p>
  
Press enter. Under `License For Customer Use of NVIDIA Software`, press the tab key followed by enter. Under `Select a language` select English, press the tab key followed by enter key. Under `Select your location`, scroll to you country using the up-down navigation keys and press the tab key followed by enter key. If your country is not in the first list, select the `other` option at the bottom of the list, press the tab key and then enter key. Navigate to your continent and select it. Choose your country. and hit ok.
  
Under `Configure locales` choose your option but preferably choose the `United States -en_US.UTF-8` option and hit ok. Hit Yes under `Where are you?`. Under `Who are you?`, enter your full name in lower case and hit ok. In the next window press ok to set user name for your account as your first name. Next choose a password for your account and press ok. Re-enter the password to confirm and hit ok. Under `APP Partition Size`, use the default by hitting ok. Under `Create SWAP File`, press ok followed by Yes. Under `Network configuration`, choose `dummy0: Uknown interface`. The system will try to configure the network with DCHP and fail. Select ok and hit enter. In the window that follows, select `Do not configure the network at this time` and hit ok. Under `Hostname`, clear ubuntu, enter `jetson` and hit ok. Under `Select Nvpmodel Mode`, select `MAXN` and hit ok. After installing system, the Jetson nano will reboot. Close the PuTTy terminal and launch it again.
  
We will use SSH to access the Jetson Nano. Under Host Name(or IP Address), enter `jetson` as shown below and press `Open`.
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/12 hostname-ssh.jpg"> 
</p>
  
Press enter for the warning security and enter the username you used for your account. Enter the password and press enter. You have now accessed the command line of the Jetson Nano as shown below:
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/13 final-ssh.jpg"> 
</p>
  
</details>

 

### Setting up a virtual environment

<details>
  <summary>Click to expand!</summary>
  
You are required to have Wi-Fi with good internet connectivity. To connect to the Wi-Fi, run the following command:

```cpp
sudo nmcli dev wifi con 'SSID' password 'pass'
```

For example if my Wi-Fi's name is `DSAIL` and its password is `dsail@19`, the command will take the form:
  
```cpp
sudo nmcli dev wifi con DSAIL password dsail@19
```
  
Enter the password when prompted.

Replace 'SSID' with the Wi-Fi name and 'pass' with the Wi-Fi's password.
  
Let's proceed to clone the repository with the requirements first. Github changed from use of password to `Personal Access TokenS (PATs)` for authentication. Follow this [link](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to learn how to generate a PAT. Use the PAT as your password when prompted. Run the following command on the command line:
  
```cpp
git clone https://github.com/DeKUT-DSAIL/arm-dev-summit.git
```
  
 To create a virtual environment run the following commands on the Jetson Nano command line one after the other:
  
 ```cpp
cd arm-dev-summit/bioacoustics/
./nano2g-setup-bash
```
 
Enter the password when prompted.
  
Now the Jetson Nano is ready for use in this task.
  
</details>
  
### Download test data

<details>
  <summary>Click to expand!</summary>
  
Download test data [here](https://drive.google.com/file/d/1rhU-XReClZ0mLo33eM6atluQJ503TJ9K/view?usp=sharing) and extract it. Transfer it to your phone to make it easier to play it close to the microphone for testing.
  
</details>
  
</details>

# Workshop Instructions

We will use the following guidelines for the workshop

<details>
  <summary>Click to expand!</summary>

### Preparing models test setup

<details>
  <summary>Click to expand!</summary>
We will demonstrate acoustic classification of birds using a Jetson Nano, some LEDs, and a USB microphone. Ensure tha the Jetson Nano is not powered before preparing the setup. To shutdown the Jetson Nano, Run the following command on the command line and enter the password when prompted:
  
```cpp
sudo shutdown now
```

 
Enter the password when prompted.

Wait about a minute before disconnecting the Jetson Nano from power. After disconnecting the Jetson Nano from power, we will proceed to prepare the models test setup. The diagram below shows the Jetson Nano pinout:
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/22 jetson pinout.jpg">  
</p>

<p align="center"> 
  <em>Pinout of the Jetson Nano</em>
</p>
  
We will be using GPIO pins `19`, `21`, `23` and Ground pin `25`. Make the connections as shown below. Note the polarity of the LED shown in the diagram. The positive terminal (the longer pin) of the LED is connected to the Jetson Nano's GPIO pin and the shorter pin to the ground rail through a resistor. The lines on the figure that follows indicate continuity of holes in the breadboard:
 
 <p align="center">
  <img width="auto" height="auto" src="/assets/img/26 breadboard-continuituy.png">  
</p>
  
 <p align="center"> 
  <em>Common holes in a breadboard</em>
</p>

<p align="center">
  <img width="auto" height="auto" src="/assets/img/23 jetson-model-setup.jpg">  
</p>

<p align="center"> 
  <em>Model test setup</em>
</p>
  
  
  <p align="center">
  <img width="auto" height="300" src="/assets/img/24 jetson-model-setup.jpg">
  <img width="auto" height="300" src="/assets/img/25 hand-drawn-jetson-schematic.jpg"> 
</p>

<p align="center"> 
  <em> A setup to test trained classification models on the Jetson Nano (left) and a schematic of LEDs connection to the Jetson Nano (right)</em>
</p>
  
Plug in the microphone into one of the Jetson Nano's USB port and power the Jetson Nano. Follow the steps outlined above to access the Jetson Nano's commandline. The setup is ready for models testing
  
</details>


### Testing the models

<details>
  <summary>Click to expand!</summary>
 Run the following commands on the commandline to test the models:

```cpp
cd arm-dev-summit/bioacoustics/
source dsp-env/bin/activate 
cd baseline_models/
python nano_model_test.py -m "svm" -md "models" -n "noise" -a "labels.csv"
```
In place of "svm" for `Linear Support Vector Classifier`, you can also use "rf" for `Random Forest Classifier`, "mlp" for `Multilayer Perceptron` or "svm-rbf" for `Support Vector Classifier`.
</details>
  
</details>
