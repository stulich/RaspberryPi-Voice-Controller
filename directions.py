import RPi.GPIO as GPIO

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

#sends robot to randomly explore, working with the ultrasonic radar to see if it is too close to walls
def explore():
    #check if distance is okay to move forward

        #if it is move forward and turn green light on

        #else turn left and check if it is okay to move forward
        #if it is turn go forward

        #else turn around completely so you are now right to where you started

        #check if it is okay to travel forward else turn right 90 degrees so you are facing opposite direction of where you started
    pass