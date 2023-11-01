from dc_motor_libary import Motor
from machine import Pin, PWM
import machine
from time import sleep

frequency = 15000     
pin1 = Pin(5, Pin.OUT) # the pin that connected to in1
pin2 = Pin(4, Pin.OUT) # the pin that connected to in2
enable = PWM(Pin(2), 15000) # enable pin

motor = Motor(pin1, pin2, enable, False, False, False) # setup 1 motor, if 2: change the first false to pin1 of motor b, and the second and the third falses as well


speed = 100 # the speed of the motor is between -100 to 100. a negative number is a moving backward motor. if 0 the motor will stop
motor.start(speed, True) # The True value is the indicator of whether you are talking on the first motor or the second (in this code I didn't set the second motor). True = first motor. False = second motor

# This code will start the motor and it will never stop it
