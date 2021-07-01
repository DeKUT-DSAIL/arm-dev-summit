# Acoustic Classification of Bird Species

Welcome to our session on acoustic classification of bird species. During this session, we will be discussing on how we can classify birds from their vocalizations and set up hardware that we will use for this task. Let us dive into the task and feel free to direct any question at me.

## Why are we really doing this?


Automatic acoustic classification of bird species offers a tool to study our ecosystems for biodiversity conservation. it will help in continous and remote monitoring of our ecosystems. It can also be interesting for bird watchers and ornithologists.
</details>

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


### Hardware

<details>
  <summary>Click to expand!</summary>

1. PC and access to the internet
2. Raspberry Pi 3/4 and its power supply
3. 8GB+ SD card
4. USB microphone
5. Mouse, keyboard, monitor and a HDMI cable (optinal)
  
</details>

### Software

#### Installing software on PC

<details>
  <summary>Click to expand!</summary>



1. Installing Python

For this task, we will be using Python programming language so let's begin with installing it on our computers. If you have Python installed on your computer you can skip to the second requirement. Before installing Python on Windows, go to the[Microsoft Visual C++ downloads](https://www.python.org/downloads/), scroll down the page to the Visual Studio 2015, 2017 and 2019 section and download and install the Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019 for your platform. For computers running on windows and Mac OS X, download the [Python installer here](https://www.python.org/downloads/) and run it. For computers running on Linux distributions, run the following on terminal:  

```cpp
sudo apt install python3 python3-pip
```

2. Creating a Python environment

Next, we need to create a Python environment and install the necessary libraries. To create the environment and activate it, run the following lines one at a time on the command prompt for Windows and terminal for Linux and Mac OS X:

```cpp
// Windows
python -m venv 'environment name'
'environment name'/Scripts/activate

// Linux and Mac OS X
python -m venv 'environment name'
source 'environment name'/bin/activate
```

After creating the environment, download the [requirements.txt here](https://raw.githubusercontent.com/DeKUT-DSAIL/arm-dev-summit/main/bioacoustics/requirements.txt?token=AQENBGXS3BGDCSGQIPAYWB3A3W65E). To install the requirements, run the following line on the command prompt or the terminal:
```cpp
pip install -r 'path to requirements.txt'
```
  
</details>

#### Installing software on the Raspberry Pi

<details>
  <summary>Click to expand!</summary>


We are going to install Raspberry Pi OS and the requirements for this task.
1. Installing Raspberry Pi OS

The Raspberry Pi needs an operating system for its operation. Download [Raspberry Pi Imager here](https://www.raspberrypi.org/software/), install it and follow the steps below to write the Raspberry Pi OS image on the SD Card.
##### Step 1
Run the Raspberry Pi Imager and the following window should appear:
<p align="center">
  <img width="auto" height="auto" src="/assets/img/1 raspbian.png"> 
</p>

##### Step 2.0
Choose operating system and select the option highlated below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/2 raspbian_LI.jpg"> 
</p>

##### Step 2.1
Press CTRL + SHIFT + X for advanced options and check and fill in the spaces as follows

<p align="center">
  <img width="auto" height="auto" src="/assets/img/3 raspbian.PNG"> 
</p>



##### Step 3
Choose storage 

<p align="center">
  <img width="auto" height="auto" src="/assets/img/4 raspbian_LI.jpg"> 
</p>

##### Step 4
Write the image and verify the SD card by clicking yes.

<p align="center">
  <img width="auto" height="auto" src="/assets/img/5 raspbian.PNG"> 
</p>

You should see the writing progress as shown below

<p align="center">
  <img width="auto" height="auto" src="/assets/img/6 raspbian.PNG"> 
</p>

When the writing is completed, the following should appear:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/7 raspbian.PNG"> 
</p>

The SD card is now ready and can be plugged into the SD card slot of the Raspberry Pi. To use the Raspberry Pi, you can do it using a USB keyboard, a monitor, a HDMI cable and a mouse. Just plug the mouse and the keyboard into the Raspberry Pi's USB ports and the HDMI to the HDMI's ports on the monitor and the Pi. Plug the monitor and the Pi to power and switch on the monitor. From here you can access the Raspberry Pi's full desktop environment. If you do not have access to a USB keyboard, a monitor, a HDMI cable and a mouse, we will ssh to the headless Raspberry Pi. 
#### SSHing into a headless Pi
##### Step 1
Connect your PC/Mac to the same Wi-Fi you entered SSID and password to the Pi during the image writing process. Alternatively, you can connect the Raspberry to your computer using an ethernet cable and then power the Raspberry Pi.

##### Step 2
After about a minute, open the command line on your computer and run the following line:
```cpp
ssh pi@raspberry.local
```
You should see the following on the terminal:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/1 headless-ssh.PNG"> 
</p>

Type 'yes' and hit enter and then enter the password you set during image writing and you should be able to get the following:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/3 headless-ssh.PNG"> 
</p>

##### Step 3
Run the following line on the terminal:

```cpp
sudo raspi-config
```
and you should get the following:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/5 headless-ssh.PNG"> 
</p>

Scroll down to Interface Options using up-down buttons and hit enter. The select P3 VNC and enable it. Exit by selecting Finish using the 'sides' arrow keys and hit enter.

##### Step 3
Run the following on the command line to obtain the IP address of the Pi.

```cpp
hostname -I
```
To get the full desktop environment, we will use need to download and install [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/). On installing VNC viewer, open it and enter the IP address of the Pi as shown below and hit enter:
<p align="center">
  <img width="auto" height="auto" src="/assets/img/9 headless-ssh.PNG"> 
</p>

When prompted to enter username, enter 'pi' and then enter the password set during image writing as shown below. Check the 'Remember password' box.

<p align="center">
  <img width="auto" height="auto" src="/assets/img/11 headless-ssh.PNG"> 
</p>

You should now be able to access the whole desktop environment as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/12 headless-ssh.PNG"> 
</p>


2. Updating Raspberry Pi OS and creating environment

To update the Raspberry Pi, clone this repository into the Raspberry Pi by running the following line in the Raspberry Pi's command line:
```cpp
git clone https://github.com/DeKUT-DSAIL/arm-dev-summit.git
```
Open the File Manager of the Raspberry Pi by clicking on the icon to the right of the Web Browser icon. Open the arm-dev-summit folder and then the bioacoustics subfolder. Copy the `raspi-update-bash` and `env-setup-bash` files and paste them in the `/home/pi` directory. Open the terminal and run the following lines one at a time:

```cpp
chmod +x raspi-update-bash
chmod +x env-setup-bash
```
Next, run the following line to update the Raspberry Pi OS and enter yes when prompted:

```cpp
./raspi-update-bash
```
After updating is done the Raspberry Pi will reboot. After the Pi has rebooted, open the terminal and run the following line and enter yes whenever prompted:

```cpp
./env-setup-bash
```
Now the Raspberry Pi is ready for use in this task.

</details>
