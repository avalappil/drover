#!/usr/bin/env python

import pygame
import time
import os
import serial
import RPi.GPIO as GPIO
import subprocess
from espeak import espeak

GPIO.setmode(GPIO.BCM)

#servoMap = {1.00:"400",0.90:"500",0.80:"600",0.70:"700",0.60:"900",0.50:"1000",0.40:"1100",0.30:"1200",0.20:"1300",0.10:"1400",0.0:"1500",-0.10:"1600",-0.20:"1700",-0.30:"1800",-0.40:"1900",-0.50:"2000",-0.60:"2100",-0.70:"2200",-0.80:"2300",-0.90:"2400",-1.00:"2500"}

#cam position from button
vertical = 1500
horizontal = 1500
# cam position
tilt = 1500
pan = 1500
# Set which GPIO pins the drive outputs are connected
PWMA = 17
AIN1 = 27
AIN2 = 4
PWMB = 23
BIN1 = 24
BIN2 = 25
STBY = 22
STARTPROGRAM = 26
GREEN = 20
RED = 16
YELLOW = 21 

##
### Set all the drive pins as output pins
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT) 
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(STARTPROGRAM, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(GREEN,GPIO.LOW)
GPIO.output(RED,GPIO.LOW)
GPIO.output(YELLOW,GPIO.HIGH)
time.sleep(5)
# initialize Serial driver
waitForPS3 = 1
GPIO.output(GREEN,GPIO.LOW)
GPIO.output(RED,GPIO.LOW) 
while (waitForPS3 == 1):
  time.sleep(0.5)  
  
  try:
    print "starting"
    input_state = GPIO.input(STARTPROGRAM)
    GPIO.output(YELLOW,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(YELLOW,GPIO.LOW)
    if (input_state == False):
      print "button Pressed"
      print "found"
      print "exit"
      waitForPS3 = 0
  except:
    print "waiting for controller"
print "Connected"
GPIO.output(YELLOW,GPIO.LOW)
GPIO.output(GREEN,GPIO.HIGH)
GPIO.output(RED,GPIO.LOW)

# Initialise the pygame library
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

threshold = 0.30

print 'Initialized Joystick : %s' % j.get_name()


typeForArduino = ""
dataForArduino = ""

typeForServo = ""
dataForServo = ""

# Configure the motors to match the current settings.
def drive(typ, data):
  print data

def forward():
  (GPIO.output(AIN1, GPIO.HIGH))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.HIGH))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def reverse():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.HIGH))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.HIGH))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def left():
  (GPIO.output(AIN1, GPIO.HIGH))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.HIGH))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def right():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.HIGH))
  (GPIO.output(BIN1, GPIO.HIGH))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def leftonly():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.HIGH))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.LOW))
  (GPIO.output(PWMB, GPIO.HIGH))

def rightonly():
  (GPIO.output(AIN1, GPIO.HIGH))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.LOW))

def off():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.LOW))
  (GPIO.output(PWMA, GPIO.LOW))
  (GPIO.output(PWMB, GPIO.LOW))


# Try and run the main code, and in case of failure we can stop the motors
try:
    #reset servo
    # This is the main loop
    while True:
      #off()
      #time.sleep(1)
      events = pygame.event.get()

      for event in events:
        UpdateMotors = 1
        straight = 0
        turn = 0
        L2 = 0
        R2 = 0
        rotate = 0
        up = 0
        UpdateServo = 0
        stb = 0
        # Check if one of the joysticks has moved
        if event.type == pygame.JOYAXISMOTION:
          ##### right joy stick - robot control
          straight = j.get_axis(3)
          turn = j.get_axis(2) 
          straight = float("{0:.2f}".format(straight))
          turn = float("{0:.2f}".format(turn))

          #print rotate
          #print up

          L2 = j.get_button(8)
          R2 = j.get_button(9)

          u = j.get_button(4)
          d = j.get_button(6)
          l = j.get_button(7)
          r = j.get_button(5)

          ps = j.get_button(16)

          stb = j.get_button(3)

          if (ps == 1):
            GPIO.output(YELLOW,GPIO.HIGH)
            GPIO.output(GREEN,GPIO.HIGH)
            GPIO.output(RED,GPIO.HIGH)            
            espeak.synth("Shutting down the drover in 10 seconds")
            time.sleep(8)
            espeak.synth("Good bye")
            time.sleep(2)
            GPIO.output(YELLOW,GPIO.LOW)
            GPIO.output(GREEN,GPIO.LOW)
            GPIO.output(RED,GPIO.LOW)            
            subprocess.call('sudo shutdown -h now', shell=True)

          #print L2
          #print R2 



          if (UpdateMotors):
            if (L2 == 1):
              print "leftonly: "
              leftonly()
            elif (R2 == 1):
              print "rightonly: "
              rightonly()            
            elif (straight > threshold):
              print "reverse: "
              reverse()
              #time.sleep(0.1)
            elif (straight < -threshold):
              print "straight: "
              forward()
              #time.sleep(0.1)
            elif (turn > threshold):
              print "right: "
              left()
              #time.sleep(0.1)
            elif (turn < -threshold):
              print "left: "
              right()
            else:
              off()
          else:
            off()
        break

except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
    GPIO.cleanup()
finally:
  j.quit()#!/usr/bin/env python
  GPIO.cleanup() # this ensures a clean exit