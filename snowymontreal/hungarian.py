def init_unmatched(degrees, ids, n):
    """Initializes the source and destination vertices from their degrees."""
    src = []
    dst = []
    for i in range(n):
        if degrees[ids[i]] < 0:
            src.append(i)
        elif degrees[ids[i]] > 0:
            dst.append(i)
    return (src, dst)

def init_labels(bipartite_matrix, src, n):
    """Initializes labels for a minimal matching lookup"""
    labels = [0] * n
    for i in src:
        labels[i] = min(bipartite_matrix[i])
    return labels                

def fill_equality(bipartite_matrix, equality_matrix, X, labels, n, matching):
    """Computes the given equality matrix with respect to the given labels"""
    for i in range(n):
        if labels[i] != 0:
            if labels[i] in bipartite_matrix[i] and i in X:
                j = bipartite_matrix[i].index(labels[i])
                equality_matrix[i][j] = True
                equality_matrix[j][i] = True

def find_alternating(equality_matrix, n, s, t, dst, match, cur, p):
    """Returns an alternating path if found. Otherwise it returns None."""
    if match:
        s.append(cur)
    else:
        t.append(cur)
    p[cur] = False
    for i in range(n):
        if equality_matrix[cur][i]:
            if i in dst:
                return [i]
            if p[i]:
                path = find_alternating(equality_matrix, n, s, t, dst,
                                        not match, i, p)
                if not path is None:
                    path.insert(0,i)
                    return path
    return None

def update_labels(bipartite_matrix, labels, s, t, y):
    """Updates assigned labels of the graph to extend visible edges."""
    delta = -float('inf')
    for i in range(len(s)):
        for j in y - set(t):
            cur_delta = labels[s[i]] + labels[j] - bipartite_matrix[s[i]][j]
            if cur_delta > delta:
                delta = cur_delta
    for i in range(len(s)):
        labels[s[i]] -= delta
    for i in range(len(t)):
        labels[t[i]] += delta

def path_to_edges(path):
    """Converts a vertex path to a list of edges represented as tuples."""
    edges = []
    for i in range(len(path)-1):
        edges.append({path[i], path[i+1]})
    return edges

def subs_edges(set1, set2):
    """Removes elements in set2 from set1."""
    res = []
    for edge in set2:
        if not edge in set1:
            res.append(edge)
    return res

def increase_matching(matching, path):
    """
    Increases the current matching.

    Edges in the path that are also in the matching are removed.
    And edges that are not in the matching but are in the path are included.
    """
    aug_path_edges = path_to_edges(path)
    res_set1 = subs_edges(matching, aug_path_edges)
    res_set2 = subs_edges(aug_path_edges, matching)
    return res_set1 + res_set2
    

def match_hungarian(bipartite_matrix, degrees, ids):
    """
    Implementation of the Hungarian matching algorithm.

    This implementation uses the given degrees vector to split the vertices
    in the given bipartite graph. And the ids vector is mainly for outputing
    a matching corresponding to the initial graph to solve. Aside from this 
    this function follows a straightforward implementation of the hungarian 
    matching algorithm.

    Parameters:
    bipartite_matrix (matrix): Matrix of a bipartite graph
    degrees (vector): Degrees of each vertex in the original graph
    ids (vector): Vertex ids of the original graph.
    
    Returns: 
    matching (vector): Result matching
    """
    num_vertices = len(ids)
    (src, dst) = init_unmatched(degrees, ids, num_vertices)
    matching = []
    X = set(src)
    Y = set(dst)
    labels = init_labels(bipartite_matrix, src, num_vertices)
    equality_matrix = [[False for i in range(num_vertices)] for j in
                range(num_vertices)] 
    fill_equality(bipartite_matrix, equality_matrix, X, labels,
                  num_vertices, matching)
    while len(src) != 0:
        start = src[0]
        s = []
        t = []
        p = [True] * num_vertices
        path = find_alternating(equality_matrix, num_vertices, s, t, dst, True,
                                start, p)
        if path is None:
            update_labels(bipartite_matrix, labels, s, t, Y)
            fill_equality(bipartite_matrix, equality_matrix, X, labels,
                           num_vertices, matching)
        else:
            path.insert(0, start)
            matching = increase_matching(matching, path)
            dst.remove(path[-1])
            src.pop(0)
    return matching
