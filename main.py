from snowymontreal.hungarian import match_hungarian
from snowymontreal.solver import solve

edges = [(0, 2, 20), (0, 1, 10), (1, 4, 10), (1, 3, 50), (2, 3, 20), (2, 4, 33),
         (3, 4, 5), (3, 5, 12), (4, 0, 12), (4, 5, 1), (5, 2, 22)]

print(solve(True, 6, edges))
