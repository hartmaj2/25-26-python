obchod = ["chleba","banan","brnko","jablko"]


# chleba = 10
# banan = 15
# brnko = 20

inventar = []
print("Tohle je v obchode: ")
for i in range(len(obchod)):
    print(i,":",obchod[i])

penize = 10
print("Na začátku máš",penize,"korun")
print("Jaky predmet si chces koupit: ")
volba = int(input())
if penize >= 5:
    inventar.append(obchod[volba])
    penize = penize - 5
else:
    print("Nemas dost penez!")

print("Zbylo ti",penize,"korun")
print(inventar)