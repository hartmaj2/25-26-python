import random

vydelek = 0

test = 26

while True:
    vydelek -= 1 # vstupni poplatek za hru

    soucet = 0
    for i in range(6):
        soucet += random.randint(1,6) # hodit kostkou

    if soucet == test: # zkontroluj jestli nam padla 6
        vydelek += test
    
    print(vydelek)

