seznam = ["a","b","egg","c","a","egg","d","egg","egg","chleba"]

j = 0
while True:
    if seznam[j] == "egg":
        seznam[j] = "dragon"
    j = j + 1
    if j == len(seznam):
        break


print(seznam)