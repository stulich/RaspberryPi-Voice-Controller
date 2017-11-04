import RPi.GPIO as GPIO

#left and right motor both have two controls
#set motors to different pins
left1=6
left2=13
right1=19
right2=26

#set up pins
GPIO.setup(left1, GPIO.OUT)
GPIO.setup(left2, GPIO.OUT)
GPIO.setup(right1, GPIO.OUT)
GPIO.setup(right2, GPIO.OUT)

#direction to go forward
def goFoward():
    GPIO.output(left1, True)
    GPIO.output(left2, False)
    GPIO.output(right1, True)
    GPIO.output(right2, False)

#direction to go backward
def goBackward():
    GPIO.output(left1, False)
    GPIO.output(left2, True)
    GPIO.output(right1, False)
    GPIO.output(right2, True)

#direction to turn left
def turnLeft():
    GPIO.output(left1, False)
    GPIO.output(left2, True)
    GPIO.output(right1, True)
    GPIO.output(right2, False)

#direction to turn right
def turnRight():
    GPIO.output(left1, True)
    GPIO.output(left2, False)
    GPIO.output(right1, False)
    GPIO.output(right2, True)

#direction to stop
def stop():
    GPIO.output(left1, False)
    GPIO.output(left2, False)
    GPIO.output(right1, False)
    GPIO.output(right2, False)