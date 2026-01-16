## Step by Step to start data publishing, subscription & forwarding to Firestore
### 1. Log into GCP, choose destined project
### 2. Start the Virtual machine
-  Load python script in order to forward data to the firestore database
-  start python script
```ubuntu shell
python3 mqttToFirestore.py
```
### 3. Power up IoT System (Assumed MCU has already loaded the latest script):
-  Check the Serial monitor for
    -    Data being read
    -    Successful Network Connection Status
    -    Data publishing to MQTT Broker

At the same time, Data should be published to the MQTT Broker, seen in the shell console as continuous publishment. Additionally, Due to the firestore database subscription to the specified topic, read data will be stored here, creating a new document for each read datapoint. 
