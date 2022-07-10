(define (problem Hot) (:domain smartcafe)
(:objects 
tempHigh tempLow - temperatureSensor 
lightOn lightOff - lightSensor 
personInRoom personNotInRoom - PIRSensor 
pressed notPressed - buttonSensor
fanOn fanOff - fan 
LEDOn LEDOff - LED 
waiter noWaiter - bell 
)

(:init
    ;todo: put the initial state's facts and numeric values here

    (highTempFanOff tempHigh fanOff)
)

(:goal (lowTempFanOn tempLow fanOn)
    ;todo: put the goal condition here
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)