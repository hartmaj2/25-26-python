import microbit as mb

while True:
    mb.pin2.write_digital(1)
    mb.sleep(1000)
    mb.pin2.write_digital(0)
    mb.sleep(1000)
    print("Hello world mbit")