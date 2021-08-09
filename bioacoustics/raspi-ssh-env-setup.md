# Using SSH with the Raspberry Pi
  
## Step 1
Download and install PuTTy [here](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.76-installer.msi) for Windows and [here](https://the.earth.li/~sgtatham/putty/latest/putty-0.76.tar.gz) for Unix

## Step 2
Connect your PC/Mac to the same Wi-Fi you entered SSID and password to the Pi during the image writing process. Alternatively, you can connect the Raspberry to your computer using an ethernet cable and then power the Raspberry Pi.

## Step 3
Open PuTTy and key in `raspberrypi.local` as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/putty-raspi-ssh.PNG"> 
</p>

Hit enter and under login in the window that will appear enter `pi` as shown below:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/putty-login.PNG"> 
</p>

Press enter and key in the password of the Raspberry and press enter once more. You should see the following window:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/putty-logged-in.PNG"> 
</p>

You have successfully accessed the command line of the Raspberry Pi using SSH.

To get the full desktop environment we can use VNC viewer. Follow the following [link](https://github.com/DeKUT-DSAIL/arm-dev-summit/blob/main/bioacoustics/vnc-viewer.md) to learn how to use VNC viewer with the Raspberry Pi. 


2. Creating virtual environment

It is necessary that the Raspbian OS on your Pi be updated. If it is not updated, run the following commands on the command line:
```cpp
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```


To update the Raspberry Pi, clone this repository into the Raspberry Pi by running the following line either on the command line:
```cpp
git clone https://github.com/kiariegabriel/bioacoustics-env.git
```
Run the following commands on the command line one by one

```cpp
cp bioacoustics-env/bioacoustics-env-bash ./
chmod +x bioacoustics-env-bash
./bioacoustics-env-bash
```
Enter yes whenever prompted:


Now the Raspberry Pi is ready for use in this task.

