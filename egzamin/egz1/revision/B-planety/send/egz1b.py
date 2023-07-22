# Urszula Stankiewicz, nr albumu: 415668
# Algorytm dynamiczny, wyznaczamy wartości tablicy F[i][j] - minimalna cena dotarcia od 0 do i mając jeszcze j paliwa w baku
# F[0][0]=0
# Dla danego pola i rozpatruję wszystkie możliwości dotarcia z i  mając j paliwa do pól k>i (posiadając na polu k jeszcze l paliwa).
# i jeśli koszt dotarcia tam jest mniejszy, to aktualizuje wartość F[k][l]
# Jeśli T[i][0]!=i oraz nie mamy paliwa w baku, to sprawdzamy, czy zmniejszy to koszt dotarcia do pola T[i][0]
# Złożoność: O(n^2*E^2)
from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)

    F = [[float('inf') for _ in range(E+1)]for _ in range(n)]

    F[0][0] = 0

    for i in range(n):
        if T[i][0] > i:
            F[T[i][0]][0] = min(F[T[i][0]][0], F[i][0]+T[i][1])
        for j in range(E+1):
            for k in range(i+1, n):
                dist = D[k]-D[i]
                # p - ile paliwa zostanie mi w baku, jeśli skorzystam tylko z tego co mam
                p = max(0, j-dist)

                for l in range(p, E+1):
                    if dist-j >= 0:
                        to_tank = dist-j+l
                    else:
                        to_tank = (l-(j-dist))
                    if to_tank >= 0:
                        F[k][l] = min(F[k][l], F[i][j]+to_tank*C[i])

    print(*F,sep="\n")
    return min(F[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=False)


D=  [0, 5, 10, 20]
C=  [2, 1, 3, 8]
T= [(2, 3), (3, 7), (2, 10), (3, 10)]
E= 10
print(planets(D,C,T,E))