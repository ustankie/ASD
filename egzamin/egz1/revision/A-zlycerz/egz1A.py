
#Urszula Stankiewicz, nr albumu: 415668
# algorytm poaługuje się algorytmem Floyda-Warshalla, znajdując najpierw wszystkie najkrótsze ścieżki w grafie G, a później
# w jego przekształceniu G2, w którym koszt każdej krawędzi to podwojony koszt krawędzi w G powiększony o r.
# Następnie w pętli for znajduję najmniejszą wartość tego wyrażenia: 
#(suma dojścia z s do jakiegoś wierzchołka u za pomocą wag z G)+(suma dojścia z u do t za pomocą wag z G2)+V[u]
#zwracam otrzymaną wartość minimalną. Algorytm jest poprawny, ponieważ sprawdza wszystkie możliwości rabowania zamków przez rycerza z zachowaniem
#warunków zadania, a następnie znajduje najmniej kosztowny sposób.
#Złożoność: O(V^3)
from egz1Atesty import runtests
from queue import PriorityQueue


def dijkstra(G,s,tr,r):
  n=len(G)
  d=[float('inf')for _ in range(n)]

  d[s]=0
  Q=PriorityQueue()
  Q.put((d[s],s))

  while not Q.empty():
     c,u=Q.get()
     if c==d[u]:
        for v,k in G[u]:
           if tr:
              k=2*k+r
           if d[v]>d[u]+k:
              d[v]=d[u]+k
              Q.put((d[v],v))
  return d


def gold(G,V,s,t,r):
    n=len(G)
    S=dijkstra(G,s,0,r)
    S1=dijkstra(G,t,1,r)
    min_c=float('inf')

    for u in range(n):
      min_c=min(min_c, S[u]+S1[u]-V[u])
    return min_c



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
G=[[(1, 9), (2, 2)], 
   [(0, 9), (3, 2), (4, 6)], 
   [(0, 2), (3, 7), (5, 1)], 
   [(1, 2), (2, 7), (4, 2), (5, 3)], 
   [(1, 6), (3, 2), (6, 1)], 
   [(2, 1), (3, 3), (6, 8)], [(4, 1), (5, 8)]]

V=[25, 30, 20, 15, 5, 10, 0]
s=1
t=2
r=7
print(gold(G,V,s,t,r))