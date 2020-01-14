#!/usr/bin/env python3
#AGC38 B
#スライド最小値

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n,k = LI()
p = LI()
ans = 0
que = deque()
que.append(0)
minlst = []
for i in range(1,n):
    if p[que[-1]] < p[i]:
        que.append(i)
    else:
        while que:
            if p[que[-1]] < p[i]:
                que.append(i)
                break
            else:
                que.pop()
        else:
            que.append(i)
    if i >= k:
        minlst.append(p[que[0]])
        if que[0] == i - k:
            que.popleft()
minlst.append(p[que[0]])
que = deque()
que.append(0)
maxlst = []
for i in range(1,n):
    if p[que[-1]] > p[i]:
        que.append(i)
    else:
        while que:
            if p[que[-1]] > p[i]:
                que.append(i)
                break
            else:
                que.pop()
        else:
            que.append(i)
    if i >= k-1:
        maxlst.append(p[que[0]])
        if que[0] == i - k:
            que.popleft()

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]
def union(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

lst = []
cnt = 1
tmp = p[0]
for i in range(1,n):
    if tmp < p[i]:
        cnt += 1
    else:
        if cnt >= k:
            lst.append(i-k)
        cnt = 1
    tmp = p[i]
if cnt >= k:
    lst.append(i-cnt+1)
par = [i for i in range(n)]
rank = [0]*n
if len(lst) > 1:
    for i in lst:
        for j in lst[::-1]:
            union(i,j)
for i in range(n-k):
    if p[i] == minlst[i] and p[i+k] == maxlst[i+1]:
        union(i,i+1)
s = set()
for i in range(n-k+1):
    s.add(root(i))
print(len(s))

