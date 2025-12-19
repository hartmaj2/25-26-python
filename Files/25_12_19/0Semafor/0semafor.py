import microbit as mb

pins : list[mb.MicroBitTouchPin] = [mb.pin0,mb.pin1,mb.pin2] # 0 - red, 1 - yellow, 2 - green

s = 1
i = 0

while True:
    i += s
    if i == 2 or i == 0: # change direction if on edge
        s = -s
    pins[i].write_digital(1)
    if i == 1: # wait longer if on yellow
        mb.sleep(500)
    else:
        mb.sleep(2000)
    pins[i].write_digital(0)