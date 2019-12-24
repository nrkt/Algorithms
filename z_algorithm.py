#!/usr/bin/env python3
#Z algorithm(ABC141-E)

def Z_algorithm(s):
    n = len(s)
    Z = [0]*n
    Z[0] = n
    i,j = 1,0
    while i < n:
        while i+j < n and s[j] == s[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
 
        #再利用部分
        while i+k < n and k+Z[k] < j:
            Z[i+k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z