
def Hierholzer(adj_list):
    l = len(adj_list)
    if l == 0:
        return
    num_edge_vrtx = []
    for i in range(l):
        num_edge_vrtx.append(len(adj_list[i]))
    path = []
    res = []
    curr_vrtx = 0
    path.append(curr_vrtx)
    while path:
        if not num_edge_vrtx[curr_vrtx]:
            res.append(curr_vrtx)
            curr_vrtx = path.pop()
        else:
            path.append(curr_vrtx)
            num_edge_vrtx[curr_vrtx] -= 1
            curr_vrtx = adj_list[curr_vrtx].pop()
    return res    
   