import turtle
import random

while True:
    x = random.randint(1, 2)
    if x == 1:
        turtle.left(90)
    if x == 2:
        turtle.left(-90)


turtle.mainloop()