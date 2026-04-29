# simulation of the cow path problem
# this algorithm moves the cow by 1 -> 1 * base^(1/root) -> ...
# in any direction with probability 1/2

import random
import math
from collections.abc import Callable 

n = 257 # location of the hole in the fence
t = 100_000
base = 2
root = 1

def random_dir(d : int) -> int:
    return random.randint(0,1) * 2 - 1

def switch_dir(d : int) -> int:
    return -d

# cow flips direction randomly
def general_experiment(n : int, dir_choice_func : Callable[[int], int], init_d : int = 1) -> int:
    global fact, base
    c = 0 # total number of steps
    step = 1 # current step size
    d = init_d
    while True:
        d = dir_choice_func(d)
        if d * step >= n:
            c += n
            break
        c += 2 * step
        # step *= math.sqrt(2)
        # step *= 2
        step *= math.pow(base, 1 / root)
        step = math.ceil(step)
        
    return c

def expected_steps(n : int, t : int) -> float:
    tot = 0
    for i in range(t):
        tot += general_experiment(n,switch_dir,random.randint(0,1)*2-1)
    return tot / t

# print(experiment(k))
print(expected_steps(n,t)/n)

