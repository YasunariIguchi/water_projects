import serial
import datetime
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    Int_data = int(ser.readline())
    print(datetime.datetime.now())
    print(Int_data)
    print()
    
    """
    if Int_data <= 807:
        print('chiisai')
    else:
        print('ookii')
    """
ser.close()
