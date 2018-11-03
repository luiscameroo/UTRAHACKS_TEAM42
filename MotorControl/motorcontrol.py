# Required libraries:
# pip install --upgrade RPi.GPIO

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# Assign motor A and B control pins
enA = 16
enB = 20
controlA = [6, 13] #control ports for motor A are GPIO6 and GPIO13.
controlB = [19, 26] #control ports for motor B are GPIO19 and GPIO 26.

# Set output pins for controlling Motor A and B.
GPIO.setup(controlA[0], GPIO.OUT)
GPIO.setup(controlA[1], GPIO.OUT)
GPIO.setup(controlB[0], GPIO.OUT)
GPIO.setup(controlB[1], GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

# Initialize PWM for enable motors A and B
pA = GPIO.PWM(enA, 1000)
pB = GPIO.PWM(enB, 1000)
pA.start(0)
pB.start(0)

def change_duty_cycles(duty_cycle):
    pA.ChangeDutyCycle(duty_cycle)
    pB.ChangeDutyCycle(duty_cycle)

def motors_forward():
    GPIO.output(controlA[0], 0)
    GPIO.output(controlA[1], 1)
    GPIO.output(controlB[0], 0)
    GPIO.output(controlB[1], 1)



