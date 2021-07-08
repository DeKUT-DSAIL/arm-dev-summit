## Creating an ABP (Activation by Personalization) device ON The Things Stack
- :hash: Step One= **The Things Network (TTN) Registration**
The things network is basically a network server where a user is able to view and re-route the data coming in from the nodes. If you don't have an account on The things Stack v3, below are a few steps on how to step a device on the server.\
1. Log on to the [The things Stack V3 website](https://eu1.cloud.thethings.network/console/applications) (:link:) and create an account  (:abcd: The normal procedure)
![Arduino](/assets/img/TTN1.PNG)
![Arduino](/assets/img/ttn2.PNG)

2. After loging in go to the **Console** and click on **Application** - The application page houses the end nodes (as we will see). If the you do not have an application, Create on by clicking on the **add application** key
![Arduino](/assets/img/ttn3.PNG)
![Arduino](/assets/img/ttn4.PNG)

3. After creating an application, click into the application and create an ABP (Activation by Personalization) device.
![Arduino](/assets/img/ttn5.PNG)
![Arduino](/assets/img/ttn6.PNG)

4. The frequency plan on the next image should depend on where you reside
![Arduino](/assets/img/ttn7.PNG)![Arduino](/assets/img/ttn8.PNG)
![Arduino](/assets/img/ttn9.PNG)
![Arduino](/assets/img/ttn10.PNG)

5. On the payload formatters view set the payload formatter to Cayenne LLP 

- :hash: Step Two  = **Arduino code and TTN link**
1. To upload the Arduino code onto the arduino Nano, you need to download and install the Arduino offline IDE. [Link](https://www.arduino.cc/en/software)
2. After installation download the code from this link :link:  :arrow_right: [Arduino code](https://github.com/DeKUT-DSAIL/arm-dev-summit/blob/main/water_level_hardwaredev-summit-arduino/dev-summit-arduino.ino)
3. Also download the following libraries using the links provided and install them using the arduino zip libraries installer.
   - [arduino-lmic-master](https://github.com/matthijskooijman/arduino-lmic)
   - ArduinoJson, MCCI_Arduino_Development_Kit_ADK and Low-Power-master can be found listed, on the Arduino library manager and you can install them directly
4. After sorting out the library and code issue, open up the code on the Arduino IDE and replace the network session keys, application session key and device address with what you have on the device detail section of the TTN.(SHOWN BELOW)

![Arduino](/assets/img/ttn10.PNG)
![Arduino](/assets/img/ttn11.PNG)





