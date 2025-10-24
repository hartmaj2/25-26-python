# TODO: Vytvoř 10 souborů. Do každého napiš samá voda, ale do jednoho vlož poklad!

import random

pocet_s = 30
ident = 1
x = random.randint(1,pocet_s)

for i in range(pocet_s):
    file = open(f"soubor{ident}.txt","w")
    if ident == x:
        file.write("Našel jsi poklad!")
    elif ident < x:
        file.write("Poklad má vyšší číslo kámo!")
    else:
        file.write("Poklad má nižší číslo kámo!")
    ident += 1