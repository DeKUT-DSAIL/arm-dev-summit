# ARM DEV SUMMIT - WATER RESOURCE MONITORING (WATER LEVEL) - Host: Jason Kabi
### :one: What we intended to handle during these session
- Building a simple water level monitoring device on a breadbord
- How to collect data - using the device
- Displaying a deployed version of the device in the field
- Later (How to analyse the water level data collected) 
## :two: Let us dive in :point_right: : Opening Remarks
Welcome to our IoT and machine learning session at the ARM DEV SUMMIT 2021. If you have any questions, please direct them to me. 
Over the next few hours, we will be diving into the Internet of Things and machine learning by building replicas of a device, which I developed to track and collect water level data in a river channel. Also, we will be analysing the data collected by the device deployed, using some machine learning tools and algorithms.
## :three: Hands-on :muscle: Let's build.
In this section I will be taking you through the development steps of a device with the schematic diagram shown below.
![Schematic diagram](/assets/img/schem.png "caption"){: .center}
I developed the device to help me in collecting water level data in a river channel. It utilizes the LoRaWAN network to send water level data collected by a micro-controller (from an ultrasonic sensor) to a network server (TTN-The Things Network). The data is then re-routed to a time-series data base (InfluxDB on GCP) for storage and easier access.


