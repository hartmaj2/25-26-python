# Dokáží uhodnout, co jednotlivé části kódu vypíší?
# vizualizovat v Thonny

seznam = ["kočka","vločka","čočka","očka"]

# --- 0 ---
print("\nNultý:")
print("--------")
i = 0
while i < 4:
    print(i)
    i = i + 1

# --- 1 ---
print("\nPrvní:")
print("--------")
i = 0
while i < 4:
    print(seznam[i])
    i = i + 1

# --- 2 ---
print("\nDruhý:")
print("--------")
for i in range(4):
    print(seznam[i])

# --- 3 ---
print("\nTřetí:")
print("--------")
for prvek in seznam:
    print(prvek)

# What if we add another element at the end of the list