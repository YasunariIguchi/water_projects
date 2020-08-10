import serial
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    Int_data = int(ser.readline())
    print(Int_data)
    if Int_data <= 807:
        print('chiisai')
    else:
        print('ookii')
ser.close()
