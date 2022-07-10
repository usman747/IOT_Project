;Header and description

(define (domain smartcafe)

;remove requirements that are not needed
(:requirements :strips :typing)

; Temp sensor     ON    high temp                  fan ON          
; Light sensor    ON(1)    high Light(day)            LED OFF
; PIR sensor      ON    someone in the room        LED ON
; Button sensor   ON    Waiter called             Bell ON

; Temp sensor     OFF    low temp                 fan OFF
; Light sensor    OFF(0) Low Light(night)         LED ON
; PIR sensor      OFF    someone not in the room  LED OFF
; Button sensor   OFF    No Waiter called         Bell Off

; night 0
;day 1


(:types ;todo: enumerate types and their hierarchy here, e.g. car truck bus - vehicle
 temperatureSensor lightSensor PIRSensor buttonSensor
 fan LED bell - object
)

; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
(lowTempFanOff ?lt - temperatureSensor ?foff - fan)   
(lowTempFanOn ?lt - temperatureSensor ?fon - fan)    ;not needed in action..maybe
(highTempFanOff ?ht - temperatureSensor ?foff - fan)   ;not needed in action..maybe
(highTempFanOn ?ht - temperatureSensor ?fon - fan)

(cafeWithLightOn ?lonn - LED)
(cafeWithLightOff ?lofff - LED)

(bellOn ?bonn - bell)
(bellOff ?bofff - bell)

(nightLightOff ?n - lightSensor ?loff - LED)  ; night hai tou light off hai
(nightLightOn ?n - lightSensor ?lon - LED)  ; night hai tou light on hai
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
(noWaiterBellOn ?nw - buttonSensor ?boff - bell)
(noWaiterBellOff ?nw - buttonSensor ?bon - bell)

)

(:action TurnOnLights
    :parameters 
    (?SomeoneInTheRoom ?SomeoneNotInTheRoom - PIRSensor      ; object= sensors and actuators
    ?LightSwitchOff ?LightSwitchOn - LED
    ?LowLightLevel ?HighLightLevel - lightSensor)    ; hight light(1) = day   low light(0)= night
    :precondition (and (nightLightOff ?LowLightLevel ?LightSwitchOff) (movementDeteced ?SomeoneInTheRoom) )
    :effect (and (nightLightOn ?LowLightLevel ?LightSwitchOn) (not(nightLightOff ?HighLightLevel ?LightSwitchOff)))
)

(:action TurnOffLights
    :parameters 
    (?SomeoneInTheRoom ?SomeoneNotInTheRoom - PIRSensor      ; object= sensors and actuators
    ?LightSwitchOff ?LightSwitchOn - LED
    ?LowLightLevel ?HighLightLevel - lightSensor)    ; hight light(1) = day   low light(0)= night
    :precondition (and (dayLightOn ?HighLightLevel ?LightSwitchOn) )
    :effect (and (dayLightOff ?HighLightLevel ?LightSwitchOff) (not(nightLightOn ?LowLightLevel ?LightSwitchOn)))
)

(:action  TurnOnFan
    :parameters (?highTemp ?lowTemp - temperatureSensor
     ?fanON ?fanOFF - fan)
    :precondition (and (highTempFanOff ?highTemp ?fanOFF))
    :effect (and (lowTempFanOn ?lowTemp ?fanON) (not(highTempFanOff ?highTemp ?fanOFF)))      ;fan on kro taka low temp ho jai
)

(:action  TurnOffFan
    :parameters (?highTemp ?lowTemp - temperatureSensor
     ?fanON ?fanOFF - fan)
    :precondition (and (lowTempFanOn ?lowTemp ?fanON))
    :effect (and (highTempFanOff ?highTemp ?fanOFF) (not(lowTempFanOn ?lowTemp ?fanON)))     ;fan off kro taka high temp ho jai
)

(:action  TurnOnBell
    :parameters (?buttonPressed ?buttonNotPressed - buttonSensor
    ?bellON ?bellOFF - bell)
    :precondition (and (waiterBellOff  ?buttonPressed ?bellOFF))
    :effect (and (noWaiterBellOn ?buttonNotPressed ?bellON) (not(waiterBellOff ?buttonPressed ?bellOFF)))
)

(:action  TurnOffBell
    :parameters (?buttonPressed ?buttonNotPressed - buttonSensor
    ?bellON ?bellOFF - bell)
    :precondition (and (noWaiterBellOn  ?buttonNotPressed ?bellON))
    :effect (and (WaiterBellOff ?buttonPressed ?bellOFF) (not(noWaiterBellOn ?buttonNotPressed ?bellON)))
)
;define actions here
)