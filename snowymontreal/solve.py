from snowymontreal.hungarian import match_hungarian
from snowymontreal.floyd_warshall import floyd_warshall
from snowymontreal.hierholzer import hierholzer

import sys

def incr_insert(l, e):
    for i in range(len(l)):
        if e < l[i]:
            l.insert(i, e)
            return
    l.append(e)

def add_edge(src, dst, dist, M, M2, degrees):
    incr_insert(M[src][dst], dist)
    degrees[src] += 1
    degrees[dst] -= 1
    M2[src][dst] += 1

def build_matrix(is_oriented, num_vertices, edge_list):
    M = []
    M2 = []
    degrees = [0] * num_vertices
    for i in range(num_vertices):
        l = []
        l2 = [0] * num_vertices
        for k in range(num_vertices):
            l.append([])
        M.append(l)
        M2.append(l2)
    for (src, dst, dist) in edge_list:
        inner = []
        add_edge(src, dst, dist, M, M2, degrees)
        if not is_oriented:
            add_edge(dst, src, dist, M, M2, degrees)
    return (M, M2, degrees)

def build_bipartite(adj, degrees, n):
    m = 0
    for degree in degrees: # do this when retrieving degrees
        if degree != 0:
            m += abs(degree)
    M = [[float('inf') for i in range(m)] for j in range(m)] 
    ids = [-1] * m
    i = 0
    for k in range(n):
        if degrees[k] != 0:
            ids[i] = k
            j = 0
            for l in range(n):
                if degrees[l] != 0:
                    if degrees[k] < 0 and degrees[l] > 0:
                        M[i][j] = adj[k][l]
                        M[j][i] = adj[k][l]
                    j += 1
            for h in range(abs(degrees[k])-1):
                for g in range(m):
                    M[m-i-1][g] = M[i][g]
                    M[g][m-i-1] = M[i][g]
                ids[m-i-1] = k
            i += 1
    return (M, ids)

def dup_path(M2, p, src, dst):
    M2[src][dst] += 1;
    if p[src][dst] == src:
        return
    dup_path(M2, p, src, p[src][dst])

def get_oriented_indices(matching, ids, degrees):
    l = []
    for edge in matching:
        start = -1;
        end = -1;
        for elt in edge:
            if degrees[ids[elt]] > 0:
                end = ids[elt]
            else:
                start = ids[elt]
        l.append((start, end))
    return l

def add_duplicates(M, parent, indices):
    for (start, end) in indices:
        dup_path(M, parent, start, end)
    
def solve(is_oriented, num_vertices, edge_list):
    (M, M2, degrees) = build_matrix(is_oriented, num_vertices, edge_list)
    (shortest, parent) = floyd_warshall(M, num_vertices)
    (bipartite, ids) = build_bipartite(shortest, degrees, num_vertices)
    matching = match_hungarian(bipartite, degrees, ids)
    indices = get_oriented_indices(matching, ids, degrees)
    add_duplicates(M2, parent, indices)
    circuit = []
    hierholzer(M2, [0], circuit, 0, len(degrees))
    return(circuit)

sys.modules[__name__] = solve
