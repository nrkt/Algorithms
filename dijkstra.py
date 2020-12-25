def dijkstra(s,graph):
    d = [inf]*n
    d[s] = 0
    h = [(0,s)]
    while h:
        c,v = heappop(h)
        if d[v] < c:
            continue
        for t,cost in graph[v]:
            if d[v] + cost < d[t]:
                d[t] = d[v] + cost
                heappush(h,(d[t],t))
    return d
