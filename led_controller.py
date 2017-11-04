import RPi.GPIO as GPIO

#assigns pin numbers that will control the different colored leds
greenLed=21
yellowLed=20
redLed=16

#set pin output mode
GPIO.setmode(GPIO.BCM)

#sets up the different pins as outputs
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)

#turns green light on/off based on status being true or false
def setGreen(status):
    GPIO.output(greenLed, status)

#turns yellow light on/off based on status being true or false
def setYellow(status):
    GPIO.output(yellowLed, status)

#turns red light on/off based on status being true or false
def setRed(status):
    GPIO.output(redLed, status)

