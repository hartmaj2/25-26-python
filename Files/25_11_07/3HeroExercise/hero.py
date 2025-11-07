# Now we will program a hero program together
# Hero has activities to do to choose from 
# Hero has some stats - hp, power, money etc.
# Each activity should somehow change the stats (decrease or increase)

# TIP: the game should involve some randomness in order to be fun (usually what is unexpected is fun)

# What is the goal of the game?

# TODO: Create variables for hero stats


money = 0
hp = 0
power = 0

# TODO: Create code that shows what is the current state of the hero (how much hp, money etc we have)

hp_text = "HP: "
money_text = "Money: "
power_text = "Power: "

print(f"{hp_text:<10}{hp}")
print(f"{money_text:10}{money}")
print(f"{power_text:10}{power}")
# TODO: Create activities and write a list of them to the player

# TODO: When player enters id of an activity, do something to the player stats