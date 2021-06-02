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
![Schematic diagram](/assets/img/multi3.PNG)
I developed the device to help me in collecting water level data in a river channel. It utilizes the LoRaWAN network to send water level data collected by a micro-controller (from an ultrasonic sensor) to a network server (TTN-The Things Network). The data is then re-routed to a time-series data base (InfluxDB on GCP) for storage and easier access.

### :arrow_down_small: Component list / Item list
Listed below, are the components we will use to build the device fully.
- [MTDOT-915-X1P-SMA-1](https://www.multitech.com/models/94557148LF) or [MTDOT-868-X1P-SMA-1](https://www.multitech.com/models/94557138LF) (The choice will depend on the area of residence)
- LoRa Antenna 868Mhz RF SMA Female to be paired with [MTDOT-868-X1P-SMA-1](https://www.multitech.com/models/94557138LF)
- LoRa Antenna 915Mhz RF SMA Female to be paired with [MTDOT-915-X1P-SMA-1](https://www.multitech.com/models/94557148LF)
- MTMDK-ST-MDOT (to upload code to the Mdot)
- Jumper cables/wires (5 (male to female),5 (female to female), 5 (male to male))
- Breadboard kit
- soldering iron and solder
- HC-SRO4 ultrasonic sensor module
- One 3.7V Lithium ion battery
- [MT3608 Step-Up Adjustable DC-DC Switching Boost Converter](https://www.addicore.com/MT3608-Boost-Converter-p/ad300.htm)
- 2.54mm male Header pins.(1 piece)
- Access to power socket outlet 
- Soldering station (optional)
- Some Masking Tape 




