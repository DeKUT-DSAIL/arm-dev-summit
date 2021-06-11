# ARM DEV SUMMIT - WATER RESOURCE MONITORING (WATER LEVEL) - Host: Jason Kabi
### :one: What we intended to handle during these session
- Building a simple water level monitoring device on a breadbord
- How to collect data - using the device
- Displaying a deployed version of the device in the field
- Later (How to analyse the water level data collected) 
## :two: Let's dive in :point_right: : Opening Remarks
Welcome to our IoT and machine learning session at the ARM DEV SUMMIT 2021. If you have any questions, please direct them to me. 
Over the next few hours, we will be diving into the Internet of Things and machine learning by building replicas of a device, which I developed to track and collect water level data in a river channel. Also, we will be analysing the data collected by the device deployed, using some machine learning tools and algorithms.
## :three: Hands-on :muscle: Let's build.
In this section I will be taking you through the development steps of a device with the schematic diagram shown below.
![Schematic diagram](/assets/img/ard1.PNG)
I developed the device to help me in collecting water level data in a river channel. It utilizes the LoRaWAN network to send water level data collected by a micro-controller (from an ultrasonic sensor) to a network server (TTN-The Things Network). The data is then re-routed to a time-series data base (InfluxDB on GCP) for storage and easier access.

### :arrow_down_small: Component list / Item list
Listed below, are the components we will use to build the device fully.
- [Arduino Nano](https://www.arduino.cc/en/pmwiki.php?n=Main/ArduinoBoardNano) (Main controller) :link:
![Arduino](/assets/img/ard2.jpg)
- [USB A Male to mini B Cable - Cable for Arduino Nano](https://www.electronicscomp.com/usb-a-male-to-mini-b-cable) :link:
![Arduino](/assets/img/ard3.jpg)
- [RFM96W](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf) Low Power Long Range Transceiver Module (868mHz - Europe & Africa) :link: 
- [RFM69HW 433Mhz](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf) (Asia) :link:
- [RFM95W LoRa Wireless Module 915Mhz](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf) (Asia & North America & south America) :link:
- Jumper cables/wires (10 (male to female),10 (female to female), 20 (male to male))
- 2 Solderless breadboard MB-102
- soldering iron and solder
- [HC-SRO4 ultrasonic sensor module](https://www.pixelelectric.com/products/sensors/distance-vision/ultrasonic-proximity-sensor/hc-sr04-ultrasonic-module/) :link:
- [2.54mm male Header pins.(2 piece)](https://www.pixelelectric.com/instruments-tools/wire-and-cables/header-pins/40pin-2-54mm-header-pin-male-straight/) :link:
- 2.54mm female Header pins.(2 piece)
- Access to power socket outlet 
- Soldering station (optional)
- Some Masking Tape 
- 1KOhm resistor - 2
- [TXS0108E Bi-directional Voltage Module](https://www.pixelelectric.com/sensors/biometric-rotation-current/current-voltage/txs0108e-bi-directional-voltage-module/) :link:
- [ESP8266 Adapter Plate](https://store.nerokas.co.ke/index.php?route=product/product&product_id=1971)
- One millimeter thick copper conductor (wire)(diameter = 1mm) (to act as the antenna) - 40cm in length
### :arrow_down_small: Access to the LoRa Gateway :signal_strength:
:arrow_right: **### If you have access gateway, we will follow the following development steps.** 
- :hash: step One = **preparation - soldering the lora transceiver on to the adapter** 
This step facilitates connection to the Arduino Nano. Carefully solder the LoRa Transceiver on the [ESP8266 Adapter Plate](https://store.nerokas.co.ke/index.php?route=product/product&product_id=1971).The soldering should been done as shown below.
![Arduino](/assets/img/ard6.jpg)
- :hash: step Two = **Solder the Male Header pins**
The header pins will enable us to create the breadboard connection we need. The setup should be as shown below.  
- :hash: step Three = **Antenna development**
To be able to connect to the LoraWAN network(if you have access) an antenna comes in handy. We will use a 1mm thick copper wire to create an antenna for the LoRA transceiver(RF95/RF96/RF69W). The wire specifics for each transceiver chip are as stated below.
   - 173 mm for the 433mHz frequency plan (Asia)
   - 86 mm for the 868mHz frequency plan (Europe and Africa)
   - 82 mm for the 915mHz frequency plan (North America and Asia)
   - :bulb: calculation base (C = λ (wavelength) * f (frequency)) but (c = 3*10^8 m/s) and f = 868mHz/915mHz/433mHz hence length :fast_forward: L = 0.25 * λ
In the image below, is illustration of how the length of the antenna is realized.   
![Arduino](/assets/img/ard7.jpg)
   - After evaluating the length of copper wire you will need, cut the piece using a side cutter or pliers, and then solder one end of the copper wire (antenna) on to the antenna pad of the LoRa transceiver(:red_circle: Care and attention is needed).
The final step u should be as shown below.
![Arduino](/assets/img/ard4.jpg)
- :hash: step Four = **Logic level conveter preparation**
The Logic level converter will help in preventing the Arduino Nano from frying the Lora Tranceiver circuit. The Transceiver operates at a 3.3V logic level and the Arduino nano operates at a 5V logic level, hence seperation is needed. The logic level is bi-directional hence the conversion happens both ways. Before plugging the converter onto the breadboard, solder the 2.54 Male Header pins as shown below, to facilitate connection.
![Arduino](/assets/img/ard5.jpg)
- :hash: step Five = **The Things Network (TTN) Registration**
1. Click and follow the steps listed on [This link](https://github.com/DeKUT-DSAIL/arm-dev-summit/blob/main/the%20things%20stack%20v3/README.md)
- :hash: Step Six = **Arduino code and TTN link**
1. To upload the Arduino code onto the arduino Nano, you need to download and install the Arduino offline IDE. [Link](https://www.arduino.cc/en/software)
2. After installation download the code from this link :link:  :arrow_right: [Arduino code](https://github.com/DeKUT-DSAIL/arm-dev-summit/blob/main/water_level_hardware/dev-summit-arduino/dev-summit-arduino.ino)
3. Also download the following libraries using the links provided and install them using the arduino zip libraries installer.
   - [arduino-lmic-master](https://github.com/matthijskooijman/arduino-lmic)
   - ArduinoJson, MCCI_Arduino_Development_Kit_ADK and Low-Power-master can be found listed, on the Arduino library manager and you can install them directly
4. After sorting out the library and code issue, open up the code on the Arduino IDE and replace the network session keys, application session key and device address with what you have on the device detail section of the TTN.(SHOWN BELOW)

![Arduino](/assets/img/ttn10.PNG)
![Arduino](/assets/img/ttn11.PNG)

5. The keys should be stretched out in MSB hexadecimal form.

- :hash: step Seven = **Uploading the code and connecting the components on the breadboard**
1. After changing the keys on your code, compile it and upload it to the Arduino Nano using the cable provided. 
2. If the upload is a success, disconnect the Nano and connect all the components on the breadboard as shown below. 

![Arduino](/assets/img/circuit.PNG)

3. Once the connection is done, power the nano by connecting it to your computer.
### :arrow_down_small: RESULTS:
Once you power the device on you should start receiving sensor data on The Things stack after every 60 seconds as shown below.

### :arrow_down_small: Incase you don't have a LoRa network connection:
If do not have access to a LoRa network, you can just connect the ultrasonic sensor directly to the Arduino nano and upload the code below as a script.
``` cpp
// ---------------------------------------------------------------- //
// Arduino Ultrasoninc Sensor HC-SR04
// Re-writed by Arbi Abdul Jabbaar
// Using Arduino IDE 1.8.7
// Using HC-SR04 Module
// Tested on 17 September 2019
// ---------------------------------------------------------------- //

#define echoPin 8 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 7 //attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Ultrasonic Sensor HC-SR04 Test"); // print some text in Serial Monitor
  Serial.println("with Arduino UNO R3");
}
void loop() {
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
}
```
The results are shown on the serial monitor in the Arduino IDE.
      





