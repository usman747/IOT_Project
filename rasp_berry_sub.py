from email import message
from operator import imod
import paho.mqtt.client as mqtt
import json
import requests
# This is the Subscriber
#hostname
broker="markar.faisalwork.net"
#port
port=8082
#time to live
timelive=60

class Planner:
    def __init__(self,broker="markar.faisalwork.net", port=8082):
        "load files"
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        self.client.message_callback_add('data/plan/daynight', self.on_message_day_or_night)
        self.client.message_callback_add('data/plan/hotcold', self.on_message_hot_or_cold)
        self.client.message_callback_add('data/plan/waiter', self.on_message_waiter_called_or_not)
        self.client.on_connect = self.on_connect
        #self.client.on_message = self.on_message
    
    def on_connect(self,clien, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe("data/#")
        
    def on_message_day_or_night(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        action = message["action"]
        print("Day OR Night action is:",message["action"])
        """
          YOUR ACTION ACTION CODE
        
        """
        
    
    def on_message_hot_or_cold(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        action = message["action"]

        print("Hot OR Cold action is:",message["action"])
        """
          YOUR ACTION ACTION CODE
        
        """
        
    
    def on_message_waiter_called_or_not(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        action = message["action"]

        print("Waiter Called action is:",message["action"])
        
        """
          YOUR ACTION ACTION CODE
        
        """
            
    def connect_to_mqtt(self):
        self.client.connect(self.broker, self.port,60)
        self.client.loop_forever()
        
        

plan = Planner()
plan.connect_to_mqtt()

