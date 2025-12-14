import serial

port = "/dev/tty.usbmodem1102" # this can be figured out by command `ls /dev/tty.*`
baudrate = 115200 # baud ... symbol (symbol can consist of multiple bytes)

ser = serial.Serial(port, baudrate)

while True:
    print(ser.readline().decode().strip())
