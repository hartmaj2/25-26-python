import random

# This is a simulation of the Monty Hall problem
# 1. the game master picks a position where to place the car
# 2. player picks one of the door


def monty(change_decision = False, force_switch = False, debug = False, n = 3) -> bool: 
    """ Returns True if user won the car. False otherwise """
    goats = [i for i in range(n)] # goat positions
    car = random.choice(goats)
    goats.remove(car)
    if debug: print(f"Game master puts car at {car}")

    possib = [i for i in range(n)] # positions that the player can pick
    guess = random.choice(possib)# let the player pick a door
    if debug: print(f"Player picks {guess}")
    if force_switch: # simulate situation, where the player doesn't want to choose random from the door he already picked when offered to change decision
        possib.remove(guess)
    if guess in goats: # Monty never shows the player the goat under his door
        goats.remove(guess)

    shown = random.choice(goats) # show one of the goats
    possib.remove(shown)
    if debug: print(f"Game master shows goat at {shown}")

    if change_decision:
        guess = random.choice(possib)
        if debug: print(f"Player switches to {guess}")

    return car == guess
        
monty(True,True)

n = 10_000
s = 0

for i in range(n):
    if monty(change_decision=True,force_switch=True):
        s += 1

print(f"Result: {s/n}")
