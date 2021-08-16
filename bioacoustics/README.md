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


## Requirements

<details>
  <summary>Click to expand!</summary>

1. Raspberry Pi 3 and above and its power supply.
2. An SD card of at least 8GB.
3. USB microphone
4. 3 220/470 ohms resistors
5. 3 LEDs
5. 4 male-female jumper cables
6. 4 connecting wires
7. Breadboard
8. A reliable Wi-Fi connection
9. Personal computer
10. A monitor, HDMI cable, mouse and keyboard (optional)
  
</details>


## Installing Raspberry Pi OS

<details>
  <summary>Click to expand!</summary>

The Raspberry Pi needs an operating system for its operation. The following steps outline the process of installing the Raspberry Pi OS (formerly known as Raspbian) on the Raspberry Pi. 

### Step 1
Download and install the [Raspberry Pi Imager here](https://www.raspberrypi.org/software/) on your PC.

### Step 2
Connect an SD card reader with an SD card of at least 8GB inside to your PC.

### Step 3
Open the Raspberry Pi Imager and the following window should appear:
<p align="center">
  <img width="auto" height="auto" src="/assets/img/1 raspbian.png"> 
</p>

### Step 4.0
Choose operating system and select the option highlated below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/2 raspbian_LI.jpg"> 
</p>

### Step 4.1
Press CTRL + SHIFT + X for advanced options and check and fill in the spaces as follows

<p align="center">
  <img width="auto" height="auto" src="/assets/img/3 raspbian.PNG"> 
</p>



### Step 5
Choose storage 

<p align="center">
  <img width="auto" height="auto" src="/assets/img/4 raspbian_LI.jpg"> 
</p>

### Step 6
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

The SD card is now ready and can be plugged into the SD card slot of the Raspberry Pi. To use the Raspberry Pi, you can do it using a USB keyboard, a monitor, a HDMI cable and a mouse. Just plug the mouse and the keyboard into the Raspberry Pi's USB ports and the HDMI to the HDMI's ports on the monitor and the Pi. Power the monitor and the Pi. From here you can access the Raspberry Pi's full desktop environment.
  
If you do not have access to a USB keyboard, a monitor, a HDMI cable and a mouse, we will use SSH to access the commandline of a headless Raspberry Pi.
  
</details>

## Accessing Raspberry Pi command line using SSH
  
<details>
  <summary>Click to expand!</summary>
  
After installing the Raspbian OS on the Raspberry Pi we need to access its the command line. This can be done using a monitor or another computer on the same network as the Raspberry Pi using SSH. The steps below are a guide on how to use access the command line of a Raspberry Pi using SSH 
  
### Step 1
Download and install PuTTy [here](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.76-installer.msi) for Windows and [here](https://the.earth.li/~sgtatham/putty/latest/putty-0.76.tar.gz) for Unix

### Step 2
Connect your PC/Mac to the same Wi-Fi you entered SSID and password to the Pi during the image writing process. Alternatively, you can connect the Raspberry to your computer using an ethernet cable and then power the Raspberry Pi.

### Step 3
Open PuTTy and key in `raspberrypi.local` as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/putty-raspi-ssh.PNG"> 
</p>

Press enter and under login in the window that will appear enter `pi` as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/putty-login.PNG"> 
</p>

Press enter and key in the password of the Raspberry and press enter once more. You should see the following window:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/putty-logged-in.PNG"> 
</p>

You have successfully accessed the command line of the Raspberry Pi using SSH.

To get the full desktop environment we can use VNC viewer. Follow the following [link](https://github.com/DeKUT-DSAIL/arm-dev-summit/blob/main/bioacoustics/vnc-viewer.md) to learn how to use VNC viewer with the Raspberry Pi. 
  
</details>

## Updating Raspberry Pi OS

<details>
  <summary>Click to expand!</summary>

It is necessary that the Raspberry Pi OS on your Pi be updated. To update the OS, run the following commands on the command line:
```cpp
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```
</details>

Once the Raspberry Pi has rebooted, the currently opened session on the PuTTy will be terminated. To access the Pi again, we will need to follow the procedure of establishing SSH again. Close the current PuTTy window and restart a new window and proceed with the steps discussed above.

## Configuring the Raspberry Pi

<details>
  <summary>Click to expand!</summary>

### Enabling GPIO
  
We will be using GPIO pins so we need to enable them. Run the following command on the command line:


```cpp
sudo raspi-config
```
and you should get the following:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/5 headless-ssh.PNG"> 
</p>

Scroll down to Interface Options using up-down buttons and press enter. Select gpio option and enable it. Exit by selecting Finish using the 'sides' arrow keys and then press enter.

</details>

## Cloning the repository

<details>
  <summary>Click to expand!</summary>
  
We will clone the repository containing the software requirements for this demo. Run the following command on the command line:
  
```cpp
git clone https://github.com/DeKUT-DSAIL/arm-dev-summit.git
```
  
</details>

## Creating virtual environment

<details>
  <summary>Click to expand!</summary>


To create a virtual environment run the following commands on the command line one by one

```cpp
cp bioacoustics-env/bioacoustics-env-bash ./
chmod +x bioacoustics-env-bash
./bioacoustics-env-bash
```
Enter yes whenever prompted:


Now the Raspberry Pi is ready for use in this task.

</details>
 

## Preparing models test setup

<details>
  <summary>Click to expand!</summary>
  We will demonstrate acoustic classification of birds using a Raspberry Pi, some LEDs, and a USB microphone. To prepare the setup, we need to shutdown the Raspberry Pi first and disconnect it from power. Run the following command on the previously opened command line:
  ```cpp
sudo shutdown now
```
Wait until the activity (green) LED stops blinking before disconnecting the Raspberry Pi from power. After disconnecting the Raspberry Pi from power, we will proceed to prepare the models test setup. The diagram below shows the Raspberry Pi pinout:
  
</details>
