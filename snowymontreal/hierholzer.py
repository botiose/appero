def hierholzer(M, path, circuit, cur, n):
    path.append(cur)
    for j in range(n):
        if len(M[cur][j]) != 0:
            M[cur][j].pop()
            hierholzer(M, path, circuit, j, n)
    circuit.insert(0, path.pop())
