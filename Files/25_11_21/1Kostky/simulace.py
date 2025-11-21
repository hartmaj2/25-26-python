import random

vydelek = 0

for i in range(100_000_000):
    vydelek -= 1 # vstupni poplatek za hru

    h = random.randint(1,6) # hodit kostkou

    if h == 6: # zkontroluj jestli nam padla 6
        vydelek += 7
    
    # print(vydelek)
print(vydelek)

