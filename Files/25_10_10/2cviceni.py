# TODO: Vytvoř hazardní program
# 1. Zadáš, kolik chceš vsadit
# 2. Program hodí mincí
#       pokud padne orel, tak získáš dvojnásobek toho, co jsi vsadil zpět
#       pokud padne panna, prohráváš peníze, které jsi vsadil

import random
import os

money = 1000

while True:
    os.system("clear")
    print(f"You have {money} dollars")
    print("Enter how much money you want to bet:")
    bet = int(input())
    if bet > money:
        print("You don't have enough money!")
        input("Press enter to continue...")
        continue
    r = random.randint(1,6)
    print(f"You rolled {r}")
    if r == 6:
        money += bet
        print(f"You won {bet} :)")
    else:
        money -= bet
        print(f"You lost {bet} :(")
    input("Press enter to continue...")
    if money < 0:
        print("You lost!")
        break