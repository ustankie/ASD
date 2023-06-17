from zad8testy import runtests
from collections import deque


def sum_stains(T):
    n = len(T)
    m = len(T[0])
    S = [0 for _ in range(m)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    Q = deque()
    for i in range(m):
        if T[0][i]:
            Q.append((0, i))
            S[i] += T[0][i]
            T[0][i] = 0
            while len(Q) > 0:
                u, v = Q.popleft()
                for um, vm in move:
                    a = u+um
                    b = v+vm
                    if a >= 0 and a < n and b >= 0 and b < m and T[a][b]:
                        S[i] += T[a][b]
                        T[a][b] = 0
                        Q.append((a, b))
    return S


def frog(A):
    n = len(A)
    F = [[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        F[n-1][i] = 0

    for i in range(n-2, -1, -1):
        for k in range(n):
            m = min(n, i+k+A[i]+1)
            for j in range(i+1, m):
                if k-(j-i)+A[i] >= 0 and k-(j-i)+A[i] < (n) and F[j][k-(j-i)+A[i]] < float('inf'):
                    F[i][k] = min(F[i][k], F[j][k-(j-i)+A[i]]+1)
    return F[0][0]


def frog2(A):
    n = len(A)
    F = [[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        F[0][i] = 0
    m = min(A[0]+1, n)
    for i in range(1, m):
        F[i][A[0]-i] = 1
    for i in range(1, n):
        for j in range(n):
            if F[i][j] < float('inf'):
                m = min(A[i]+j, n)
                for k in range(1, m+1):
                    next = m-k
                    if next >= 0 and k+i < n:
                        F[k+i][next] = min(F[k+i][next], F[i][j]+1)
    return min(F[n-1])


def plan(T):
    S = sum_stains(T)
    return frog2(S)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)


A = [2, 2, 1, 0, 0, 0]
A = [2, 3, 1, 1, 2, 0]
print(frog(A))
