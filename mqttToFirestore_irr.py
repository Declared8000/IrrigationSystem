# script Name: mqttToFirestore_irr.py                                        
import json 
import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore import SERVER_TIMESTAMP


cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()

mqttBroker = "localhost"
mqttTopic = "iot/irrigation"
mqttPort = 1883

def on_message(client, userdata, msg):
        data = json.loads(msg.payload.decode())

        print("Received Data:", data)

        db.collection("irrigationData").add({
        "deviceID": data["deviceID"],
        "soilMoisture": data["soilMoisture"],
        "temperature": data["temperature"],
        "timestamp": SERVER_TIMESTAMP
        })

client = mqtt.Client()
client.connect(mqttBroker, mqttPort)
client.subscribe(mqttTopic)
client.on_message = on_message

print("MQTT to Firestore connection running ...")
print("Receive datat to Topic:", mqttTopic)
client.loop_forever()
