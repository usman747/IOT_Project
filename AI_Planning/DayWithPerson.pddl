(define (problem DayWithPerson) (:domain smartcafe)
(:objects 
tempHigh tempLow - temperatureSensor 
lightOn lightOff - lightSensor    ; Lighton=day lightoff=night
personInRoom personNotInRoom - PIRSensor 
pressed notPressed - buttonSensor
fanOn fanOff - fan 
LEDOn LEDOff - LED 
waiter noWaiter - bell 
)

(:init
    ;todo: put the initial state's facts and numeric values here
    (dayLightOff lightON LEDOff)
    (movementDeteced personInRoom)
)

(:goal ( dayLightON lightON LEDOn)
    ;todo: put the goal condition here
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
