# ABC157-E/ABC185-F
# 1-indexed

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.lst = [0] * n

    def add(self, i, w):
        while i <= self.n:
            self.lst[i-1] += w
            i += i & (-i)
        return
    
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.lst[i-1]
            i -= i & (-i)
        return res
