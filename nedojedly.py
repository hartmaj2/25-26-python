from random import randint

def user_print_games():
    """Asks the user if he wants to print each game"""
    to_print = False
    user = str(input("Print each simulated game? [y/N]: "))
    if len(user) == 1 and (user[0] == 'y' or user[0] == 'Y'):
        to_print = True
    return to_print

def user_number_of_games():
    """Asks the user to choose the number of games to simulate"""
    user = int(input("Enter the number of games to simulate: "))
    if user <= 0:
        ValueError("Invalid number of games, enter only natural number.")
        exit(-1)
    return user

def print_header(sep_width=40):
    """Prints the welcome message"""
    print("Monty Hall problem simulator")
    print("-" * sep_width)

def print_simulation_info(sep_width=40):
    print("^ my choice")
    print("x monty opened this door")
    print("R my random pick")
    print("-"*sep_width)


def print_footer(won_keep, won_rand, won_monty, nof_games, sep_width=40):
    """Prints the results of the simulation"""
    print("-"*sep_width)

    print(f"Simulated {nof_games} games.")
    print("-"*sep_width)

    print(f"The chance of winning is (if you): ")

    print("(a) Keep the first choice:", f"{won_keep*100/nof_games:.2f}%".rjust(14,' '),end='\n')
    print("(b) Choose other door at random:", f"{won_rand*100/nof_games:.2f}%".rjust(8, ' '),end='\n')
    print("(c) Choose the other door:", f"{won_monty*100/nof_games:.2f}%".rjust(14,' '),end='\n')

def print_game_init(game, game_n, sep_width=40):
    print(f"# Running simulation {game_n + 1}:  ".ljust(sep_width,'#'))
    print(f"Game set: {game}")

def print_game_my_pick(game, char_for_monty = 'x', char_for_me = '^'):
    print(" "*10,
          f"{char_for_monty if game.monty_pick == 0 else (char_for_me if game.my_pick == 0 else ' ')} ",
          f"{char_for_monty if game.monty_pick == 1 else (char_for_me if game.my_pick == 1 else ' ')} ",
          f"{char_for_monty if game.monty_pick == 2 else (char_for_me if game.my_pick == 2 else ' ')}",
          sep='')

def print_game_my_random_pick(game, char_for_me = 'R'):
    print(" "*10,f"{" "*game.my_random_pick*2}{char_for_me}", sep='')

def print_game_results(game, nof_games, sep_width=40):
    print("-"*sep_width)
    won = False
    if game.won_if_keeping():
        print("Won if keeping the first choice.".rjust(sep_width,' '))
        won = True
    if game.won_if_monty():
        print("Won if picked the other door.".rjust(sep_width, ' '))
        won = True
    if game.won_if_random():
        print("Won if randomly picked the other door.".rjust(sep_width, ' '))
        won = True
    if not won:
        print("Did not won.".rjust(sep_width,' '))
    print("#"*sep_width)
    print()

def get_left_or_right_to(index, left_or_right):
    """
    Calculates the left or right index for array of length 3 in relation to given index, f.e.

        <x> given index; [x] returned index;

        index=2, left_or_right=0; [0] 1 <2>

        index=2, left_or_right=1; 0 [1] <2>

        index=1; left_or_right=1; 0 <1> [2]

    :param index: Index to ignore
    :param left_or_right: Left or right index of the reaming two; 0 for left, 1 for right
    :return: The calculated index
    """
    if index == 0:
        return 1 + left_or_right
    if index == 1:
        return 0 if left_or_right == 0 else 2
    return left_or_right


class MontyGameSet:
    """ Creates a Monty Game Set """
    def __init__(self, char_for_goat='G', char_for_car='C'):
        self.set = [char_for_goat, char_for_goat, char_for_goat]
        self.set[randint(0,2)] = char_for_car
        self.char_for_goat = char_for_goat
        self.char_for_car = char_for_car
        self.monty_pick = -1

    def index_of_monty_pick(self, index_of_my_pick:int):
        """ Calculates which door did monty pick if we picked 'index_of_my_pick' """
        if self.monty_pick != -1:
            return self.monty_pick

        left_or_right = randint(0,1) # 0 - he picked the left door, 1 - he picked the right door from the remaining two
        self.monty_pick = get_left_or_right_to(index_of_my_pick, left_or_right)

        # If monty picked a car
        if self.set[self.monty_pick] == self.char_for_car:
            # pick in the other direction
            self.monty_pick = get_left_or_right_to(index_of_my_pick, 1 if left_or_right == 0 else 0)

        return self.monty_pick

    def __getitem__(self, item):
        if item < 0 or item > 2:
            ValueError("Can't get index out of range.")
        return self.set[item]

class MontyGame:
    """
    Creates one Monty game, which picks some door, and calculates each possibility of playing:

    (a) sticking to the first choice
    (b) choosing other door (excluding the door that Monty picked) at random
    (c) switching to the other door
    """
    def __init__(self, char_for_goat='G', char_for_car='C'):
        self.game_set = MontyGameSet(char_for_goat, char_for_car)
        self.my_pick = randint(0,2)
        self.monty_pick = self.game_set.index_of_monty_pick(self.my_pick)
        test_pick = get_left_or_right_to(self.my_pick, 0)
        self.monty_pick_other = test_pick if test_pick != self.monty_pick else get_left_or_right_to(self.my_pick, 1)
        self.my_random_pick = [self.monty_pick_other, self.my_pick][randint(0,1)]

    def __repr__(self):
        return f"{self.game_set.set[0]} {self.game_set.set[1]} {self.game_set.set[2]}"

    def won_at(self, index):
        """Is 'index' a winning door?"""
        if index < 0 or index > 2:
            ValueError("Can't get index out of range.")
            return False
        return self.game_set[index] == self.game_set.char_for_car

    def won_if_keeping(self):
        return self.won_at(self.my_pick)

    def won_if_monty(self):
        return self.won_at(self.monty_pick_other)

    def won_if_random(self):
        return self.won_at(self.my_random_pick)




if __name__ == "__main__":
    print_header()
    nof_games=user_number_of_games()
    print_games = user_print_games()

    if print_games:
        print_simulation_info()

    won_keep = 0
    won_rand = 0
    won_monty = 0

    for i in range(nof_games):
        game = MontyGame()

        if print_games:
            print_game_init(game, i)

        # Keeping the wirst choice
        if game.won_if_keeping():
            won_keep+=1
        if print_games:
            print_game_my_pick(game)

        # Choosing other, then the door Monty opened, at random
        if game.won_if_random():
            won_rand+=1
        if print_games:
            print_game_my_random_pick(game)

        # Opening the other door - not pick at first
        if game.won_if_monty():
            won_monty+=1

        if print_games:
            print_game_results(game, nof_games)


    print_footer(won_keep, won_rand, won_monty, nof_games)