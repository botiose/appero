def floyd_warshall(A, n):
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
