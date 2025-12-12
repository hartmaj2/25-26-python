# tests experimentally the probability of a random graph being connected, acyclic or a tree

import random

import matplotlib.pyplot as plt
import networkx as nx

# create a random graph as list of neighbors

def random_graph(n : int) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if random.randint(0,1) == 1:
                graph[i].append(j)
                graph[j].append(i)
    return graph

# use dfs to check if the graph is connected

def check_conn_acyc(graph : list[list[int]]) -> tuple[bool,bool]:
    n = len(graph)
    opened_by = n * [-1]
    acyclic = True
    connected = True
    i = 0
    while i < n:
        if opened_by[i] != -1:
            i += 1 
            continue
        if i != 0:
            connected = False
        stack = [i]
        opened_by[i] = i # DON'T FORGET THIS, OTHERWISE WE WILL REOPEN THE FIRST VTX
        while len(stack) > 0:
            v = stack.pop()
            for w in graph[v]:
                if opened_by[w] != -1 and opened_by[v] != w: # if the neighbor was opened by somebody and the neighbor did not open me we found a cycle
                    acyclic = False
                elif opened_by[w] == -1: # the neighbor was not yet opened
                    opened_by[w] = v
                    stack.append(w)
        i += 1
    # print(f"{connected=} and {acyclic=}")
    return connected,acyclic

def plot_graph(graph : list[list[int]]) -> None:
    G = nx.Graph()
    G.add_nodes_from(range(len(graph)))
    for i, neighs in enumerate(graph):
        for j in neighs:
            G.add_edge(i, j)

    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

# check_conn_acyc([[1, 4], [0], [3], [2, 4], [0, 3]]) 

n = 10
trials = 100_000
conn = 0
acyclic = 0
tree = 0
for k in range(trials):
    g = random_graph(n)
    c,a = check_conn_acyc(g)
    if c and a:
        tree += 1
    if c:
        conn += 1
    if a:
        acyclic += 1

print(f"Prob that g is connected: {conn/trials}")
print(f"Prob that g is acyclic: {acyclic/trials}")
print(f"Prob that g is tree: {tree/trials}")


