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


## Writing image in the SD Card

<details>
  <summary>Click to expand!</summary>

The Raspberry Pi needs an operating system for its operation. The following steps outline the process of installing the Raspberry Pi OS (formerly known as Raspbian) on the Raspberry Pi. 

  ### Step 1
      
  Download the [Jetson Nano Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-sd-card-image) and note where it is saved.
      
  ### Step 2
Download, install and launch the Raspberry Pi imager for [Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe), [macOS](https://downloads.raspberrypi.org/imager/imager_latest.dmg) and [Ubuntu x86](https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb). You will get the following window:
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/1 raspberry pi imager.jpg"> 
</p>

### Step 3
Connect the SD Card to your computer using an SD Card reader or using the SD Card slot if the computer has one

### Step 4
Click on `CHOOSE OS`  and select the option `Use Custom` as shown below:
 
<p align="center">
  <img width="auto" height="auto" src="/assets/img/2. use custom.jpg"> 
</p>
  
On the window that will popup, access the location where the Jetson Nano Developer Kit SD Card Image was saved. Select the image and click on open as shown below:
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/3 image-select.jpg"> 
</p>

Once in the home page of the Raspberry Pi imager, press CTRL + SHIFT + X for advanced options and uncheck all options if any is checked as shown below and save:
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/4 advanced options.jpg"> 
</p>


### Step 5
Next click on `CHOOSE STORAGE` button and select the SD card as shown below: 

<p align="center">
  <img width="auto" height="auto" src="/assets/img/5 storage.jpg"> 
</p>

### Step 6
Next click on `WRITE` button and click on `YES` on the pop up as shown below:


<p align="center">
  <img width="auto" height="auto" src="/assets/img/6 writing pop up.jpg"> 
</p>

You should see the writing progress as shown below

<p align="center">
  <img width="auto" height="auto" src="/assets/img/7 write progress.jpg"> 
</p>

When the writing is completed, the following should appear:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/8 write complete.jpg"> 
</p>

Unplug the SD Card. 
</details>

## Accessing Jetson Nano command line using SSH
  
<details>
  <summary>Click to expand!</summary>
  
Insert the SD Card into the Jetson Nano SD card slot and a USB wifi adapter. If you have a keyboard, mouse, monitor and monitor, follow the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#setup) to access the Jetson Nano full desktop on a monitor. 
  
In this section, we will access the commandline of the Jetson Nano using SSH and an extra computer. The guide is for computers operating on Windows OS. 

### Step 1
Connect your computer to the Jetson Nano's micro USB port. Connect the power to the Nano's power micro-USB power port and switch it on.  
  
### Step 2
Download and install PuTTy [here](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.76-installer.msi) for Windows and [here](https://the.earth.li/~sgtatham/putty/latest/putty-0.76.tar.gz) for Unix

### Step 3
Open PuTTy and key in `raspberrypi.local` as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/24 putty-raspi-ssh.PNG"> 
</p>

Press enter and under login in the window that will appear enter `pi` as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/23 putty-login.PNG"> 
</p>

Press enter and key in the password of the Raspberry and press enter once more. You should see the following window:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/22 putty-logged-in.PNG"> 
</p>

You have successfully accessed the command line of the Raspberry Pi using SSH.
  
### Step 4
Run the following on the command line to obtain the IP address of the Pi.

```cpp
hostname -I
```
  
Note the IP address down.
  
</details>


## Configuring the Raspberry Pi

<details>
  <summary>Click to expand!</summary>

Run the following command on the command line:


```cpp
sudo raspi-config
```
and you should get the following `Raspberry Pi Software Configuration Tool (raspi-config)` window:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/5 headless-ssh.PNG"> 
</p>
  
### Setting Display options
To configure display settings, scroll down to `Display Options` in the `raspi-config` window using up-down keys and press enter. Select `D1 Resolution` option and press enter. Select the ` DMT Mode 85 1280x720 60Hz 16:9` option and press enter. A window indicating `The resolution is set to DMT mode 85` will pop up. Press enter to exit 
  
### Enabling VNC server
  
We will be need enable VNC server so we can access the Raspberry Pi full desktop environment using VNC viewer on our computer. In the `raspi-config` window scroll down to `Interface Options` using up-down keys and press enter. Scroll to the `VNC` option using up-down buttons and press enter. When prompted to enable it scroll to the `<Yes>` option using side arrow keys and press enter. A window to notify you VNC server has been enabled will pop up. Press enter to exit. 

### Enabling GPIO
Still in the `raspi-config` window, we will need to enable GPIO pins. Scroll down to `Interface Options`, press enter, scroll to the `Remote GPIO` option and press enter. When prompted to enable it scroll to the `<Yes>` option using side arrow keys and press enter. A window to notify you GPIO has been enabled will pop up. Press enter to exit.

  
To exit `(raspi-config)` select Finish using the 'sides' arrow keys and then press enter.

</details>
  
## Accessing full desktop environment using VNC 
  
<details>
  <summary>Click to expand!</summary>

To get the full desktop environment we can use VNC viewer. The following steps are a guide on how to use VNC viewer with the Raspberry Pi: 
  
### Step 1
We will use need to download and install [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/).
  
### Step 2

Open VNC viewer and enter the IP address of the Pi as shown below and press enter:
<p align="center">
  <img width="auto" height="auto" src="/assets/img/9 headless-ssh.PNG"> 
</p>

When prompted to enter username, enter 'pi' and then enter the password set during image writing as shown below. Check the 'Remember password' box.

<p align="center">
  <img width="auto" height="auto" src="/assets/img/11 headless-pi.PNG"> 
</p>

You should now be able to access the whole desktop environment as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/12 headless-ssh.PNG"> 
</p>

 </details>

## Updating Raspberry Pi OS

<details>
  <summary>Click to expand!</summary>

It is necessary that the Raspberry Pi OS on your Pi be updated. The Raspberry Pi needs to be connected to the internet for updating. The Raspberry Pi should connect automatically to the internet whose SSID and password was entered during image writing. If not, click on the two arrows at the right of the Pi's taskbar (located at top of the desktop interface) and choose the Wi-Fi to connect to and enter its password if it is password protected and press enter. To update the OS, open the command line by clicking the terminal icon on the taskbar and run the following commands on the command line:
```cpp
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```
  
Enter `Y` when prompted
  
Once the Raspberry Pi has rebooted it will reconnect automatically with VNC viewer.
  
</details>


  

## Cloning the repository

<details>
  <summary>Click to expand!</summary>
  
We will clone the repository containing the software requirements for this demo. Github changed from use of password to `Personal Access TokenS (PATs)` for authentication. Follow this [link](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to learn how to generate a PAT. Use the PAT as your password when prompted. Run the following command on the command line:
  
```cpp
git clone https://github.com/DeKUT-DSAIL/arm-dev-summit.git
```
  
</details>

## Creating virtual environment

<details>
  <summary>Click to expand!</summary>


To create a virtual environment run the following commands on the command line one by one

```cpp
cp arm-dev-summit/bioacoustics/env-setup-bash ./
chmod +x env-setup-bash
./env-setup-bash
```
Enter yes whenever prompted. Ignore the *Failed to build llvmlite* warning.


Now the Raspberry Pi is ready for use in this task.

</details>
 

## Preparing models test setup

<details>
  <summary>Click to expand!</summary>
  We will demonstrate acoustic classification of birds using a Raspberry Pi, some LEDs, and a USB microphone. To prepare the setup, we need to shutdown the Raspberry Pi first and disconnect it from power. Run the following command on the command line:
  
```cpp
sudo shutdown now
```
Wait until the activity (green) LED stops blinking before disconnecting the Raspberry Pi from power. After disconnecting the Raspberry Pi from power, we will proceed to prepare the models test setup. The diagram below shows the Raspberry Pi pinout:
  
<p align="center">
  <img width="auto" height="auto" src="/assets/img/25 raspi-pinout.png">  
</p>

<p align="center"> 
  <em>Pinout of the Raspberry Pi</em>
</p>
  
We will be using `GPIO 18`, `GPIO 23`, `GPIO 24` and `Ground (pin 6)`. Make the connections as shown below. Note the polarity of the LED shown in the diagram. The positive terminal (the longer pin) of the LED is connected to the Raspberry Pi's GPIO pin through a resistor and the shorter pin to the ground rail. The lines on the figure that follow indicate continuity of holes in the breadboard:
 
 <p align="center">
  <img width="auto" height="auto" src="/assets/img/31 breadboard-continuituy.png">  
</p>
  
 <p align="center"> 
  <em>Common holes in a breadboard</em>
</p>

<p align="center">
  <img width="auto" height="auto" src="/assets/img/26 model-test-setup.jpg">  
</p>

<p align="center"> 
  <em>Model test setup</em>
</p>
  
Plug in the microphone into one of the Raspberry Pi's USB port and power the Raspberry Pi. Follow the steps outlined above to access the Raspberry Pi's Desktop on VNC viewer. The setup is ready for models testing
  
</details>
