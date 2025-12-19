import microbit as mb

phases : list[list[mb.MicroBitTouchPin]] = [[mb.pin0],[mb.pin0,mb.pin1],[mb.pin2],[mb.pin1]] # 0 - red, 1 - yellow, 2 - green

def pins_write(pins : list[mb.MicroBitTouchPin], value : int):
    for pin in pins:
        pin.write_digital(value)

i = 0
while True:
    i += 1
    if i == 4:
        i = 0
    pins_write(phases[i],1)
    if i == 1 or i == 3: # wait longer if on in-between-states
        mb.sleep(500)
    else:
        mb.sleep(2000)
    pins_write(phases[i],0)