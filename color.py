#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO
import time

R,G,B=15,18,14
btnR, btnG, btnB=21,20,16
RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)


RPi.GPIO.setup(btnR, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(btnG, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(btnB, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)


RPi.GPIO.add_event_detect(btnR,GPIO.RISING)
if RPi.GPIO.event_detected(btnR):
	RPi.GPIO.output(B, True)
