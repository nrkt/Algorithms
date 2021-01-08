# ABC187-E
euler_tour = []
stack = [0, 0]
check = [False] * n
while stack:
    v = stack.pop()
    euler_tour.append(v)
    check[v] = True
    for u in edges[v][::-1]:
        if check[u]:
            continue
        stack.append(u)
        stack.append(u)