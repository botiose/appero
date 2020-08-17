from hungarian import match_hungarian

def incr_insert(l, e):
    for i in range(len(l)):
        if e < l[i]:
            l.insert(i, e)
            return
    l.append(e)

def add_edge(src, dst, dist, M, degrees):
    incr_insert(M[src][dst], dist)
    degrees[src] += 1
    degrees[dst] -= 1

def build_matrix(is_oriented, num_vertices, edge_list):
    M = []
    degrees = [0] * num_vertices
    for i in range(num_vertices):
        l = []
        for k in range(num_vertices):
            l.append([])
        M.append(l)
    for (src, dst, dist) in edge_list:
        inner = []
        M[src][dst].append
        add_edge(src, dst, dist, M, degrees)
        if not is_oriented:
            add_edge(dst, src, dist, M, degrees)
    return (M, degrees)

def floydWarshall(A, n):
    d = []
    p = []
    for i in range(n):
        d.append([])
        p.append([])
        for j in range(n):
            if len(A[i][j]) != 0:
                d[i].append(A[i][j][0])
            else:
                d[i].append(float('inf'))
            p[i].append(i)
    for k in range(n): 
        for i in range(n): 
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]
    return (d, p)

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

def dup_path(M, p, src, dst):
    M[p[src][dst]][dst].append(-1)
    if p[src][dst] == src:
        return
    dup_path(M, p, src, p[src][dst])

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

def hierholzer(M, path, circuit, cur, n):
    path.append(cur)
    for j in range(n):
        if len(M[cur][j]) != 0:
            M[cur][j].pop()
            hierholzer(M, path, circuit, j, n)
    circuit.insert(0, path.pop())
    
def solve(is_oriented, num_vertices, edge_list):
    (M, degrees) = build_matrix(is_oriented, num_vertices, edge_list)
    (shortest, parent) = floydWarshall(M, num_vertices)
    (bipartite, ids) = build_bipartite(shortest, degrees, num_vertices)
    matching = match_hungarian(bipartite, degrees, ids)
    indices = get_oriented_indices(matching, ids, degrees)
    add_duplicates(M, parent, indices)
    circuit = []
    hierholzer(M, [0], circuit, 0, len(degrees))
    print(circuit)

edges = [(0, 2, 20), (0, 1, 10), (1, 4, 10), (1, 3, 50), (2, 3, 20), (2, 4, 33),
         (3, 4, 5), (3, 5, 12), (4, 0, 12), (4, 5, 1), (5, 2, 22)]

solve(True, 6, edges)

# inf = float('inf')
# bipartite = [[inf,7,inf,6,inf,9,inf,3], # inf
#              [7,inf,4,inf,3,inf,5,inf], # 1
#              [inf,4,inf,8,inf,4,inf,8], # 2
#              [6,inf,8,inf,5,inf,9,inf], # 3
#              [inf,3,inf,5,inf,4,inf,7], # 4
#              [9,inf,4,inf,4,inf,2,inf], # 5
#              [inf,5,inf,9,inf,2,inf,4], # 6
#              [3,inf,8,inf,7,inf,4,inf]] # 7
# degrees = [1,-1,1,-1,1,-1,1,-1]
# ids = [0,1,2,3,4,5,6,7]
# matching = match_hungarian(bipartite, degrees, ids)
# print(matching)
