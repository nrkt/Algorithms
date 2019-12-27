"""
[トポロジカルソート]
⇒入次数0の頂点からスタートし、その番号を1とする.1から出ている有向辺をすべて削除.
  入次数0になった頂点の番号を2とし,2から出ている有向辺をすべて削除
  入次数0になった頂点の番号を3とし,...を繰り返す.
"""
n,m = map(int,input().split())

edges = [[] for _ in range(n)]
cnt = [0]*n
for _ in range(n-1+m):
    a,b = map(int,input().split())
    edges[a-1].append(b-1)
    cnt[b-1] += 1


lst = [None]*n
que = deque()
num = 1
for i in range(n):
    if cnt[i] == 0:
        que.append(i)
        lst[i] = num
        num += 1
        while que:
            v = que.popleft()
            for i in edges[v]:
                cnt[i] -= 1
                if cnt[i] == 0:
                    que.append(i)
                    lst[i] = num
                    num += 1
        break
#print(*lst)