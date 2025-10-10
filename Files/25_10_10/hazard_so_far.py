import random

print("Ahoj, pojď hazardovat. To se ti vyplatí! :)")

money = 1000

print("Kolik chceš vsadit?")
sazka = int(input())

if sazka > money:
    print("Tolik peněž nemáš.")

while True:
    if  random.randint(1,2) == 1:
        print("panna")
        money = money - sazka
    else:
        print("orel")
        money = money + sazka
    print(money)
    print("Stiskni enter pro pokračování...")
    input()


