(define (problem Notpressed) (:domain smartcafe)
(:objects 
tempHigh tempLow - temperatureSensor 
lightOn lightOff - lightSensor 
personInRoom personNotInRoom - PIRSensor 
pressed notPressed - buttonSensor
fanOn fanOff - fan 
LEDOn LEDOff - LED 
bellon belloff - bell 
)

(:init
    ;todo: put the initial state's facts and numeric values here

     (noWaiterBellOn notPressed bellon)
)

(:goal (WaiterBellOff pressed belloff)  
    ;todo: put the goal condition here
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
