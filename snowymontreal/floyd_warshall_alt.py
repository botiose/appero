def minimum(a, b):
    if a < b:
        return a
    else:
        return b

def adjacency_matrix(verts, edges):
    Adjs = []
    
    for i in range(verts):
        Adjs.append([])
        
        for j in range(verts):
            weight = float('inf')
            
            for edge in edges:
                if i == edge[0] and j == edge[1]:
                    weight = edge[2]
                    
            Adjs[i].append(weight)
                
    return Adjs

def floyd_warshall(verts, edges):
    """
    Alternative version of the Floyd-Warshall algorithm

    This method only uses a single one matrix, which is the adjacency of the graph

    Minimum paths are calculated in-place
    """
    Fwmat = adjacency_matrix(verts, edges)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                Fwmat[i][j] = minimum(Fwmat[i][j], Fwmat[i][k] + Fwmat[k][j])
                    
    return Fwmat

n = 5
edges = [(0,1,1), (1,0,3), (3,2,1), (1,4,4), (4,3,-1), (3,4,2)]
print(floyd_warshall(n, edges))

def minimum(a, b):
    if a < b:
        return a
    else:
        return b

def adjacency_matrix(verts, edges):
    Adjs = []
    
    for i in range(verts):
        Adjs.append([])
        
        for j in range(verts):
            weight = float('inf')
            
            for edge in edges:
                if i == edge[0] and j == edge[1]:
                    weight = edge[2]
                    
            Adjs[i].append(weight)
                
    return Adjs

def floyd_warshall(Adjs, verts):
    Fwmat = Adjs
    
    for k in range(verts):
        for i in range(verts):
            for j in range(verts):
                Fwmat[i][j] = minimum(Fwmat[i][j], Fwmat[i][k] + Fwmat[k][j])
                    
    return (Fwmat, Adjs)
