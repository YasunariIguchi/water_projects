#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

path = '/home/pi/Documents/water_projects/check_on_off.txt'

with open(path,mode='r') as f:
        s = f.read()
#print 's=',s

if s == "1":
        print 'hit'
        subprocess.call("python /home/pi/Documents/water_projects/push_mist.py",shell=True)
        with open(path, mode='w') as f:
                f.write('0')
