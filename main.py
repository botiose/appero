from snowymontreal.hungarian import match_hungarian
from snowymontreal import solve

# edges = [(0, 2, 20), (0, 1, 10), (1, 4, 10), (1, 3, 50), (2, 3, 20), (2, 4, 33),
#          (3, 4, 5), (3, 5, 12), (4, 0, 12), (4, 5, 1), (5, 2, 22)]

# print(solve(True, 6, edges))


# bipartite_matrix = [[inf, 10, inf, 11, inf, 9],
#                     [10, inf, 13, inf, 8, inf],
#                     [inf, 13, inf, 11, inf, 7],
#                     [11, inf, 11, inf, 4, inf],
#                     [inf, 8, inf, 4, inf, 1],
#                     [9, inf, 7, inf, 1, inf]]

inf = float('inf')

bipartite_matrix = [[inf, 10, inf, 11, inf, 9],
                    [10, inf, 13, inf, 8, inf],
                    [inf, 13, inf, 11, inf, 7],
                    [11, inf, 11, inf, 4, inf],
                    [inf, 8, inf, 4, inf, 2],
                    [9, inf, 7, inf, 2, inf]]

degrees = [1, -1, 1, -1, 1, -1]
ids = [0, 1, 2, 3, 4, 5]

print(match_hungarian(bipartite_matrix, degrees, ids))
