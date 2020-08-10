#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PIN = 2
sleep_time = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN, False)
time.sleep(sleep_time)
GPIO.output(PIN, True)
time.sleep(sleep_time)
GPIO.output(PIN, False)
time.sleep(sleep_time)

#GPIO.cleanup()                      
