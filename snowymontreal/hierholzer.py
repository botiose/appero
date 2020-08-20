def hierholzer(deg_matrix, path, circuit, cur, n):
    path.append(cur)
    for j in range(n):
        if deg_matrix[cur][j] != 0:
            deg_matrix[cur][j] -= 1
            hierholzer(deg_matrix, path, circuit, j, n)
    circuit.insert(0, path.pop())
