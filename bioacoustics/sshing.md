# SSHing into a headless
  
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

