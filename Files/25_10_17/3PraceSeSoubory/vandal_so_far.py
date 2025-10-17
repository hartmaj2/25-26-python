x = 1
for i in range(5):
    file = open(f"soubor{x}.txt","w")
    file.write("Ahoj")
    x = x + 1