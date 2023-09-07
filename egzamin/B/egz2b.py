'''
Urszula Stankiewicz, nr albumu: 415668
Algorytm posługuje się tablicą F, gdzie F[i][j] - najmniejsza suma odległości działek od biurowców, kiedy dostępne są biurowce 0...i oraz działki 0...j.
Początkowo wypełniamy zerowy wiersz tablicy, uzupełniając go minimalną odległością zerowego biurowca od wszystkich działek od 0 do j:'
F[0][0]=abs(X[0]-Y[0])
dla j od 1 do m: F[0][j]=min(F[0][j-1],abs(X[0]-Y[j])) - czyli znajdujemy najlepszą działkę dla zerowego biurowca
Następnie w podwójnej pętli for wypełniamy resztę tablicy:
F[i][j]=min(F[i-1][j-1]+abs(X[i]-Y[j]),F[i][j-1],F[i][j])
- dopasowując działkę do i-tego biurowca, bierzemy sumę z biurowca i-1, kiedy korzystaliśmy z działek 0...j-1 i do i-tego biurowca przyporządkowujemy j-tą
działkę, a później sprawdzamy, czy przyporządkowanie przy dostępnych działkach 0..j-1 nie było lepsze.
Złożoność: O(mn)
'''
from egz2btesty import runtests


def parking(X, Y):
    n = len(X)
    m = len(Y)

    inf = float('inf')
    F = [[inf for _ in range(m)]for _ in range(n)]
    F[0][0] = abs(X[0]-Y[0])

    for j in range(1, m):
        F[0][j] = min(F[0][j-1], abs(X[0]-Y[j]))

    for i in range(1, n):
        for j in range(i, m):
            dist = abs(X[i]-Y[j])
            F[i][j] = min(F[i-1][j-1]+dist, F[i][j-1], F[i][j])

    return F[n-1][m-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
