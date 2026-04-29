# simulation of the cow path problem
# this algorithm moves the cow by 1 -> 1 * base^(1/root) -> ...
# in any direction with probability 1/2

import random
import math

k = 1000 # location of the hole in the fence
t = 100_000
base = 2
root = 2

def experiment(k : int) -> int:
    global fact, base
    c = 0 # total number of steps
    step = 1 # current step size
    while True:
        d = random.randint(0,1) * 2 - 1 # direction of the cow in this step
        if d * step >= k:
            c += k
            break
        c += 2 * step
        # step *= math.sqrt(2)
        # step *= 2
        step *= math.pow(base, 1 / root)
        step = math.ceil(step)
        
    return c

def expected_steps(k : int, t : int) -> float:
    tot = 0
    for i in range(t):
        tot += experiment(k)
    return tot / t

# print(experiment(k))
print(expected_steps(k,t))

