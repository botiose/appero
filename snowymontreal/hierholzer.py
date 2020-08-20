def hierholzer(M2, path, circuit, cur, n):
    path.append(cur)
    for j in range(n):
        if M2[cur][j] != 0:
            M2[cur][j] -= 1
            hierholzer(M2, path, circuit, j, n)
    circuit.insert(0, path.pop())
