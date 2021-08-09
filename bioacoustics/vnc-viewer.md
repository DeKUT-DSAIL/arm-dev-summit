# Using VNC viewer

## Step 1
We will use need to download and install [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/).

## Step 2
Connect your PC/Mac to the same Wi-Fi you entered SSID and password to the Pi during the image writing process. Alternatively, you can connect the Raspberry to your computer using an ethernet cable and then power the Raspberry Pi.

## Step 3
Access the Raspberry Pi's command line on your PC/Mac with SSH to enable VNC server on your Raspberry Pi by running the following line (follow this [link](https://github.com/DeKUT-DSAIL/arm-dev-summit/edit/main/bioacoustics/raspi-ssh.md) to learn how to use access Pi's command line using SSH). 

```cpp
sudo raspi-config
```
and you should get the following:

<p align="center">
  <img width="auto" height="auto" src="/assets/img/5 headless-ssh.PNG"> 
</p>

Scroll down to Interface Options using up-down buttons and hit enter. The select P3 VNC and enable it. Exit by selecting Finish using the 'sides' arrow keys and hit enter.

## Step 4
Run the following on the command line to obtain the IP address of the Pi.

```cpp
hostname -I
```
Open VNC viewer and enter the IP address of the Pi as shown below and hit enter:
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

 </details>
