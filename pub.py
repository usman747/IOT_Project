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
#client.on_publish = on_publish
client.connect(broker,port)
message={"problemfile": "abcd.pddl"} # any key value
message = json.dumps(message)    
    #publish message
ret= client.publish("data/daynight",message,retain=False)
ret= client.publish("data/hotcold",message,retain=False)
ret= client.publish("data/waiter",message,retain=False)
ret= client.publish("data/cutomer",message,retain=False)
ret= client.publish("data/actlight",message,retain=False)
ret= client.publish("data/actfan",message,retain=False)
ret= client.publish("data/actbuzz",message,retain=False)


print("Stopped...")