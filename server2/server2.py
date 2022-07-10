from email import message
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
        
        self.client.message_callback_add('data/daynight', self.on_message_day_or_night)
        self.client.message_callback_add('data/hotcold', self.on_message_hot_or_cold)
        self.client.message_callback_add('data/waiter', self.on_message_waiter_called_or_not)
       
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.pddl_cold = open("./IOT_Project/AI Planning/cold.pddl",'r').read()
        self.pddl_day_w_person = open("./IOT_Project/AI Planning/DayWithPerson.pddl",'r').read()
        self.pddl_day_wo_person = open("./IOT_Project/AI Planning/DayWithoutPerson.pddl",'r').read()
        self.pddl_hot = open("./IOT_Project/AI Planning/Hot.pddl",'r').read()
        self.pddl_nigt_w_person = open("./IOT_Project/AI Planning/NightWithPerson.pddl",'r').read()
        self.pddl_night_wo_person = open("./IOT_Project/AI Planning/NightWithoutPerson.pddl",'r').read()

        self.pddl_not_pressed = open("./IOT_Project/AI Planning/NotPressed.pddl",'r').read()
        self.pddl_pressed = open("./IOT_Project/AI Planning/Pressed.pddl",'r').read()
        self.pddl_domain = open("./IOT_Project/AI Planning/domain.pddl",'r').read()
        print(self.pddl_domain)
        
    def on_connect(self,clien, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe("data/#")
    
    def on_message(slef,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        print(message)
        
    def on_message_day_or_night(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        keyfile = message['key']
        if keyfile == "day_with_person":
            file = self.pddl_day_w_person
        if keyfile == "day_without_person":
            file = self.pddl_day_wo_person
        if keyfile == "night_with_person":
            file = self.pddl_nigt_w_person
        if keyfile == "night_without_person":
            file = self.pddl_night_wo_person
            
        plan =  self.get_plan(self.pddl_domain, file)
        print("Day OR Night:",message)
        message = {"action": plan}
        message = json.dumps(message) 
        client.publish("data/plan/daynight",message)
        
    
    def on_message_hot_or_cold(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        keyfile = message['key']
        if keyfile == "hot":
            file = self.pddl_hot
        if keyfile == "cold":
            file = self.pddl_cold
        plan =  self.get_plan(self.pddl_domain, file)
        
        print("Hot OR Cold:",message)
        message = {"action": plan}
        message = json.dumps(message)
        client.publish("data/plan/hotcold",message)

    
    def on_message_waiter_called_or_not(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        keyfile = message['key']
        if keyfile == "pressed":
            file = self.pddl_pressed
        if keyfile == "not_pressed":
            file = self.pddl_not_pressed
        plan =  self.get_plan(self.pddl_domain, file)
        print("Waiter Called:",message)
        message = {"action": plan}
        message = json.dumps(message)
        client.publish("data/plan/waiter",message)
    
    def on_message_customer_present(self,client, userdata, msg):
        message = msg.payload.decode()
        message = json.loads(message)
        keyfile = message['key']
        if keyfile == "pressed":
            file = self.pddl_pressed
        if keyfile == "not_pressed":
            file = self.pddl_not_pressed
        plan =  self.get_plan(self.pddl_domain, file)
        
        print("Customer Present:",message)
        message = {"action": plan}
        message = json.dumps(message)
        client.publish("data/plan/cutomer",message)
         
    def connect_to_mqtt(self):
        self.client.connect(self.broker, self.port,60)
        self.client.loop_forever()

    def get_plan(self,domain_, problem_):
        """
        get plan for particular domain file
        """
        data = {'domain': domain_,'problem': problem_}
        response = requests.post("http://solver.planning.domains/solve",json=data).json()
        return response['result']['plan'][0]['name'].split(" ")[0].replace("(","")
        
        

plan = Planner()
plan.connect_to_mqtt()
