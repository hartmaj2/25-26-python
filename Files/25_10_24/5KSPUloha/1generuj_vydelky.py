import random

file = open("vydelky2.txt","w")
file.write("Vydělané peníze:")
file.write("\n")

for i in range(20):
    file.write(str(random.randint(1000,20000)))
    file.write("\n")
