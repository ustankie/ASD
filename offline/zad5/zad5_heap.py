#Urszula Stankiewicz, nr albumu: 415668
#Program przekształca zbiór krawędzi E na listę sąsiedztwa, a następnie wykonuje
#algorytm Djikstry, korzystając z kopca minimum (w kopcu wierzchołki grafu uporządkowane według kosztów dojścia do nich z wierzchołka a).
#Program podejmuje więc następujące kroki, dopóki nie dotrze do wierzchołka b:
#   1) wyjmuje najmniejszy element z kopca- (u)
#   2) przywraca strukturę kopca (heapify w dół od zerowego elementu)
#   3) sprawdza, czy wyjęty wierzchołek u jest osobliwością, jeśli tak, to sprawdzamy, czy koszt dojścia do innych 
#       osobliwości przez u jest mneijszy od dotychczas znalezionego, jeśli tak, to zmieniamy ten koszt na niższy i przywracamy własności kopca
#   4) Podobnie postępujemy dla wszystkich sąsiadów u
#   5) Jeśli pierwszym elementem kopca w pewnym momencie stanie się wierzchołek, do którego dojście kosztuje inf, to znaczy, że 
#       do b nie ma ścieżki -> program zwraca None
# Algorytm znajduje więc dla każdego wierzchołka najmniejszy koszt dojścia do niego z wierzchołka a.
# Algorytm ma złożoność
from zad5testy import runtests
from collections import deque

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

def left(i):return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(T,i,n,d,pos):
    l=left(i)
    r=right(i)
    
    max_ind=i
    if l<n and d[T[max_ind]]>d[T[l]]: max_ind=l
    if r<n and d[T[max_ind]]>d[T[r]]: max_ind=r

    if max_ind!=i:
        pos[T[max_ind]],pos[T[i]]=pos[T[i]],pos[T[max_ind]]

        T[max_ind],T[i]=T[i],T[max_ind]   

        heapify(T,max_ind,n,d,pos)

def heapify2(T,i,n,d,pos):
    while i>=0:
        p=parent(i)
        if p>=0 and d[T[p]]>d[T[i]]: 
            pos[T[p]],pos[T[i]]=pos[T[i]],pos[T[p]]    
            T[p],T[i]=T[i],T[p] 
        i=p


def spacetravel( n, E, S, a, b ):
    T=[0 for _ in range(n)]
    G=adjacent(E,S,T,n)

    pos=[i for i in range(n)]
    vis=[False for _ in range(n)]
    cost=[float('inf') for _ in range(n)]

    # Q=deque()
    # Q.append(a)

    vis[a]=True
    cost[a]=0
    heap=deque()
    for i in range(n):
        heap.append(i)
        
    heap[0],heap[a]=heap[a],heap[0]
    pos[heap[0]],pos[heap[a]]=pos[heap[a]],pos[heap[0]]
    m=n
    u=a  

    while u!=b: 
        # p=Q.popleft()
        # for i in G[p]:
        #     v=i[0]
        #     if not vis2[v]:
        #         vis2[v]=True
        #         Q.append(v)
        # if T[p]:
        #     for v in S:
        #         if not vis2[v]:
        #             vis2[v]=True
        #             Q.append(v)

        heap[0],heap[m-1]=heap[m-1],heap[0]
        pos[heap[0]],pos[heap[m-1]]=pos[heap[m-1]],pos[heap[0]]

        u=heap.pop()
        m-=1

        if cost[u]==float('inf'):
            return None
        
        vis[u]=True
        heapify(heap,0,len(heap),cost,pos)

        if T[u]:
            for v in S:
                if cost[u]<cost[v]:
                    cost[v]=(cost[u])
                    if not vis[v]:
                        heapify2(heap,pos[v],m,cost,pos)

                    
        for i in G[u]: 
            v=i[0]
            c=i[1]
            if cost[v]>(cost[u]+c):
                cost[v]=(cost[u]+c)

                if not vis[v]:
                    heapify2(heap,pos[v],m,cost,pos)


    if u!=b:
        return None
    
    return cost[b]

    




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
# E = [(0,1, 5),
# (1,2,21),
# (1,3, 1),
# (2,4, 7),
# (3,4,13),
# (3,5,16),
# (4,6, 4),
# (5,6, 1)]
# S = [ 0, 2, 3 ]
# a = 1
# b = 5
# n = 7

#print(spacetravel(n,E,S,a,b))