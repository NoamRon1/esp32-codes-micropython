from dcmotor import DCMotor
from machine import Pin, PWM
import machine
from time import sleep
#dc motor setup
frequency = 15000     
pin1 = Pin(5, Pin.OUT) # the pin that connected to in1
pin2 = Pin(4, Pin.OUT) # the pin that connected to in2
enable = PWM(Pin(2), frequency) # enable pin
dc_motor = DCMotor(pin1, pin2, enable)
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)

#code
dc_motor.forward(100) #100 is the speed of the motor
sleep(3)
dc_motor.stop() # stoping the motor

# this code will start the motor for 3 seconds and after that it will stop it.
# you can replace the "forward" method to "backwards" too for changing the direction.
