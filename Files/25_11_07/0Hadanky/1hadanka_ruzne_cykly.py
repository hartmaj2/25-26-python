# Dokáží uhodnout, co jednotlivé části kódu vypíší?
# vizualizovat v Thonny

seznam = ["kocka","vlocka","cocka","ocka"]

# --- 0 ---
print("0.")
i = 0
while i < 4:
    print(i)
    i = i + 1

# --- 1 ---
print("1.")
i = 0
while i < 4:
    print(seznam[i])
    i = i + 1

# --- 2 ---
print("2.")
for i in range(4):
    print(seznam[i])

# --- 3 ---
print("3.")
for prvek in seznam:
    print(prvek)