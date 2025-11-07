# V této hře na hrdinu je cílem porazit draka, jak už to tak v pohádkách bývá. Má to však jeden háček, na přípravu máme jen jeden týden. Tedy 7 dní!

# ACTIONS:
# fighting orcs - orc deals damage to hero based on ratio between player power and orc power
#  - orc power increases every day
# sleep - replenishes health to max value
# shop 
#  - herbal tea - increases max hp
#  - lucky potion - increases rewards from slain orcs and chance of winning in tavern
#  - sword upgrade - simply increases power of hero
# tavern - you bet some money (enemy must bet the same), then you roll a die and your enemy also
#  - the one who rolled more wins the bet
# dragon - epic battle which you will always lose in this demo version

import os
import random

# hero stats
gold = 0
hp = 100
base_max_hp = 100
hero_power = 1

# general info
day = 1

# shop items
shop_items = ["herbal tea", "lucky potion", "sword upgrage"]
shop_prices_base = [5,10,5]
shop_prices = shop_prices_base.copy()

luck_active = False
lucky_potions = 0
herbal_tea = 0

def print_stats():
  print(f"Day {day}")
  print_line()
  print(f"HP: {hp}/{base_max_hp + 10 * herbal_tea}")
  print(f"Power: {hero_power}")
  print(f"Gold: {gold}")

def clear_screen():
  os.system("clear")

def print_line():
  print("--------------------------------")

def petc():
   input("Press enter to continue...")

def get_user_input():
   return input("Enter your choice: ")

def print_choices():
  print_line()
  print(f"What do you want to do? ")
  print("(1) Fight orcs to gain power")
  print("(2) Go to the shop")
  print("(3) Go to the tavern")
  print("(4) Sleep")
  print("(5) Fight the dragon")
  if lucky_potions > 0:
     print("(6) Drink lucky potion")

def sleep():
   global hp, day, luck_active
   new_shop_prices()
   print("You have slept well and recovered all your health.")
   hp = base_max_hp + 10 * herbal_tea
   day += 1
   luck_active = False

def orcs():
    global hero_power, hp, gold
    orc_power = random.randint(3,9)
    damage = int(5 * (2 * day * orc_power / hero_power) + day)
    print(f"You fight with an orc with power {orc_power}. The orc dealt {damage} damage.")
    hp -= damage
    if hp > 0:
        print(f"You have slain the orc!")
        hero_power += int((orc_power * 0.1) + random.randint(1,2))
        gold += int((orc_power * 0.1) + random.randint(5,10))
        if luck_active:
           gold += random.randint(1,10)
        print(f"You received {hero_power} power and {gold} gold.")
    else:
        print(f"You died!")

def tavern():
    global gold
    print("Let's play dice against each other!")
    print("How much money do you want to bet?")
    choice = get_user_input()
    if not choice.isdigit():
        print("Invalid option")
        return
    choice = int(choice)
    if choice > gold:
        print("You don't have that much money")
    else:
        hero = random.randint(1,6)
        if luck_active and hero < 6:
           hero += 1
        opponent = random.randint(1,6)
        print(f"You rolled {hero}")
        print(f"Your opponent rolled {opponent}")
        if hero > opponent:
           print(f"You won! And you receive {choice} gold.")
           gold += choice
        elif hero == opponent:
           print("You draw. Nothing happens!")
        else:
           print(f"You lost {choice} gold.")
           gold -= choice

def new_shop_prices():
   global shop_prices_base, shop_prices
   for i in range(len(shop_prices)):
      shop_prices[i] = shop_prices_base[i] + day + random.randint(1,10)

def print_shop():
    clear_screen()
    print_stats()
    print_line()
    print("SHOP ITEMS:")
    print_line()
    for i in range(len(shop_prices)):
       print(f"({i}) {shop_items[i]} - {shop_prices[i]} gold")
    print_line()
    print("What do you want to buy: ")

def shop():
    global shop_items, shop_prices, gold, lucky_potions, herbal_tea, hero_power
    print_shop()
    choice = get_user_input()
    if not choice.isdigit():
        print("Invalid option")
        return
    choice = int(choice)
    if choice >= len(shop_items):
       print("invalid option")
       return
    if shop_prices[choice] > gold:
       print("You don't have enough money!")
       return
    gold -= shop_prices[choice]
    if choice == 0:
       herbal_tea += 1
       print("You bought a herbal tea.")
    if choice == 1:
       lucky_potions += 1
       print("You bought a lucky potion.")
    if choice == 2:
       hero_power += 5
       print("You received 5 power.")

def dragon():
   global hp
   print("You died a horrible death!")
   hp = 0

while hp > 0 and day <= 7:
    clear_screen()
    print_stats()
    print_choices()
    choice = get_user_input()
    if choice == "1":
       orcs()
    elif choice == "2":
       shop()
    elif choice == "3":
       tavern()
    elif choice == "4":
       sleep()
    elif choice == "5":
       dragon()
    elif choice == "6" and lucky_potions > 0:
       luck_active = True
       lucky_potions -= 1
       print(f"You drank a lucky potion. You will be lucky for the rest of the day. You have {lucky_potions} lucky potions left.")
    petc()
