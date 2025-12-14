# Notes on microbit

## IMPORTANT

- don't name your file `microbit.py` (it will then import itself instead of the module)

## Maintenance mode

Microbit can be put into maintenance mode by holding the reset button on the bottom side and while holding it connecting to the computer. Then releasing the button. The microbit will then show as MAINTENANCE folder mounted to my computer.

- [link1](https://microbit.org/get-started/user-guide/firmware/)

## Workflow

- into my program import the `microbit` module

## Using the stubs

- for intelli sense to work I need to use so called stubs
- to get them, we can use `pip install microbit-stubs`
- [link](https://pypi.org/project/microbit-stubs/)

## Flashing the microbit

- install python module "uflash" using `pip install uflash`

- to flash the program onto the microbit use `uflash <program_name>.py`
- [link](https://pypi.org/project/uflash/)

## Reading from serial port

- the microbit can send messages to the serial port (via usb cable)
  - the first thing that has to be done is to determine the port using `ls /dev/tty.*` (tty stands for teletypewriter - terminals used back in the old days to communicate with the computer)
  - in the output, find something like `/dev/tty.usbmodem1102`

- now install the pyserial module 
  - [link](https://www.pyserial.org/docs)

- use the path to the serial terminal create the following program
  - DON'T NAME THE FILE SERIAL!!!

```py
import serial

port = "/dev/tty.usbmodem1102" # this can be figured out by command `ls /dev/tty.*`
baudrate = 115200 # baud ... symbol (symbol can consist of multiple bytes)

ser = serial.Serial(port, baudrate)

while True:
    print(ser.readline().decode().strip())
```

- this program has to be running in order to listen to the serial port