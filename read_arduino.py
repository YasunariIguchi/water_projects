import serial
import datetime
import csv
import subprocess
import sys
dry_thresh = 850
emergency_thresh = 600
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    print('waiting for data...')
    Int_data = int(ser.readline())
    time_now = datetime.datetime.now()
    print('time:', time_now)
    print('data:', Int_data)
    if Int_data >= dry_thresh :
        print('water process started')
        subprocess.call("python /home/pi/Documents/water_projects/water.py 2",shell=True)
        Int_data_before = Int_data
        print('water process finished, waiting for data_after...')
        Int_data_after = int(ser.readline())
        l =[time_now, Int_data_before, Int_data_after]

        with open('/home/pi/Documents/water_projects/log.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(l)
        print('time:', time_now)
        print('data_before:', Int_data_before)
        print('data_after:', Int_data_after)
        print('memorized')
        if Int_data_after >= emergency_thresh :
            print('emergency occured')
            with open('/home/pi/Documents/water_projects/log.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow('emergency')
            print('quit')
            sys.exit()
        else:
            print('giving water succeeded')
    else:
        print('wet enough')
    print()

        
    
    """
    if Int_data <= 807:
        print('chiisai')

    else:
        print('ookii')
    """
ser.close()
