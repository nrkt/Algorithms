# osa_k法
# ARC116-C

from collections import Counter

class prime_factorization():
    def __init__(self, _max):
        self._max = _max
        self.min_factor = [i for i in range(self._max+1)]
        for i in range(2, int(self._max**(1/2))+1):
            if self.min_factor[i] == i:
                for j in range(i, self._max+1, i):
                    if self.min_factor[j] > i:
                        self.min_factor[j] = i
    
    def create(self, x):
        p = x
        ret = Counter()
        while p >= 2:
            ret[self.min_factor[p]] += 1
            p //= self.min_factor[p]
        return ret
