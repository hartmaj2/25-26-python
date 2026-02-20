import random
import time

countries = [
    "South Africa",
    "Bolivia",
    "Sri Lanka",
    "Eswatini",
    "Czech Republic"
]

capitals = [
    ["Pretoria", "Cape Town", "Bloemfontein"],          # executive, legislative, judicial
    ["La Paz", "Sucre"],                                # de facto, constitutional
    ["Sri Jayawardenepura Kotte", "Colombo"],            # legislative, commercial
    ["Mbabane", "Lobamba"],                              # administrative, legislative
    ["Prague","Praha"]                                          # single capital
]

def kontrola():
    for i in range(len(capitals)):
        print(countries[i],"-",capitals[i])

def otazka():
    i = random.randint(0,4)

    print("Jaké je hlavní město",countries[i],"?")

    start = time.time()

    odpoved = input()

    end = time.time()

    if odpoved in capitals[i]:
        print("Paráda!")
    else:
        print("Ty jsi blbec")
    
    print("Trvalo ti to",round(end-start,2))

kontrola()

# for i in range(10):
#     otazka()