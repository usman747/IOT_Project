from email import message
from operator import imod
import paho.mqtt.client as mqtt
import json
import requests

import pyrebase
import grovepi
from grovepi import *
import datetime

cafeLight = 3
personInCafe = 5
fan = 2
buzzer = 4

pinMode(cafeLight,"OUTPUT")
pinMode(personInCafe,"OUTPUT")
pinMode(fan,"OUTPUT")
pinMode(buzzer,"OUTPUT")

digitalWrite(cafeLight,0)
digitalWrite(personInCafe,0)
digitalWrite(fan,0)
digitalWrite(buzzer,0)

config = {     
  "apiKey": "AIzaSyCiZrawvyy5WhqXWDKCK3BiVEg9Lixgl8o",
  "authDomain": "projectiot-4500d.firebaseapp.com",
  "databaseURL": "https://projectiot-4500d-default-rtdb.firebaseio.com",
  "storageBucket": "projectiot-4500d.appspot.com"
}

firebase = pyrebase.initialize_app(config) 
database = firebase.database()

#on=False
#while True:
#    #print("HERERER")
#    if not on:
#        digitalWrite(cafeLight,1)
#        digitalWrite(personInCafe,1)
#        on = True

# This is the Subscriber
#hostname
broker="markar.faisalwork.net"
#port
port=8082
#time to live
timelive=60

last_state_1 = None
last_state_2 = None
last_state_3 = None

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
        global last_state_1
        message = msg.payload.decode()
        message = json.loads(message)
        action = message["action"]
        #print("Day OR Night action is:",message["action"])
        """
          YOUR ACTION ACTION CODE
        
        """
        #print(last_state_1) 
             
    #Actuate lights
        if action == "turnonlightsnight":
            if last_state_1 != action:
                #print(action)
                digitalWrite(cafeLight,1)
                digitalWrite(personInCafe,0)
                ear = datetime.datetime.now()
                database.child("PI").child("CAFE_LIGHT").set(1)
                database.child("PI").child("CUSTOMER_IN_CAFE").set(1)
                now = datetime.datetime.now()
                print("time taken:",(now-ear).total_seconds())
                last_state_1 =  action

            
        elif action == "turnofflightsnight":
            if last_state_1 != action:
                #print(action)
                digitalWrite(cafeLight,0)
                digitalWrite(personInCafe,0)
                database.child("PI").child("CAFE_LIGHT").set(0)
                database.child("PI").child("CUSTOMER_IN_CAFE").set(0)
                last_state_1 =  action

        
        elif action == "turnonlightsday":
            if last_state_1 != action:
                #print(action)
                digitalWrite(cafeLight,0)
                digitalWrite(personInCafe,0)
                database.child("PI").child("CAFE_LIGHT").set(0)
                database.child("PI").child("CUSTOMER_IN_CAFE").set(1)
                last_state_1 =  action

                
        elif action == "turnofflightsday":
            if last_state_1 != action:
                #print(action)
                digitalWrite(cafeLight,0)
                digitalWrite(personInCafe,0)
                database.child("PI").child("CAFE_LIGHT").set(0)
                database.child("PI").child("CUSTOMER_IN_CAFE").set(0)
                last_state_1 =  action

            
    
    def on_message_hot_or_cold(self,client, userdata, msg):
        global last_state_2
        message = msg.payload.decode()
        message = json.loads(message)
        action = message["action"]

        #print("Hot OR Cold action is:",message["action"])
        """
          YOUR ACTION ACTION CODE
        
        """
        #print(last_state_2) 
        #Actuate fan if plan is "hot"
        if action == "turnonfan":
            if last_state_2 != action:
                #print(action)
                digitalWrite(fan,1)
                database.child("PI").child("FAN").set(1)
                last_state_2 =  action
        elif action == "turnofffan":
            if last_state_2 != action:
                #print(action)
                digitalWrite(fan,0)
                database.child("PI").child("FAN").set(0)
                last_state_2 =  action
        
    
    def on_message_waiter_called_or_not(self,client, userdata, msg):
        global last_state_3
        message = msg.payload.decode()
        message = json.loads(message)
        action = message["action"]

        #print("Waiter Called action is:",message["action"])
        
        """
          YOUR ACTION ACTION CODE
        
        """
        #print(last_state_3) 
        #Actuate buzzer if pressed
        if action == "turnonbell":
            if last_state_3 != action:
                #print(action) 
                digitalWrite(buzzer,1)
                database.child("PI").child("BELL").set(1)
                last_state_3 =  action
            
        elif action == "turnoffbell":
            if last_state_3 != action:
                #print(action)
                digitalWrite(buzzer,0)
                database.child("PI").child("BELL").set(0)
                last_state_3 =  action
            
    def connect_to_mqtt(self):
        self.client.connect(self.broker, self.port,60)
        self.client.loop_forever()
        
        

plan = Planner()
plan.connect_to_mqtt()