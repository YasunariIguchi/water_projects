import serial
import datetime
import csv
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    Int_data = int(ser.readline())
    time_now = datetime.datetime.now()
    print(time_now)
    print(Int_data)
    print()

    l =[time_now, Int_data]

    with open('/home/pi/Documents/water_projects/log.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(l)
        
        
    
    """
    if Int_data <= 807:
        print('chiisai')
    else:
        print('ookii')
    """
ser.close()
