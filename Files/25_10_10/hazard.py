# TODO: Vytvoř hazardní program
# 1. Zadáš, kolik chceš vsadit
# 2. Program hodí mincí
#       pokud padne orel, tak získáš dvojnásobek toho, co jsi vsadil zpět
#       pokud padne panna, prohráváš peníze, které jsi vsadil

import random
import os

money = 100000

print(f"Ahoj fešáku, pojď hazardovat!")
input("Stiskni enter pro pokračování...")

while True:
    os.system("clear")
    print(f"Máš {money} korun")
    print("Kolik chceš vsadit bratře?")
    bet = int(input())
    if bet > money:
        print("Na to nemáš prachy kámo!")
        input("Stiskni enter pro pokračování...")
        continue
    r = random.randint(1,6)
    print(f"Hodil jsi {r}")
    if r == 6:
        money += bet
        print(f"Vyhrál jsi {bet} :)")
    else:
        money -= bet
        print(f"Prohrál jsi {bet} :(")
    input("Stiskni enter pro pokračování...")
    if money <= 0:
        os.system("clear")
        print("Přišel jsi o všechny prachy.")
        input("Stiskni enter pro pokračování...")
        os.system("clear")
        print("Nemáš peníze na to abys uživil děti a žena tě vykopla z domu")
        input("Stiskni enter pro pokračování...")
        os.system("clear")
        print("Musíš jít smažit hambáče do mekáče, aby sis vydělal něco málo zpět")
        input("Stiskni enter pro pokračování...")
        os.system("clear")
        print("MILÉ DĚTI, HAZARD JE ŠPATNÝ, NEDĚLEJTE TO")
        break