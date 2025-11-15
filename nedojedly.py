from random import randint
from math import log10, floor

N = 10000000
TAB_SPACE = 4 # [1...9]
PRINT_GAMES = False

won_keep = 0
won_pick_rand = 0
won_pick_other = 0

def tab(): 
    return "|"+" "*(TAB_SPACE-1)

for _ in range(N):
    game_set = ['G','G','G'] # G - goat, C - car
    game_set[randint(0,2)] = 'C'
    if(PRINT_GAMES):
        print(f"Game {_ + 1} with set [{game_set[0]}] [{game_set[1]}] [{game_set[2]}]:")
    choose = randint(0,2)
    if(PRINT_GAMES):
        print(tab()+f"Picked: {" "*(9 - TAB_SPACE + floor(log10(_+1))+choose*4)}^")
    # Keep the door
    if(game_set[choose] == 'C'):
        won_keep += 1
    
    game_set_other = game_set[:]
    game_set_other.pop(choose)

    # Pick other at random
    choose_other_rand = randint(0,1)
    if(game_set_other[choose_other_rand] == 'C'):
        won_pick_rand += 1

    if(PRINT_GAMES):
        spacing = 0
        if choose == 0 or choose == 1 and choose_other_rand == 1:
            spacing = 1
        print(tab()+f"Random: {" "*(9 - TAB_SPACE + floor(log10(_+1))+(spacing+choose_other_rand)*4)}^")
    
    # Pick other 
    choose_other = 0
    removed = -1
    if(game_set_other.count('G') == 2):
        choose_other = randint(0,1)
    else:
        choose_other = game_set_other.index('C')
    
    if(game_set_other[choose_other] == 'C'):
        won_pick_other += 1

    if(PRINT_GAMES):
        print(tab()+f"Other: {" "*(10 - TAB_SPACE + floor(log10(_+1)))}",end='')
        monty_pick = 0
        my_pick=0
        if choose == 1:
            if removed == -1:
                print("x   |   ^" if choose_other == 1 else "^   |   x")
            else:
                print("^   |   x" if removed == 1 else "x   |   ^")

        else:
            if choose == 0:
                print("|   ", end='')

            if removed == -1:
                print("x   ^" if choose_other == 1 else "^   x", end='')
            else:
                print("^   x" if removed == 1 else "x   ^",end='')

            if choose == 2:
                print("   |")
            else:
                print()

        print("")

print(f"After {N} games, the chance of winning is (if): ")

print(f"(a) Keeping the first choice: {won_keep*100/N}%",end='\n\n')
print(f"(b) Choose other door at random: {won_pick_rand*100/N}%",end='\n\n')
print(f"(c) Choose other door (not with the goat): {won_pick_other*100/N}%",end='\n\n')