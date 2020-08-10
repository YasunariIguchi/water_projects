#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time

on_min = 15


path = '/home/pi/Documents/water_projects/check_on_off.txt'

with open(path,mode='r') as f:
    s = f.read()

if s == "0":
    subprocess.call("python /home/pi/Documents/water_projects/push_mist.py",shell=True)
    subprocess.call("python /home/pi/Documents/water_projects/push_light.py",shell=True)
    with open(path, mode='w') as f:
        f.write('1')
        print 'now_on'

time.sleep(60 * on_min)

subprocess.call("python /home/pi/Documents/water_projects/push_mist.py",shell=True)
with open(path, mode ='w') as f:
    f.write('0')
    print 'now_off'
