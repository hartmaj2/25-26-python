pns_left = [DigitalPin.P0, DigitalPin.P3, DigitalPin.P6, DigitalPin.P9]
pns_right = [DigitalPin.P16, DigitalPin.P15, DigitalPin.P13, DigitalPin.P10]

def reset_pins(pns : List[number]):
    for p in pns:
        pins.digital_write_pin(p, 0)

def blink_pins(pns : List[number],t):
    for p in pns:
        pins.digital_write_pin(p, 1)
        pause(t)
        pins.digital_write_pin(p, 0)

def flash_pins(pns : List[number], t):
    for p1 in pns:
        pins.digital_write_pin(p1, 1)
    pause(t)
    for p2 in pns:
        pins.digital_write_pin(p2, 0)  

led.enable(False)

reset_pins(pns_left + pns_right)

while True:
    blink_pins(pns_left,100)
    pause(200)
    blink_pins(pns_right,100)

    flash_pins(pns_left,200)
    pause(200)
    flash_pins(pns_right,200)
    pause(200)

    blink_pins(pns_left[::-1],100)
    pause(200)
    blink_pins(pns_right[::-1],100)