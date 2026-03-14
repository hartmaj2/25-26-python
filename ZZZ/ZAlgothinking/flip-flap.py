# simulates probability of flip flap flop team creating scheme
# the general formula should be \binom{n}{n/2} / 2^n

import random

n = 6
t = 1_000_000
debug = False

def trial(n : int) -> bool:
    l = []
    for i in range(n):
        l.append(random.randint(0,1))
    good = sum(l) == n // 2
    if debug: print(f"{l} is {good}")
    return good

s = 0

for i in range(t):
    if trial(n):
        s += 1

print(f"Probability is {s/t}")