import random
import time

start = time.time()

while True:
    print(round(time.time()-start,2))

states = ["Česká republika","Slovensko","Německo","Rakousko","Polsko","Francie","Itálie","Španělsko","Velká Británie","USA"]

capitals = ["Praha","Bratislava","Berlín","Vídeň","Varšava","Paříž","Řím","Madrid","Londýn","Washington, D.C."]

def otazka():
    i = random.randint(0,9)

    print("Jaké je hlavní město",states[i],"?")

    odpoved = input()

    if odpoved == capitals[i]:
        print("Paráda!")
    else:
        print("Ty jsi blbec")

