def floyd_warshall(adj_matrix, num_vertices):
    shortest_matrix = []
    parent_matrix = []
    for i in range(num_vertices):
        shortest_matrix.append([])
        parent_matrix.append([])
        for j in range(num_vertices):
            if len(adj_matrix[i][j]) != 0:
                shortest_matrix[i].append(adj_matrix[i][j][0])
            else:
                shortest_matrix[i].append(float('inf'))
            parent_matrix[i].append(i)
    for k in range(num_vertices): 
        for i in range(num_vertices): 
            for j in range(num_vertices):
                if shortest_matrix[i][k] + shortest_matrix[k][j] < \
                   shortest_matrix[i][j]:
                    shortest_matrix[i][j] = shortest_matrix[i][k] + \
                        shortest_matrix[k][j]
                    parent_matrix[i][j] = parent_matrix[k][j]
    return (shortest_matrix, parent_matrix)
