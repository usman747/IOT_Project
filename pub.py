import paho.mqtt.client as paho
import time
import random
import json
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
    
#client.on_publish = on_publish
client.connect(broker,port)
ret= client.publish("data/daynight",get_message("day_with_person"))
ret= client.publish("data/daynight",get_message("day_without_person"))
ret= client.publish("data/daynight",get_message("night_with_person"))
ret= client.publish("data/daynight",get_message("night_without_person"))

ret= client.publish("data/hotcold",get_message("hot"))
ret= client.publish("data/hotcold",get_message("cold"))

ret= client.publish("data/waiter", get_message("pressed"))
ret= client.publish("data/waiter", get_message("not_pressed"))

#ret= client.publish("data/cutomer",message,retain=False)
#ret= client.publish("data/actlight",message,retain=False)
#ret= client.publish("data/actfan",message,retain=False)
#ret= client.publish("data/actbuzz",message,retain=False)


print("Stopped...")