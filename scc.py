def scc(n, edges, rev_edges):
    order = []
    used = [False] * n
    group = [None] * n
    
    def dfs(v):
        used[v] = True
        for u in edges[v]:
            if not used[u]:
                dfs(u)
        order.append(v)

    def rdfs(v, col):
        group[v] = col
        used[v] = True
        for u in rev_edges[v]:
            if not used[u]:
                rdfs(u, col)
    
    for v in range(n):
        if not used[v]:
            dfs(v)
    
    used = [False] * n
    label = 0
    for v in order[::-1]:
        if not used[v]:
            rdfs(v, label)
            label += 1
    return label, group