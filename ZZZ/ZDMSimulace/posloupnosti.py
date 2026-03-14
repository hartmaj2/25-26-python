# Tento program jsem vytvoril abych otestoval, jak vypada pravdepodobnostni rozdeleni promenne, ktera pocita pocet souvislych useku nahodne posloupnosti nul a jednicek delky n

# 1. funkce na urceny poctu souvislych useku stejneho znaku
# 2. generovat cisla [0 , 2^n - 1]
# 3. prevest kazde na string odpovidajici binarni reprezentaci jednicek a nul 
# 4. pro kazdy pocet do dictu ulozit kolikrat nastal

def count_segments(text : str):
    c = 0
    last = ""
    for cur in text:
        if cur != last:
            c += 1
        last = cur
    return c

def get_padded_binary(i : int, k : int) -> str:
    return bin(i)[2:].zfill(k)

n = 6
counts = {}

for i in range(2**n):
    s = get_padded_binary(i,n)
    c = count_segments(s)
    if c not in counts:
        counts[c] = 0
    counts[c] += 1

print(f"{"segments":^10}{"count":^10}{"prob":<10}")
print(f"{"":-^30}")
for key,val in counts.items():
    prob = val / (2**n)
    print(f"{key:^10}{val:^10}{prob:<10.4}")