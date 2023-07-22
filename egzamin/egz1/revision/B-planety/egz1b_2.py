from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)
    F = [[float('inf') for _ in range(E+1)]for _ in range(n)]

    F[0][0] = 0

    for i in range(n-1):
        if T[i][0] != i:
            F[T[i][0]][0] = min(F[T[i][0]][0], F[i][0]+T[i][1])

        dist = D[i+1]-D[i]

        F[i+1][0] = min(F[i+1][0], F[i][dist])
        for j in range(1, E+1):
            F[i][j] = min(F[i][j], F[i][j-1]+C[i])
            if j-dist >= 0:
                F[i+1][j-dist] = min(F[i+1][j-dist], F[i][j])
    # print(*F,sep="\n")
    return min(F[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
D = [0, 5, 10, 20]
C = [2, 1, 3, 8]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E = 10
print(planets(D, C, T, E))
