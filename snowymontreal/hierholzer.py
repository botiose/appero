def hierholzer(deg_matrix, is_oriented, path, circuit, cur, n):
    path.append(cur)
    for j in range(n):
        if deg_matrix[cur][j] != 0:
            deg_matrix[cur][j] -= 1
            if not is_oriented:
                deg_matrix[j][cur] -= 1
            hierholzer(deg_matrix, is_oriented, path, circuit, j, n)
    circuit.insert(0, path.pop())
