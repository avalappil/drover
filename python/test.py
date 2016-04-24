#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GREEN = 20
RED = 16
YELLOW = 21 
##
### Set all the drive pins as output pins
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)


GPIO.output(GREEN,GPIO.LOW)
GPIO.output(RED,GPIO.LOW)
GPIO.output(YELLOW,GPIO.LOW)

GPIO.output(YELLOW,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.LOW)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.LOW)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.LOW)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.HIGH)