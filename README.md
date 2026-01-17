## Step by Step to start data publishing, subscription & forwarding to Firestore
For detailed instructions regarding API Activation, please refer to the Assignment Report

### 1. Log into GCP, choose specified project
### 2. Start 2 Virtual machines (VM)
#### IF ACTUAL SENSOR SYSTEM HAS BEEN BUILD, FOLLOW A. ONLY & FOLLOW ALTERNATIVE TO B.
#### A. Machine 1: acts as a MQTT Broker
-  Update & Upgrade the Virtual Machine to make sure it runs on the latest patch
```ubuntu shell
sudo apt-get update
sudo apt-get upgrade
```
-  Install MQTT Broker in the VM
```ubuntu shell
sudo apt-get install mosquitto
```
- Install MQTT Clients
```ubuntu shell
sudo apt-get install mosquitto-clients
```
-  Load python script "mqttToFirestore_irr.py" in order to forward data to the firestore database
-  start python script
```ubuntu shell
python3 mqttToFirestore_irr.py
```
#### B. Machine 2: acts as MQTT Publisher, de facto as the IoT System transmitting data
- sends data to the First VM
- Load python script "dataGenerator.py" in order to forward data to the firestore database
```ubuntu shell
python3 dataGenerator.py
```
#### ALTERNATIVE to B: Power up IoT System (Assumed MCU has already loaded the latest script):
-  Check the Serial monitor for
    -    Data being read
    -    Successful Network Connection Status
    -    Data publishing to MQTT Broker

At the same time, Data should be published to the MQTT Broker, seen in the shell console as continuous publishment. Additionally, Due to the firestore database subscription to the specified topic, read data will be stored here, creating a new document for each read datapoint. 
