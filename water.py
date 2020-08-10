#! /usr/bin/env python
# -*- coding: utf-8 -*-


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

subprocess.call("sudo sh -c \"echo -n \"1-1\" > /sys/bus/usb/drivers/usb/bind\"",shell=True)
print("giving water for", pump_time, "sec...")
time.sleep(pump_time)
print(pump_time, "secs have passed")
subprocess.call("sudo sh -c \"echo -n \"1-1\" > /sys/bus/usb/drivers/usb/unbind\"",shell=True)
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
