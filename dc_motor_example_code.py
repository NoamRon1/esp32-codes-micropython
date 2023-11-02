from dc_motor_libary import Single_Motor, Two_Motors
from machine import Pin, PWM
import machine
from time import sleep
import time

frequency = 15000     
pin1 = Pin(5, Pin.OUT) # the pin that connected to in1
pin2 = Pin(4, Pin.OUT) # the pin that connected to in2
enable = PWM(Pin(2), 15000) # enable pin

motor = Single_Motor(pin1, pin2, enable) # setup 1 motor
#two_motors = Two_Motors(pin1a, pin2a, enablea, pin1b, pin2b, enableb) # setup 2 motors as a pair


speed = 100 # The speed of the motor is between -100 to 100. a negative number is a moving backward motor. if 0 the motor will stop
motor.start(speed) # This will start the motor forever at a speed of 100.
#two_motors.start(speed, True) # The True value is the indicator of whether you are talking on the first motor or the second (in this code I didn't set the second motor). True = first motor. False = second motor


during = 10 # the time of the motor will be on (in sec)
motor.timemove(speed, during) # this code will start the motor for 10 sec and will stop it after
#second_speed = 50
#two_motors.timemove(speed, second_speed, during) # this will start one of the motors at 100 speed and the other for 50, for 10 sec and will stop it after

