import microbit as mb
import math

def sin_wave(t = 0):
    for col in range(5):
        y_sin = math.sin((math.pi / 8) * (col + t))
        for row in range(5):
            if row <= 2 + y_sin * 2:
                mb.display.set_pixel(col,row,9)
            else:
                mb.display.set_pixel(col,row,0)
t = 0
while True:
    sin_wave(t)
    mb.sleep(100)
    t += 1