import matplotlib.pyplot as plt
import random
import networkx as nx
from external.pp.postman_problems.solver import cpp

import sys
sys.path.append("..")

from snowymontreal.solver import solve

num_vertices = 4
is_oriented = True

while True:
    H = nx.gnp_random_graph(num_vertices, 0.7, directed=True)
    if is_oriented:
        G = nx.MultiDiGraph()
    else:
        G = nx.MultiGraph()
    i = 0
    for edge in H.edges(data=True):
        G.add_edge(edge[0], edge[1], distance=random.randint(0,100), id=i)
        i += 1

    if not nx.is_eulerian(G):
        continue
        
    edge_list = []
    for edge in G.edges(data=True):
        edge_list.append((edge[0], edge[1], edge[2]['distance']))

    cpp_circuit = cpp(G)[0]
    tot2 = 0
    for edge in cpp_circuit:
        tot2 += edge[3]['distance']

    my_circuit = solve(is_oriented, num_vertices, edge_list)
    tot1 = 0
    prev_vert = my_circuit[0]
    for cur_vert in my_circuit[1:]:
        tot1 += G[prev_vert][cur_vert][0]['distance']
        prev_vert = cur_vert

    if is_oriented:
        if tot1 != tot2:
            print("test.py: Mismatch. given: " + str(tot1) + ", expected: "
                  + str(tot2))
            for edge in G.edges(data=True):
                print(edge)
                quit()
    else:
        if len(my_circuit) != len(cpp_circuit) + 1:
            print("test.py: Mismatch. given: " + str(len(my_circuit)) +
                  ", expected: " + str(len(cpp_circuit) + 1));
            print(my_circuit)
            print(cpp_circuit)
            quit()
    print("test.py: Results match")
