# TODO: Želva nakreslí to, jí napíšeme na vstupu

import turtle

print("Zadej volbu: ")
v = input()

if v == "ctverec":
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
elif v == "kolecko":
    for i in range(36):
        turtle.forward(5)
        turtle.left(10)
elif v == "trojuhelnik":
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
else:
    print(v + " ti fakt nenakreslím. Tak čau!")

turtle.mainloop()