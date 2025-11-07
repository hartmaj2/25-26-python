# TODO: What if I want to instead print: (or in different order)
# ------------------------
# Health: xxx
# Gold: xxx
# Power: xxx
# ------------------------

def print_stats():
    print("Player stats")
    print("------------------------")
    print("Health:",gold)
    print("Gold:",gold)
    print("Power:",power)
    print("------------------------")

hp = 100
gold = 0
power = 0

print_stats()

input() # do something in the game
print("The hero defeated some orcs")
hp = hp - 10
gold = gold + 15
power = power + 1
input() # do something in the game

print_stats()


# TODO: What if I want to instead print:
# =========================
# Health: xxx
# Gold: xxx
# Power: xxx
# =========================