#Urszula Stankiewicz, nr albumu: 415668
#Program przekształca zbiór krawędzi E na listę sąsiedztwa, a następnie wykonuje
#algorytm Djikstry, korzystając z kolejki priorytetowej PriorityQueue
#Program podejmuje więc następujące kroki, dopóki nie dotrze do wierzchołka b:
#   1) wyjmuje wierzchołek o najmniejszym koszcie dojścia, który jeszcze nie był odwiedzony z kolejki
#   2) sprawdza, czy wyjęty wierzchołek u jest osobliwością, jeśli tak, to sprawdzamy, czy koszt dojścia do innych 
#       osobliwości przez u jest mneijszy od dotychczas znalezionego, jeśli tak, to zmieniamy ten koszt na niższy i wrzucamy wierzchołek jeszcze raz do kolejki
#   3) Podobnie postępujemy dla wszystkich sąsiadów u
#   4) Jeśli pierwszym nieodwiedzonym jeszcze elementem kopca w pewnym momencie stanie się wierzchołek, do którego dojście kosztuje inf, to znaczy, że 
#       do b nie ma ścieżki -> program zwraca None
# Algorytm znajduje więc dla każdego wierzchołka najmniejszy koszt dojścia do niego z wierzchołka a.
# Algorytm ma złożoność O(mlogn), gdzie m - liczba krawędzi, n - liczba planet

from zad5testy import runtests
from queue import PriorityQueue

def adjacent(E,S,T,n):
    G=[[]for _ in range(n)] 
    k=len(S)
    for i in range(k):
        T[S[i]]=1

    m=len(E)
    for i in range(m):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G

def spacetravel( n, E, S, a, b ):
    T=[0 for _ in range(n)]
    G=adjacent(E,S,T,n)

    vis=[False for _ in range(n)]
    cost=[float('inf') for _ in range(n)]


    vis[a]=True
    cost[a]=0
    heap=PriorityQueue()
    for i in range(n):
        heap.put((cost[i],i))
        
    u=a
    print(heap.queue)

    while u!=b: 
        if cost[u]==float('inf'):
            return None
        
        vis[u]=True

        if T[u]:
            for v in S:
                if cost[u]<cost[v]:
                    cost[v]=(cost[u])
                    heap.put((cost[v],v))

                    
        for i in G[u]: 
            v=i[0]
            c=i[1]
            if cost[v]>(cost[u]+c):
                cost[v]=(cost[u]+c)
                heap.put((cost[v],v))

        u=heap.get()
        u=u[1]
        while vis[u]==1:
            u=heap.get()
            u=u[1]

    if u!=b:
        return None
    
    return cost[b]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
