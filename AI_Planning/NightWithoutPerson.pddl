(define (problem NightWithoutPerson) (:domain smartcafe)
(:objects 
tempHigh tempLow - temperatureSensor 
lightOn lightOff - lightSensor ; Lighton=day lightoff=night
personInRoom personNotInRoom - PIRSensor 
pressed notPressed - buttonSensor
fanOn fanOff - fan 
LEDOn LEDOff - LED 
waiter noWaiter - bell 
)

(:init
    ;todo: put the initial state's facts and numeric values here
    (nightLightOn lightOff LEDOn)
    (movementNotDeteced personNotInRoom) 
)

(:goal (nightLightOFF lightOff LEDOff)
    ;todo: put the goal condition here
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
