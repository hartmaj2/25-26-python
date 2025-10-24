file = open("Files/25_10_24/5KSPUloha/vydelky.txt")

suma = 0
file.readline()
for i in range(5):
    data = file.readline()
    suma += int(data)

print(f"Celkem sis vydělal {suma} korun")