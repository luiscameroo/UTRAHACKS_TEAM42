# Required libraries:
# pip install --upgrade RPi.GPIO

import RPi.GPIO as GPIO
from time import sleep

# GPIO INITIALIZATION BELOW.

GPIO.setmode(GPIO.BCM)

# Assign motor A and B control pins
enA = 16
enB = 20
controlA = [6, 13]  # control ports for motor A are GPIO6 and GPIO13.
controlB = [19, 26]  # control ports for motor B are GPIO19 and GPIO 26.

# Set output pins for controlling Motor A and B.
GPIO.setup(controlA[0], GPIO.OUT)
GPIO.setup(controlA[1], GPIO.OUT)
GPIO.setup(controlB[0], GPIO.OUT)
GPIO.setup(controlB[1], GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

# Initialize PWM for enable motors A and B
duty_cycle = 0
pA = GPIO.PWM(enA, 1000)
pB = GPIO.PWM(enB, 1000)
pA.start(duty_cycle)
pB.start(duty_cycle)


# ROBOT CONTROL FUNCTIONS DEFINED BELOW.

# Change speed of both motors according to duty_cycle.
# NOTE: Duty cycle is value between 0 and 100.
# NOTE: to stop robot, simply call function with parameter 0.
def change_duty_cycles(newdc):
    pA.ChangeDutyCycle(newdc)
    pB.ChangeDutyCycle(newdc)
    global duty_cycle
    duty_cycle = newdc


# Set both motors to go forward.
def motors_forward():
    GPIO.output(controlA[0], 0)
    GPIO.output(controlA[1], 1)
    GPIO.output(controlB[0], 0)
    GPIO.output(controlB[1], 1)


# Set both motors to reverse.
def motors_reverse():
    GPIO.output(controlA[0], 1)
    GPIO.output(controlA[1], 0)
    GPIO.output(controlB[0], 1)
    GPIO.output(controlB[1], 0)


# Slow down speed of motor A by 50% to turn left while driving.
# NOTE: pass time in seconds.
def turn_left(time):
    pA.ChangeDutyCycle(0.5 * duty_cycle)
    sleep(time)
    pA.ChangeDutyCycle(duty_cycle)


# Slow down speed of motor B by 50% to turn right while driving.
# NOTE: pass time in seconds.
def turn_right(time):
    pB.ChangeDutyCycle(0.5 * duty_cycle)
    sleep(time)
    pB.ChangeDutyCycle(duty_cycle)


# NOTE: for below two functions, may need to sleep within if-statement to ensure robot has come to a complete stop.
# Turn robot in place clockwise.
def turn_clockwise(time):
    # Ensure duty cycle is 0 at beginning of function.
    global duty_cycle
    if duty_cycle != 0:
        duty_cycle = 0
        change_duty_cycles(0)

    # Set motor A forward and motor B reverse.
    GPIO.output(controlA[0], 0)
    GPIO.output(controlA[1], 1)
    GPIO.output(controlB[0], 1)
    GPIO.output(controlB[1], 0)

    change_duty_cycles(25)
    sleep(time)
    change_duty_cycles(0)


# Turn robot in place counter-clockwise.
def turn_c_clockwise(time):
    # Ensure duty cycle is 0 at beginning of function.
    global duty_cycle
    if duty_cycle != 0:
        duty_cycle = 0
        change_duty_cycles(0)

    # Set motor A reverse and motor B forward.
    GPIO.output(controlA[0], 1)
    GPIO.output(controlA[1], 0)
    GPIO.output(controlB[0], 0)
    GPIO.output(controlB[1], 1)

    change_duty_cycles(25)
    sleep(time)
    change_duty_cycles(0)


# MAIN RUNNING LOOP BELOW.
while True:

    with open("data.txt") as myfile:
        data = myfile.read()
