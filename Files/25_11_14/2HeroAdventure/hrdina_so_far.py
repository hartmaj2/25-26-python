import os

hp = 100
gold = 0
power = 1

def vytiskni_stats():
    cara = "------------------------------------"
    print(cara)
    print("HP:",hp)
    print("GOLD:",gold)
    print("POW:",power)
    print(cara)

def vytiskni_moznosti():
    print("(1) - Spanek")
    print("(2) - Bojovani")
    print("(3) - Taverna")
    print("(4) - Obchod")

while True:
    os.system("clear")
    vytiskni_stats()
    vytiskni_moznosti()
    volba = input("Zadej tvou volbu: ")
    if volba == "1":
        print("Krasne ses vyspal")
    elif volba == "2":
        print("Bojujes se skrety")
    input("Press enter to continue...")