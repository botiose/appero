def init_unmatched(degrees, ids, n):
    src = []
    dst = []
    for i in range(n):
        if degrees[ids[i]] < 0:
            src.append(i)
        elif degrees[ids[i]] > 0:
            dst.append(i)
    return (src, dst)

def init_labels(M, src, n):
    labels = [0] * n
    for i in src:
        labels[i] = min(M[i])
    return labels                

def build_equality(A, M, X, labels, n, matching):
    for i in range(n):
        if labels[i] != 0:
            if labels[i] in A[i] and i in X:
                j = A[i].index(labels[i])
                M[i][j] = True
                M[j][i] = True
    return M

def find_alt(A, n, s, t, dst, match, cur, p):
    if match:
        s.append(cur)
    else:
        t.append(cur)
    p[cur] = False
    for i in range(n):
        if A[cur][i]:
            if i in dst:
                return [i]
            if p[i]:
                path = find_alt(A, n, s, t, dst, not match, i, p)
                if not path is None:
                    path.insert(0,i)
                    return path
    return None

def update_labels(A, labels, s, t, y):
    delta = -float('inf')
    for i in range(len(s)):
        for j in y - set(t):
            cur_delta = labels[s[i]] + labels[j] - A[s[i]][j]
            if cur_delta > delta:
                delta = cur_delta
    for i in range(len(s)):
        labels[s[i]] -= delta
    for i in range(len(t)):
        labels[t[i]] += delta

def path_to_edges(path):
    edges = []
    for i in range(len(path)-1):
        edges.append({path[i], path[i+1]})
    return edges

def subs_edges(set1, set2):
    res = []
    for edge in set2:
        if not edge in set1:
            res.append(edge)
    return res

def increase_matching(matching, path):
    aug_path_edges = path_to_edges(path)
    tmp1 = subs_edges(matching, aug_path_edges)
    tmp2 = subs_edges(aug_path_edges, matching)
    return tmp1 + tmp2
    

def match_hungarian(A, degrees, ids):
    n = len(ids)
    (src, dst) = init_unmatched(degrees, ids, n)
    matching = []
    X = set(src)
    Y = set(dst)
    labels = init_labels(A, src, n)
    equality = [[False for i in range(n)] for j in range(n)] 
    equality = build_equality(A, equality, X, labels, n, matching)
    while len(src) != 0:
        start = src[0]
        s = []
        t = []
        p = [True] * n
        path = find_alt(equality, n, s, t, dst, True, start, p)
        if path is None:
            update_labels(A, labels, s, t, Y)
            equality = build_equality(A, equality, X, labels, n, matching)
        else:
            path.insert(0, start)
            matching = increase_matching(matching, path)
            dst.remove(path[-1])
            src.pop(0)
    return matching
