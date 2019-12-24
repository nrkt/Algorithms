#!/usr/bin/env python3
#最長増加部分列問題

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

n = 5
a = [4,2,3,1,5]
dp = [0]*n
ans = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i],dp[j]+1)
    ans = max(ans,dp[i])
print(ans)
#ans = 3
