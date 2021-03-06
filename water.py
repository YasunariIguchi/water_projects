#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import subprocess
import time
import sys

if (len(sys.argv) < 2):
    print("notime")
    quit()

try:
    pump_time = int(sys.argv[1])
except Exception:
    print("bad time")
    quit()

PIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
subprocess.call("node /home/pi/Documents/water_projects/start_water.js",shell=True)
time.sleep(2)
GPIO.output(PIN, False)
print("giving water for", pump_time, "sec...")
time.sleep(pump_time)
print(pump_time, "secs have passed")
GPIO.output(PIN, True)
print("giving water finished.")
subprocess.call("node /home/pi/Documents/water_projects/end_water.js",shell=True)
"""
try:
    while True:
        time.sleep(1)
        print('please finish...')
except KeyboardInterrupt:
    print('!!FINISH!!')
"""
