import paho.mqtt.client as paho
import time
import random
import json

#hostname
broker = "markar.faisalwork.net"

#port
port=8082

def on_publish(client, userdata, result):
    print("Device 1: Data published")
    pass

client= paho.Client("admin")
client.on_publish = on_publish
client.connect(broker,port)

#create message
message= {"sensor1":}
message= json.dumps(message)
time.sleep(5)

#publish message
ret = client.publish("/data",message)
