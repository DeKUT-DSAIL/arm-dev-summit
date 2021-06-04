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
- :hash: step Two = **Solder the Male Header pins**
The header pins will enable us to create the breadboard connection we need. The setup should be as shown below.  
- :hash: step Three = **Antenna development**
To be able to connect to the LoraWAN network(if you have access) an antenna comes in handy. We will use a 1mm thick copper wire to create an antenna for the LoRA transceiver(RF95/RF96/RF69W). The wire specifics for each transceiver chip are as stated below.
   - 173 mm for the 433mHz frequency plan (Asia)
   - 86 mm for the 868mHz frequency plan (Europe and Africa)
   - 82 mm for the 915mHz frequency plan (North America and Asia)
   - :bulb: calculation base (C = λ (wavelength) * f (frequency)) but (c = 3*10^8 m/s) and f = 868mHz/915mHz/433mHz hence length :fast_forward: L = 0.25 * λ
In the image below, is illustration of how the length of the antenna is realized.   
![Arduino](/assets/img/ard4.jpg)
   - After evaluating the length of copper wire you will need, cut the piece using a side cutter or pliers, and then solder one end of the copper wire (antenna) on to the antenna pad of the LoRa transceiver(:red_circle: Care and attention is needed).
The final step u should be as shown below.
- :hash: step Four = **Logic level conveter preparation**
The Logic level converter will help in preventing the Arduino Nano from frying the Lora Tranceiver circuit. The Transceiver operates at a 3.3V logic level and the Arduino nano operates at a 5V logic level, hence seperation is needed. The logic level is bi-directional hence the conversion happens both ways. Before plugging the converter onto the breadboard, solder the 2.54 Male Header pins as shown below, to facilitate connection.
- :hash: step Five = **The Things Network (TTN) Registration**
The things network is basically a network server where a user is able to view and re-route the data coming in from the nodes. If you don't have an account on The things Stack v3, below are a few steps on how to step a device on the server.\
      1.  Log on to the [The things Stack V3 website](https://eu1.cloud.thethings.network/console/applications) (:link:) and create an account  (:abcd: The normal procedure)
      ![Arduino](/assets/img/ttn1.PNG)
      ![Arduino](/assets/img/ttn2.PNG)
      2. After loging in go to the **Console** and click on **Application** - The application page houses the end nodes (as we will see). If the you do not have an application, Create on by clicking on the **add application** key.
      ![Arduino](/assets/img/ttn3.PNG)
      ![Arduino](/assets/img/ttn4.PNG)
      3. After creating an application, click into the application and create an ABP (Activation by Personalization) device.
      ![Arduino](/assets/img/ttn5.PNG)
      ![Arduino](/assets/img/ttn6.PNG)
      
      The frequency plan on the next image should depend on where you reside
      
   ![Arduino](/assets/img/ttn7.PNG)
      Continue.
   ![Arduino](/assets/img/ttn8.PNG)
   ![Arduino](/assets/img/ttn9.PNG)
   ![Arduino](/assets/img/ttn10.PNG)




      





