def hierholzer(deg_matrix, is_oriented, path, circuit, cur, num_vertices):
    """
    Recursive implementation of hierholzer's algorithm.

    Given an adjancency matrix corresponding to a eulerian graph this algorithm
    finds the eulerian cycle of this one.

    Parameters
    deg_matrix (matrix): Ddjacency matrix
    is_oriented (bool): Whether the graph is oriented
    path (vector): Path to current vertex
    circuit (vector): Currently built eulerian path
    cur (int): Current vertex
    num_vertices (int): Number of vertices in the graph
    """
    path.append(cur)
    for j in range(num_vertices):
        if deg_matrix[cur][j] != 0:
            deg_matrix[cur][j] -= 1
            if not is_oriented:
                deg_matrix[j][cur] -= 1
            hierholzer(deg_matrix, is_oriented, path, circuit, j, num_vertices)
    circuit.insert(0, path.pop())
