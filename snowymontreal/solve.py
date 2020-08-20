from snowymontreal.hungarian import match_hungarian
from snowymontreal.floyd_warshall import floyd_warshall
from snowymontreal.hierholzer import hierholzer

import sys

def incr_insert(adj_vect, elt):
    for i in range(len(adj_vect)):
        if e < adj_vect[i]:
            adj_vect.insert(i, elt)
            return
    adj_vect.append(elt)

def add_edge(src, dst, dist, adj_matrix, deg_matrix, degrees):
    incr_insert(adj_matrix[src][dst], dist)
    degrees[src] += 1
    degrees[dst] -= 1
    deg_matrix[src][dst] += 1

def build_matrix(is_oriented, num_vertices, edge_list):
    adj_matrix = []
    deg_matrix = []
    degrees = [0] * num_vertices
    for i in range(num_vertices):
        adj_row = []
        deg_row = [0] * num_vertices
        for k in range(num_vertices):
            adj_row.append([])
        adj_matrix.append(adj_row)
        deg_matrix.append(deg_row)
    for (src, dst, dist) in edge_list:
        inner = []
        add_edge(src, dst, dist, adj_matrix, deg_matrix, degrees)
        if not is_oriented:
            add_edge(dst, src, dist, adj_matrix, deg_matrix, degrees)
    return (adj_matrix, deg_matrix, degrees)

def build_bipartite(adj, degrees, n):
    num_inbalanced = 0
    for degree in degrees:
        if degree != 0:
            num_inbalanced += abs(degree)
    bipartite_matrix = [[float('inf') for i in range(num_inbalanced)] for j in
         range(num_inbalanced)] 
    ids = [-1] * num_inbalanced
    i = 0
    for k in range(n):
        if degrees[k] != 0:
            ids[i] = k
            j = 0
            for l in range(n):
                if degrees[l] != 0:
                    if degrees[k] < 0 and degrees[l] > 0:
                        bipartite_matrix[i][j] = adj[k][l]
                        bipartite_matrix[j][i] = adj[k][l]
                    j += 1
            for h in range(abs(degrees[k])-1):
                for g in range(num_inbalanced):
                    bipartite_matrix[num_inbalanced-i-1][g] = M[i][g]
                    bipartite_matrix[g][num_inbalanced-i-1] = M[i][g]
                ids[num_inbalanced-i-1] = k
            i += 1
    return (bipartite_matrix, ids)

def dup_path(deg_matrix, parent_matrix, src, dst):
    deg_matrix[parent_matrix[src][dst]][dst] += 1
    if parent_matrix[src][dst] == src:
        return
    dup_path(deg_matrix, parent_matrix, src, parent_matrix[src][dst])

def get_oriented_indices(matching, ids, degrees):
    indices = []
    for edge in matching:
        start = -1;
        end = -1;
        for elt in edge:
            if degrees[ids[elt]] > 0:
                end = ids[elt]
            else:
                start = ids[elt]
        indices.append((start, end))
    return indices

def add_duplicates(deg_matrix, parent, indices):
    for (start, end) in indices:
        dup_path(deg_matrix, parent, start, end)
    
def solve(is_oriented, num_vertices, edge_list):
    (adj_matrix, deg_matrix, degrees) = build_matrix(is_oriented, num_vertices,
                                                     edge_list)
    (shortest_matrix, parent_matrix) = floyd_warshall(adj_matrix, num_vertices)
    (bipartite_matrix, ids) = build_bipartite(shortest_matrix, degrees,
                                              num_vertices)
    matching = match_hungarian(bipartite_matrix, degrees, ids)
    indices = get_oriented_indices(matching, ids, degrees)
    add_duplicates(deg_matrix, parent_matrix, indices)
    circuit = []
    hierholzer(deg_matrix, [0], circuit, 0, len(degrees))
    return(circuit)

sys.modules[__name__] = solve
