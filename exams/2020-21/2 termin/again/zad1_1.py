from zad1_testy import runtests


def DFS(G, x, m):
    n = len(G)
    vis = [False for _ in range(n)]
    P = [False for _ in range(m)]

    def recur(u):
        for v, i in G[u]:
            P[i] = True

            if not vis[v]:
                vis[v] = True
                recur(v)

    vis[x] = True
    recur(x)

    return P


def binsearch(A, x):
    n = len(A)
    i = 0
    j = n-1
    while i < j:
        q = (i+j)//2
        if A[q] == x:
            return q
        if A[q] > x:
            j = q-1
        else:
            i = q+1
        #print(i,j,x)
    return i


def intuse(I, x, y):
    # if x == 1 and y == 10:
    #     print(I)
    n = len(I)
    V1 = [x,y]
    V = []
    for i in range(n):
        V1.append(I[i][0])
        V1.append(I[i][1])
    V1.sort()

    V.append(V1[0])

    for i in range(1, 2*n+2):
        #print(V1[i])
        if V1[i] != V1[i-1]:
            V.append(V1[i])
    m = len(V)
    
    G = [[]for _ in range(m)]
    G2 = [[]for _ in range(m)]
    S = [False for _ in range(n)]

    for i in range(n):
        a = binsearch(V, I[i][0])
        b = binsearch(V, I[i][1])
        #print(a,b)
        G[a].append((b, i))
        G2[b].append((a, i))
    # print(*G,sep="\n")
    # print(*G2,sep="\n")
    a=binsearch(V,x)
    b=binsearch(V,y)
    vis_x = DFS(G, a, n)
    vis_y = DFS(G2, b, n)
    R = []
    # print(vis_x)
    # print(vis_y)

    for i in range(n):
        if vis_x[i] and vis_y[i]:
            R.append(i)
    return R


runtests(intuse)

I = [(4, 4), (4, 10), (2, 15), (6, 16), (3, 8), (2, 14),
     (6, 21), (3, 1), (0, 5), (7, 15), (3, 19), (2, 17),
     (4, 24), (7, 10), (5, 8), (4, 21), (6, 22), (9, 27),
     (2, 18), (1, 6), (5, 14), (5, 13), (0, 18), (10, 16),
     (9, 24), (11, 24), (5, 7), (6, 14), (1, 7), (3, 19),
     (11, 18), (6, 9), (11, 19), (9, 27), (7, 11),
     (13, 17), (10, 24), (8, 16), (11, 25), (11, 25),
     (11, 26), (12, 30), (4, 9), (5, 11), (10, 20),
     (6, 12), (14, 33), (13, 18), (8, 25), (15, 26)]
I = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
I = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7),
     (5, 8), (6, 9), (7, 10), (8, 11), (9, 12)]
x = 0
y = 13
print(intuse(I, x, y))
