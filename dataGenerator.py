# Script Name: dataGenerator.py

import json
import random
import time
from datetime import datetime
import paho.mqtt.client as mqtt

mqttBroker ="localhost"
mqttPort = 1883
mqttTopic = "iot/irrigation"

client = mqtt.Client()
client.connect(mqttBroker, mqttPort)

current_moisture = 45
current_temperature = 28.0
current_ph = 6.5

def generate_soil_moisture():
        global current_moisture

        change = random.choice([-3, -2, -1, 1, 2, 3])
        current_moisture += change
        current_moisture = max(20, min(80, current_moisture))

        return current_moisture

def generate_temperature():
        global current_temperature

        change = random.choice([-0.3,-0.2,0.2,0.3])
        current_temperature += change
        current_temperature = max(24.0, min(32.0, current_temperature)) 
        return round(current_temperature,2)

def generate_ph():
        global current_ph

        change = random.choice([-0.1, -0.05, 0.05, 0.1])
        current_ph += change
        current_ph = max(5.5, min(7.5, current_ph))

        return round(current_ph,2)

print("Start Data Generation Simulation")
while True:
        data = {
                "deviceID": "esp32_irrigation",
                "soilMoisture": generate_soil_moisture(),
                "temperature": generate_temperature(),
                "phValue": generate_ph(),
                "timestamp": datetime.utcnow().isoformat()
        }
        
        payload = json.dumps(data)
        client.publish(mqttTopic, payload)
        print("Publish Data:", data)
        time.sleep(5)
