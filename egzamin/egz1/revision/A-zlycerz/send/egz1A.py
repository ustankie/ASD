# Urszula Stankiewicz, nr albumu: 415668
# algorytm poaługuje się algorytmem Floyda-Warshalla, znajdując najpierw wszystkie najkrótsze ścieżki w grafie G, a później
# w jego przekształceniu G2, w którym koszt każdej krawędzi to podwojony koszt krawędzi w G powiększony o r.
# Następnie w pętli for znajduję najmniejszą wartość tego wyrażenia:
# (suma dojścia z s do jakiegoś wierzchołka u za pomocą wag z G)+(suma dojścia z u do t za pomocą wag z G2)+V[u]
# zwracam otrzymaną wartość minimalną. Algorytm jest poprawny, ponieważ sprawdza wszystkie możliwości rabowania zamków przez rycerza z zachowaniem
# warunków zadania, a następnie znajduje najmniej kosztowny sposób.
# Złożoność: O(V^3)
from egz1Atesty import runtests


def floyd(G, r, transformed):
    n = len(G)
    S = [[float('inf')for _ in range(n)]for _ in range(n)]

    for u in range(n):
        for v, c in G[u]:
            if transformed:
                S[u][v] = c*2+r
            else:
                S[u][v] = c
    for u in range(n):
        S[u][u] = 0

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t]+S[t][v]:
                    S[u][v] = S[u][t]+S[t][v]
    return S


def gold(G, V, s, t, r):
    n = len(G)
    # print(G)
    S = floyd(G, r, 0)
    S1 = floyd(G, r, 1)
    min_c = float('inf')

    for u in range(n):
        min_c = min(min_c, S[s][u]+S1[u][t]-V[u])
    return min_c


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)

