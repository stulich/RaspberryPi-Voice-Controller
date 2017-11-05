# ********The following code is adapted from https://www.youtube.com/watch?v=xACy8l3LsXI*******
import RPi.GPIO as GPIO
import time

#set pin boards to output mode
GPIO.setmode(GPIO.BOARD)

#assign raspberry pi pins for pins on ultrasonic sensor
#forward sensors pins
triggerForward=11
echoForward=15

#backward sensors pins
triggerBackward=12
echoBackward=16

#set trigger pins as outputs
GPIO.setup(triggerForward, GPIO.OUT)
GPIO.setup(triggerBackward, GPIO.OUT)
GPIO.output(triggerForward,0)
GPIO.output(triggerBackward,0)

#set echo pins as inputs
GPIO.setup(echoForward, GPIO.IN)
GPIO.setup(echoBackward, GPIO.IN)

#gets the distance between the sensor and closest object in front of it
def getForwardDistance():

    #turns sensor on and off and measures distance between itself and wall
    GPIO.output(triggerForward,1)
    time.sleep(0.00001)
    GPIO.output(triggerForward,0)

    while GPIO.input(echoForward)==0:
        pass
    start= time.time()

    while GPIO.input(echoForward)==1:
        pass
    stop=time.time()

    #returns the distance in meters
    #speed travels ~340m/s, distance to go to object and back is 2d, 340=2d/time ->d=170*time
    return ((stop-start)*170)

def getBackwardDistance():
    # turns sensor on and off and measures distance between itself and wall
    GPIO.output(triggerBackward, 1)
    time.sleep(0.00001)
    GPIO.output(triggerBackward, 0)

    while GPIO.input(echoBackward) == 0:
        pass
    start = time.time()

    while GPIO.input(echoBackward) == 1:
        pass
    stop = time.time()

    # returns the distance in meters
    # speed travels ~340m/s, distance to go to object and back is 2d, 340=2d/time ->d=170*time
    return ((stop - start) * 170)