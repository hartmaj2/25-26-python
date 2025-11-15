import random

#počítadlo že došlo k výhře
a = 0
b = 0
c = 0

#počet pokusů
n = 182

#postup soutěže
for soutez in range(n):
    
    #příprava výher za dveřmi (1 = auto, 0 = koza)
    vyhry = [1,0,0]
    random.shuffle(vyhry)

    #hráčův výběr
    hrac = random.randint(0,2)
    vybrane = vyhry[hrac]

    #odstranění jednich z dveří, za kterými je koza
    for i in range(0,3):
        if vyhry[i] == 0 and i != hrac:      #kontrola zda se nejedná o vybrané dveře a o ty, za kterými je auto
            vyhry.pop(i)
            break

    #původní volba
    if vybrane == 1:
        a += 1
        
    #náhodně
    nahodne = random.choice(vyhry)
    if nahodne == 1:
        b += 1

    #ty zbylé
    if vybrane == 0:
        c += 1

print("Původní volba: "+str(a/n*100)+"%")   #odpovídá přibližně 1/3
print("Náhodná volba: "+str(b/n*100)+"%")   #odpovídá přibližně 1/2
print("Změnit volbu: "+str(c/n*100)+"%")    #odpovídá přibližně 2/3