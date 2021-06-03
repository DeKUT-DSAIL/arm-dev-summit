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
- [Arduino Nano](https://www.arduino.cc/en/pmwiki.php?n=Main/ArduinoBoardNano) (Main controller)
![Arduino](/assets/img/ard2.jpg)
- [USB A Male to mini B Cable - Cable for Arduino Nano](https://www.electronicscomp.com/usb-a-male-to-mini-b-cable)
![Arduino](/assets/img/ard3.jpg)
- [RFM96W](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf) Low Power Long Range Transceiver Module (868mHz - Europe & Africa) 
- [RFM69HW 433Mhz](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf) (Asia)
- [RFM95W LoRa Wireless Module 915Mhz](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf) (Asia & North America & south America)
- Jumper cables/wires (10 (male to female),10 (female to female), 20 (male to male))
- 2 Solderless breadboard MB-102
- soldering iron and solder
- [HC-SRO4 ultrasonic sensor module](https://www.pixelelectric.com/products/sensors/distance-vision/ultrasonic-proximity-sensor/hc-sr04-ultrasonic-module/)
- [2.54mm male Header pins.(2 piece)](https://www.pixelelectric.com/instruments-tools/wire-and-cables/header-pins/40pin-2-54mm-header-pin-male-straight/)
- 2.54mm female Header pins.(2 piece)
- Access to power socket outlet 
- Soldering station (optional)
- Some Masking Tape 
- 1KOhm resistor - 2
- [TXS0108E Bi-directional Voltage Module](https://www.pixelelectric.com/sensors/biometric-rotation-current/current-voltage/txs0108e-bi-directional-voltage-module/)
- [ESP8266 Adapter Plate](https://store.nerokas.co.ke/index.php?route=product/product&product_id=1971)
- One millimeter thick copper conductor (wire)(diameter = 1mm) (to act as the antenna) - 40cm in length
### :arrow_down_small: Access to the LoRa Gateway
:arrow_right: **If you have access gateway, we will follow the following development steps.** 
- :hash: step one **preparation - soldering the lora transceiver on to the adapter** 
This step facilitate connection to the Arduino Nano. The soldering should been done as shown below.


 


