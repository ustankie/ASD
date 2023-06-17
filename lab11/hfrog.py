def frog(A):
    n = len(A)
    max_snack = max(A)
    F = [[float('inf') for _ in range(max_snack*n)]for _ in range(n)]
    for i in range(n):
        F[n-1][i] = 0

    for i in range(n-2, -1, -1):
        for k in range(max_snack*n):
            m = min(n, i+k+A[i]+1)
            for j in range(i+1, m):
                if k-(j-i)+A[i] >= 0 and k-(j-i)+A[i] < (max_snack*n) and F[j][k-(j-i)+A[i]] < float('inf'):
                    F[i][k] = min(F[i][k], F[j][k-(j-i)+A[i]]+1)
    return (F[0][0])


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


A = [2, 2, 1, 0, 0, 0]
A = [2, 3, 1, 1, 2, 0]
A = [1, 2, 1, 1, 0, 0, 0, 0]
# A=[1,0]
print(frog2(A))
