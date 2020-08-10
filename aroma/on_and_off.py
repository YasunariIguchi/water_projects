#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

path = '/home/pi/Documents/water_projects/check_on_off.txt'

subprocess.call("python /home/pi/Documents/water_projects/push_mist.py",shell=True)

with open(path,mode='r') as f:
	s = f.read()
print 's=',s

if s == "0":
	print 'hit_0'
	subprocess.call("python /home/pi/Documents/water_projects/push_light.py",shell=True)
	with open(path, mode='w') as f:
		f.write('1')

else:
	print 'not hit'
	with open(path, mode ='w') as f:
		f.write('0')
