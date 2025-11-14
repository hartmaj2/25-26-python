import random

#koza = 0
#ferrari = 1
vysledky = []

"""
a) - pro 999999 to chvili trva (8 sek), ale prvni tri platne cifry jsou 333 často => 0,333
b) - pro 321322 to je fast a mga dobry
c) - pro 541328 to je fakt 2/3
"""



#a
n_pokusy = int(input()) #zadejte kolikrát
p = 0                   #padne auto v úloze a

for i in range(n_pokusy):
    trojice = (random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)])) #volba kde bude ferrari
    vyber = random.randint(0, 2)                             #výběr dveří
    if trojice[vyber] == 1:                                       #jestli je v něm auto tak výhra
        p += 1                                                   #přičtu výhru k příznivým pokusům

vysledky.append(p / n_pokusy)                                        #příznivé pokusy ku všem





#2
n_pokusy = int(input()) #zadejte kolikrát
p = 0                   #padne auto v úloze b

for i in range(n_pokusy):
    trojice = (random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)]))
    vyber = random.randint(0, 2)
    nevybrane = [0,1,2]
    for j in range(len(nevybrane)):
        if trojice[j] == 0 and vyber != j: #projizdim dvirka a hledam takove, ktere jsem nevybral a je koza, abych mohl odstranit aka otevrit
            nevybrane.remove(j)
            break


    randomzedvou = random.choices(nevybrane)        # vybiram random ze 2
    if trojice[int(randomzedvou[0])] == 1:
        p += 1

vysledky.append(p / n_pokusy)     #příznivé pokusy ku všem



#3
n_pokusy = int(input()) #zadejte kolikrát
p = 0                   #padne auto

for i in range(n_pokusy):
    trojice = (random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)]))
    vyber = random.randint(0, 2)
    nevybrane = [0,1,2]
    for j in range(len(nevybrane)):
        if trojice[j] == 0 and vyber != j:
            nevybrane.remove(j)
            break

    for j in range(len(nevybrane)):
        if vyber != nevybrane[j]:                    #vezmu dvirka, na ktere jsem predtím neukázal
            if trojice[int(nevybrane[j])] == 1:     #je v nem auto (1) tak prictu
                p += 1
                break
            break

vysledky.append(p / n_pokusy)       #příznivé pokusy ku všem

for i in vysledky:
    print(f"Vysledek: {i}")