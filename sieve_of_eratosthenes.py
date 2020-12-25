#エラトステネスの篩
#n以下の素数全列挙

def Eratosthenes(n):
    ret = []
    check = [True] * (n+1)
    for i in range(2, n+1):
        if not check[i]:
            continue
        ret.append(i)
        for j in range(i, n+1, i):
            check[j] = False
    return ret

m = 1000
print(Eratosthenes(m))
