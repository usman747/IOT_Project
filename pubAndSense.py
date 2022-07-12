import pyrebase
import time
import math 
import grovepi
from grovepi import *
from time import sleep
import grove_dht_pro
import grove_light_sensor
import grove_button
import grove_ultrasonic

import paho.mqtt.client as paho
import time
import random
import json

time.sleep(0.1)#LET THE PI TURN ON AND CONNECT TO WIFI

motionDetection = 0
lightSensor = 0
buttonSensor = 0
customerInCafe = 0

#sendToMqtt = {"DayOrNight":0, "HotOrCold": 0,"WaiterCalledOrNot": 0, "CustomerPresent":0}

#hostname
broker="markar.faisalwork.net"
#port
port=8082
def on_publish(client,userdata,result):
    pass
client= paho.Client("admin")

def get_message(key):
    message = {"key":key}
    message = json.dumps(message)    
    return message

config = {     
  "apiKey": "AIzaSyCiZrawvyy5WhqXWDKCK3BiVEg9Lixgl8o",
  "authDomain": "projectiot-4500d.firebaseapp.com",
  "databaseURL": "https://projectiot-4500d-default-rtdb.firebaseio.com",
  "storageBucket": "projectiot-4500d.appspot.com"
}

firebase = pyrebase.initialize_app(config) 

database = firebase.database()

#client.on_publish = on_publish
client.connect(broker,port)


#MAIN FUNCTION
print ("PROGRAM STARTED---------------------")

while True:
    try:
    #Temperature Sensor (DHT)
        measuredTemp = grove_dht_pro.func1()
        measuredTemp = int(measuredTemp)
        if measuredTemp > 29:
            tempToSend = 1 #hot
        else:
            tempToSend = 0 #cold
        
    #Motion detection sensor
        personIn = grove_ultrasonic.func1()
        if personIn < 25:
            customerInCafe = 1 #customer is inside
        else:
            customerInCafe = 0
     
    #Light Sensor
        lightSensor = grove_light_sensor.func1()#1 -> night, 0->day      
            
    #Button Sensor, 1->WaiterCalled 0->WaiterNotCalled ..Press for 1-2sec
        buttonSensor = grove_button.func1()
        
    #Uploading Sensor Values to Firebase for visualization
        database.child("PI").child("TEMPERATURE").set(measuredTemp)
        database.child("PI").child("CUSTOMER_PRESENT").set(customerInCafe)
        database.child("PI").child("DAY_OR_NIGHT").set(lightSensor)
        database.child("PI").child("WAITER_CALLED").set(buttonSensor)
        
        
        #sendToMqtt["DayOrNight"] = lightSensor
        #sendToMqtt["HotOrCold"] = tempToSend
        #sendToMqtt["WaiterCalledOrNot"] = buttonSensor
        #sendToMqtt["CustomerPresent"] = customerInCafe
        


        
        if tempToSend == 1:
            ret= client.publish("data/hotcold",get_message("hot"))
            
        elif tempToSend == 0:            
            ret= client.publish("data/hotcold",get_message("cold"))
        
        
        if buttonSensor == 1:
            ret= client.publish("data/waiter", get_message("pressed"))
        
        elif buttonSensor == 0:
            ret= client.publish("data/waiter", get_message("not_pressed"))
        
        
        if lightSensor == 1: #means its night time
            if customerInCafe == 1: #customer in cafe
                ret= client.publish("data/daynight",get_message("night_with_person"))
            elif customerInCafe == 0:
                ret= client.publish("data/daynight",get_message("night_without_person"))
        
        if lightSensor == 0: #means daytime
            if customerInCafe == 1:
                ret= client.publish("data/daynight",get_message("day_with_person"))
            elif customerInCafe == 0:
                ret= client.publish("data/daynight",get_message("day_without_person"))
            
        time.sleep(4)
        #print("Stopped...")  
        
    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError as exp:             # Print "Error" if communication error encountered
        print ("Error:",exp)
        



        
