# ax + by = c整数解をもつ <=> cはgcd(a,b)の倍数
# 特に，ax + by = 1が整数解をもつ <=> aとbは互いに素

# ABC186-E
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0

import math
t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    g = math.gcd(n, k)
    if s % g != 0:
        print(-1)
    else:
        n //= g
        s //= g
        k //= g
        _, x, y = extgcd(n, -k)
        print('aa')