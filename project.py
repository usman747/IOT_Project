
import pyrebase
import time
import math #for dht sensor
import grovepi
from grovepi import *
from time import sleep
import grove_dht_pro
import grove_pir_motion_sensor
import grove_light_sensor
import grove_button
import grove_rotary_angle_sensor

led1 = 4
led2 = 3
fan = 2

measuredTemp = 0
motionDetection = 0
lightSensor = 0
buttonSensor = 0
potAngle = 0

personCounter = 0 

config = {     
  "apiKey": "AIzaSyCiZrawvyy5WhqXWDKCK3BiVEg9Lixgl8o",
  "authDomain": "projectiot-4500d.firebaseapp.com",
  "databaseURL": "https://projectiot-4500d-default-rtdb.firebaseio.com",
  "storageBucket": "projectiot-4500d.appspot.com"
}

firebase = pyrebase.initialize_app(config) 

database = firebase.database()
#database.child("PI").child("TEMP").set("27")
#database.child("PI").child("TEMP").push("23")
#database.child("PI").child("TEMP").set("45")
#leep(1)
#database.child("PI").child("TEMP").set("46")
#sleep(1)
#database.child("PI").child("TEMP").set("47")

#database.child("PI").child("CUSTOMERS").set("1")


#ProjectBucket = database.child("PI")
#getTemp = ProjectBucket.child("TEMPERATURE").get().val()
#print ("THE value is" )
#print (getTemp)

pinMode(led1,"OUTPUT")
pinMode(led2,"OUTPUT")
pinMode(fan,"OUTPUT")
time.sleep(0.1)

digitalWrite(led1,0)     
digitalWrite(led2,0)
digitalWrite(fan,0)

#MAIN FUNCTION
print ("PROGRAM STARTED---------------------")

while True:
    try:
    #Temperature Sensor (DHT)
        measuredTemp = grove_dht_pro.func1()
        #print("measured temp below me")
        #print(measuredTemp)
        
    #Motion detection sensor
        motionDetection = grove_pir_motion_sensor.func1()
        #print("Motion detected from sensor")
        #print(motionDetection)
        if motionDetection==1:
            personCounter = personCounter + 1;
            #print("I am counting persons")
            #print(personCounter)
     
    #Light Sensor
        lightSensor = grove_light_sensor.func1()#0 -> night, 1->day
        #print("Light sensor output is below me")
        #print(lightSensor)        
            
    #Button Sensor, 1->Customer calling 0->Customer idle..Press for 1-2sec
        buttonSensor = grove_button.func1()
        #print("Button sensor output is below me")
        #print(buttonSensor)
        
    #Potentiometer Angle Sensor
        potAngle = grove_rotary_angle_sensor.func1()#0 -> night, 1->day
        #print("Pot Angle is below me (in degrees)")
        #print(potAngle)
        
    #Uploading Sensor Values to Cloud
        database.child("PI").child("TEMPERATURE").set(measuredTemp)
        database.child("PI").child("PERSON_COUNT").set(personCounter)
        database.child("PI").child("DAY_OR_NIGHT").set(lightSensor)
        database.child("PI").child("WAITER_CALLED").set(buttonSensor)
        database.child("PI").child("BRIGHTNESS").set(potAngle)
        time.sleep(0.1)
        
    #Downloading Sensor Values from Cloud
        ProjectBucket = database.child("PI")
        tempFromCloud = ProjectBucket.child("TEMPERATURE").get().val()
        #print("Temperature received from cloud")
        #print(tempFromCloud)
        ProjectBucket = database.child("PI")
        personCountCloud = ProjectBucket.child("PERSON_COUNT").get().val()
        
        ProjectBucket = database.child("PI")
        dayOrNightCloud = ProjectBucket.child("DAY_OR_NIGHT").get().val()

        ProjectBucket = database.child("PI")
        waiterCalledCloud = ProjectBucket.child("WAITER_CALLED").get().val()
    
        ProjectBucket = database.child("PI")
        brightnessCloud = ProjectBucket.child("BRIGHTNESS").get().val()
        
    # Actuate fan if condition true
        if tempFromCloud > 29:
            digitalWrite(fan,1)
            #print("HERE")
            
        else:
            digitalWrite(fan,0)
            
            
        
    # Actuate lights
        if dayOrNightCloud == 0: #if night 
            if personCountCloud > 0:
                digitalWrite(led1,1) #2 customer, 1 light on
        
            if personCountCloud > 2: #4 customer, 2lights on
                digitalWrite(led2,1)
        else: #if daytime then turn off lights irrespective of customers
            digitalWrite(led1,0)
            digitalWrite(led2,0)
            
        
    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print ("Error")
        
       

        
