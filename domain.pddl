;Header and description

(define (domain smartcafe)

;remove requirements that are not needed
(:requirements :strips :typing)


(:types ;todo: enumerate types and their hierarchy here, e.g. car truck bus - vehicle
 temperatureSensor lightSensor PIRSensor buttonSensor
 fan LED bell - object
)

; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
(lowTempFanOff ?lt - temperatureSensor ?foff - fan)
(lowTempFanOn ?lt - temperatureSensor ?fon - fan)
(highTempFanOff ?ht - temperatureSensor ?foff - fan)
(highTempFanOn ?ht - temperatureSensor ?fon - fan)

(cafeWithLightOn ?lonn - LED)
(cafeWithLightOff ?lofff - LED)

(bellOn ?bonn - bell)
(bellOff ?bofff - bell)

(nightLightOff ?n - lightSensor ?loff - LED)
(nightLightOn ?n - lightSensor ?lon - LED)
(dayLightOff ?d - lightSensor ?loff - LED)
(dayLightOn ?d - lightSensor ?lon - LED)

(nightOutside ?OutsideN - LightSensor)
(dayOutside ?OutsideD - LightSensor)

(waiterCalled ?wc - buttonSensor)
(waiterNotCalled ?wnc - buttonSensor)

(movementDeteced ?md - PIRSensor)
(movementNotDeteced ?mnd - PIRSensor)

(waiterBellOn ?w - buttonSensor ?boff - bell)
(waiterBellOff ?w - buttonSensor ?bon - bell)
(noWaiterBellOn ?nw- buttonSensor ?boff - bell)
(noWaiterBellOff ?nw - buttonSensor ?bon - bell)

)

(:action TurnOnLights
    :parameters 
    (?SomeoneInTheRoom - PIRSensor
    ?LightSwitchOff ?LightSwitchOn - LED
    ?LowLightLevel ?HighLightLevel - LightSensors)
    :precondition (and (LowLightLightOff ?LowLightLevel ?LightSwitchOff) (MovementSensor ?SomeoneInTheRoom) )
    :effect (and (HighLightLightOn ?HighLightLevel ?LightSwitchOn) (not(LowLightLightOff ?LowLightLevel ?LightSwitchOff))
)


)

;define actions here

)


