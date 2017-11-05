import RPi.GPIO as GPIO
from distance_monitor import *
import led_controller
import thread

#when to turn away from an object that is sensed, in meters
turn_distance = .5
# seconds it takes to turn 90 degrees
ninety_deg_turn= .3


#left and right motor both have two controls
#set motors to different pins
left1=6
left2=13
right1=19
right2=26

#set pin output mode
GPIO.setmode(GPIO.BCM)

#set up pins
GPIO.setup(left1, GPIO.OUT)
GPIO.setup(left2, GPIO.OUT)
GPIO.setup(right1, GPIO.OUT)
GPIO.setup(right2, GPIO.OUT)

#direction to go forward
def goForward():
    GPIO.output(left1, False)
    GPIO.output(left2, True)
    GPIO.output(right1, False)
    GPIO.output(right2, True)

#direction to go backward
def goBackward():
    GPIO.output(left1, True)
    GPIO.output(left2, False)
    GPIO.output(right1, True)
    GPIO.output(right2, False)

#direction to turn left
def turnLeft():
    GPIO.output(left1, True)
    GPIO.output(left2, False)
    GPIO.output(right1, False)
    GPIO.output(right2, True)

#direction to turn right
def turnRight():
    GPIO.output(left1, False)
    GPIO.output(left2, True)
    GPIO.output(right1, True)
    GPIO.output(right2, False)

#direction to stop
def stop():
    GPIO.output(left1, False)
    GPIO.output(left2, False)
    GPIO.output(right1, False)
    GPIO.output(right2, False)

#switch variables to not check same directions too much


#sends robot to randomly explore, working with the ultrasonic radar to see if it is too close to walls
def explore():
    #check if distance is okay to move forward

    goForward()


    while getForwardDistance() > turn_distance:
        # if it is move forward and turn green light on
        continue

    # if in front there is an obstacle, turn right, check again
    slow_turn(True)

    if getForwardDistance() > turn_distance:
        explore()
    else:

        # if to the right is also covered, turn all the way around and check original left
        # if its clear go back to explore
        slow_turn(False)
        slow_turn(False)
        time.sleep(ninety_deg_turn*2)
        if getForwardDistance() > turn_distance:
            explore()
        else:

            slow_turn(False)
            explore()

def slow_turn(direction):
    i=0
    if direction==True:
        for i in range(5):
            turnRight()
            time.sleep(.05)
            stop()
    else:
        for i in range(5):
            turnLeft()
            time.sleep(.05)
            stop()

def control_lights():
    while 1:
        time.sleep(.1)
        led_controller.setGreen(False)
        led_controller.setRed(False)
        led_controller.setYellow(False)

        d = getForwardDistance()
        if d < turn_distance:
            led_controller.setRed(True)
        elif d < 2*turn_distance:
            led_controller.setYellow(True)
        else:
            led_controller.setGreen(True)

def start_led_controller():
    thread.start_new_thread( control_lights())

#start_led_controller()
