import random
from typing import Tuple


class Player:
    def __init__(self, name: str):
        self.name = name
        self.max_hp = 30
        self.hp = self.max_hp
        self.strength = 5
        self.agility = 5
        self.intellect = 5
        self.gold = 10
        self.potions = 1
        self.weapon_bonus = 0
        self.day = 1

    def is_alive(self) -> bool:
        return self.hp > 0

    def heal_full(self) -> None:
        self.hp = self.max_hp

    def show_stats(self) -> None:
        print("\n=== STATS ===")
        print(f"Name      : {self.name}")
        print(f"Day       : {self.day}/7")
        print(f"HP        : {self.hp}/{self.max_hp}")
        print(f"Strength  : {self.strength}")
        print(f"Agility   : {self.agility}")
        print(f"Intellect : {self.intellect}")
        print(f"Weapon    : +{self.weapon_bonus} damage")
        print(f"Gold      : {self.gold}")
        print(f"Potions   : {self.potions}")
        print("=============\n")


class Enemy:
    def __init__(self, name: str, hp: int, strength: int, agility: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.strength = strength
        self.agility = agility

    def is_alive(self) -> bool:
        return self.hp > 0


# ---------- Input helpers ----------

def ask_choice(prompt: str, options: Tuple[str, ...]) -> str:
    """Ask until user enters one of given options."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Enter one of: {', '.join(options)}")


# ---------- Gameplay actions ----------

def train_stat(player: Player, stat: str) -> None:
    if stat == "str":
        player.strength += 1
        print("You train your muscles. Strength +1.")
    elif stat == "agi":
        player.agility += 1
        print("You run and dodge. Agility +1.")
    elif stat == "int":
        player.intellect += 1
        print("You study old tomes. Intellect +1.")
    else:
        return

    # Small chance to find gold while training
    if random.random() < 0.25:
        found = random.randint(1, 5)
        player.gold += found
        print(f"While training, you find {found} gold.")


def rest(player: Player) -> None:
    heal = random.randint(5, 10) + player.intellect // 2
    player.hp = min(player.max_hp, player.hp + heal)
    print(f"You take a rest and recover {heal} HP.")


def use_potion(player: Player) -> None:
    if player.potions <= 0:
        print("You have no potions.")
        return
    heal = 15
    player.potions -= 1
    player.hp = min(player.max_hp, player.hp + heal)
    print(f"You drink a potion and recover {heal} HP.")


def shop(player: Player) -> None:
    while True:
        print("\n=== SHOP ===")
        print("1) Small potion (+15 HP) - 8 gold")
        print("2) Better weapon (+1 dmg) - 15 gold")
        print("3) Leave shop")
        choice = ask_choice("> ", ("1", "2", "3"))
        if choice == "1":
            if player.gold >= 8:
                player.gold -= 8
                player.potions += 1
                print("You buy a potion.")
            else:
                print("Not enough gold.")
        elif choice == "2":
            if player.gold >= 15:
                player.gold -= 15
                player.weapon_bonus += 1
                print("You improve your weapon.")
            else:
                print("Not enough gold.")
        else:
            break


# ---------- Combat ----------

def player_attack_damage(player: Player) -> int:
    base = player.strength + player.weapon_bonus
    return max(1, base + random.randint(-2, 2))


def enemy_attack_damage(enemy: Enemy) -> int:
    base = enemy.strength
    return max(1, base + random.randint(-2, 2))


def combat(player: Player, enemy: Enemy) -> bool:
    """Returns True if player wins, False if loses."""
    print(f"\nA wild {enemy.name} appears!")
    print(f"{enemy.name} HP: {enemy.hp}")

    while player.is_alive() and enemy.is_alive():
        print(f"\nYour HP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
        print("Actions: [a]ttack, [p]otion, [r]un")
        action = ask_choice("> ", ("a", "p", "r"))

        # Player turn
        if action == "a":
            if random.random() < 0.5 + (player.agility - enemy.agility) * 0.03:
                dmg = player_attack_damage(player)
                enemy.hp -= dmg
                print(f"You hit the {enemy.name} for {dmg} damage.")
            else:
                print("You miss!")
        elif action == "p":
            use_potion(player)
        elif action == "r":
            if random.random() < 0.5 + (player.agility - enemy.agility) * 0.05:
                print("You successfully run away.")
                return True  # escape counts as “not dead”
            else:
                print("You fail to escape!")

        if not enemy.is_alive():
            break

        # Enemy turn
        if random.random() < 0.5 + (enemy.agility - player.agility) * 0.03:
            dmg = enemy_attack_damage(enemy)
            player.hp -= dmg
            print(f"The {enemy.name} hits you for {dmg} damage.")
        else:
            print(f"The {enemy.name} misses!")

    if player.is_alive():
        print(f"\nYou defeated the {enemy.name}!")
        reward_gold = random.randint(5, 12)
        player.gold += reward_gold
        print(f"You loot {reward_gold} gold.")
        return True
    else:
        print("\nYou were slain...")
        return False


def random_monster_for_day(day: int) -> Enemy:
    base_hp = 12 + day * 2
    base_str = 4 + day // 2
    base_agi = 4 + day // 2
    name = random.choice(["Goblin", "Wolf", "Bandit", "Skeleton"])
    return Enemy(name, base_hp, base_str, base_agi)


# ---------- Dragon fight ----------

def dragon_battle(player: Player) -> bool:
    print("\n=== FINAL DAY ===")
    print("You enter the dragon's lair. The final battle begins!")
    # Dragon stats depend on how much player trained
    avg_stat = (player.strength + player.agility + player.intellect) / 3
    dragon_hp = int(60 + avg_stat * 3)
    dragon_str = int(10 + avg_stat * 0.8)
    dragon_agi = int(8 + avg_stat * 0.5)
    dragon = Enemy("Dragon", dragon_hp, dragon_str, dragon_agi)

    # Heal a bit before the fight
    player.hp = min(player.max_hp, player.hp + 10)
    print("You gather your courage and recover 10 HP before the fight.")

    return combat(player, dragon)


# ---------- Main game loop ----------

def day_menu(player: Player) -> None:
    while True:
        print(f"\n=== DAY {player.day}/7 ===")
        print("What will you do?")
        print("1) Train strength")
        print("2) Train agility")
        print("3) Train intellect")
        print("4) Hunt monsters")
        print("5) Rest")
        print("6) Visit shop")
        print("7) View stats")
        print("8) Use potion")
        print("9) End the day")
        choice = ask_choice("> ", tuple(str(i) for i in range(1, 10)))

        if choice == "1":
            train_stat(player, "str")
        elif choice == "2":
            train_stat(player, "agi")
        elif choice == "3":
            train_stat(player, "int")
        elif choice == "4":
            enemy = random_monster_for_day(player.day)
            if not combat(player, enemy):
                return  # player died
        elif choice == "5":
            rest(player)
        elif choice == "6":
            shop(player)
        elif choice == "7":
            player.show_stats()
        elif choice == "8":
            use_potion(player)
        elif choice == "9":
            print("You end the day.")
            break

        if not player.is_alive():
            return


def main() -> None:
    print("=== 7 DAYS TO SLAY THE DRAGON ===")
    name = input("Enter your hero's name: ").strip() or "Hero"
    player = Player(name)

    while player.day <= 7 and player.is_alive():
        if player.day < 7:
            day_menu(player)
            if not player.is_alive():
                break
            player.day += 1
        else:
            # Day 7 -> dragon fight
            result = dragon_battle(player)
            if result and player.is_alive():
                print("\nYou have slain the Dragon. The kingdom is saved!")
            else:
                print("\nThe Dragon has defeated you. The kingdom falls into ruin.")
            break

    if not player.is_alive():
        print("\nGame over.")


if __name__ == "__main__":
    main()
