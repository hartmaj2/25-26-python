print("Zadej číslo:")
x = int(input())



while True:
    zbytek = x % 2
    if x == 1:
        print("Konec")
        break
    if zbytek == 1:
        x = 3*x+1
    else:
        x = x // 2

    print(x)