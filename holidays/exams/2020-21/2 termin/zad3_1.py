from zad3testy import runtests
from math import log2
'''
Program posługuje się drzewem przedział przedział, w którym każdy węzeł pamięta, ile lampek w przedziale za który odpowiada 
świeci się na każdy z trzech kolorów. W momencie wciśnięcia przełącznika znajdujemy funkcją range_assign odpowiedni przedział
i zamienamy zielone lampki na czerwone, czerwone na niebieskie i niebieskie na zielone. Po każdym wciśnięciu lampek 
sprawdzamy, ile jest niebieskich w całym drzewie, odwołując się do korzenia
0-zielona lampka
1-czerwona
2-niebieska
'''


def lamps(n, T):
    _n = 1 << (1+int(log2(n-1)))
    if n == 20:
        print(T)

    ST = [[0, 0, 0] for i in range(2*_n)]
    lazy = [0 for i in range(2*_n)]

    for i in range(n):
        ST[i+_n][0] = 1

    for i in range(_n-1, 0, -1):
        ST[i][0] = ST[2*i][0]+ST[2*i+1][0]

    def push(k):
        for i in range(lazy[k]):
            p = ST[2*k][0]
            q = ST[2*k][1]
            r = ST[2*k][2]
            ST[2*k][0] = r
            ST[2*k][1] = p
            ST[2*k][2] = q

            p = ST[2*k+1][0]
            q = ST[2*k+1][1]
            r = ST[2*k+1][2]
            ST[2*k+1][0] = r
            ST[2*k+1][1] = p
            ST[2*k+1][2] = q

        lazy[2*k] = (lazy[k]+lazy[2*k])%3
        lazy[2*k+1] =(lazy[k]+lazy[2*k+1])%3
        lazy[k] = 0

    def range_assign(a, b, k, ka, kb):
        if b < ka or a > kb:
            return
        if a <= ka and b >= kb:
            p = ST[k][0]
            q = ST[k][1]
            r = ST[k][2]
            ST[k][0] = r
            ST[k][1] = p
            ST[k][2] = q
            lazy[k] =(lazy[k]+1)%3
            return
        push(k)
        mid = (ka+kb)//2
        range_assign(a, b, 2*k, ka, mid)
        range_assign(a, b, 2*k+1, mid+1, kb)
        for j in range(3):
            ST[k][j] = (ST[2*k][j]+ST[2*k+1][j])

    t = len(T)
    all_max = 0
    for i in range(t):
        a, b = T[i]
        a = max(a, 0)
        b = min(b, n-1)

        range_assign(a, b, 1, 0, _n-1)

        all_max = max(all_max, ST[1][2])

    return all_max


runtests(lamps)
# T=[(11, 13), (4, 4), (2, 3), (5, 5), (14, 18),
# (9, 13), (7, 10), (9, 11), (7, 10), (9, 11), (14, 14), (5, 9), (16, 19), (6, 10), (16, 19), (14, 18), (16, 18), (4, 7), (8, 12), (2, 3)]
# print(lamps(20,T))
