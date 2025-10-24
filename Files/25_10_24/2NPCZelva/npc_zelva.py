# TODO: Naprogramuj nahodne se pohybujici zelvu

import turtle
import random

# HINT: Predstav si, ze zelva si hazi minci a podle toho se otaci bud vlevo nebo vpravo. Jinak chodi vzdy vpred.

while True:
    turtle.forward(2)
    x = random.randint(1,3)
    if x == 1:
        turtle.left(15)
    if x == 2:
        turtle.left(-15)
