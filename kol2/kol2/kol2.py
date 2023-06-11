#Urszula Stankiewicz, nr albumu: 415668
#Algorytm sortuje krawędzie grafu, a następnie działa na bazie algorytmu Kruskala. 
#Wykonujemy go dopóki nie znajdziemy MST spełniającego warunki zadania, sumując dodawane krawędzie. 
# Jeśli jednak po drodze okaże się, że omijamy jakąś kolejną z posortowanych krawędzi,
#musimy wyzerować stworzoną sumę i zacząć szukać jeszcze raz, tym razem omijając pierwszą dodaną krawędź.
#Robimy to dopóki nie znajdziemy MST rozpinającego wszystkie wierzchołki grafu.
#Na koniec zwracamy wyliczoną sumę lub None, jeśli takie drzewo nie istnieje.
#Złożoność: O(E^2)
from kol2testy import runtests
from queue import PriorityQueue
class Node():
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.par=self

def findset(x):
    if x.par!=x:
        x.par=findset(x.par)
    return x.par
def union(x,y):
    x=findset(x)
    y=findset(y)

    if x.rank>y.rank:
        y.par=x
    else:
        x.par=y
        if x.rank==y.rank:
            y.rank+=1
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    T=[0 for _ in range(n1+n2)]

    while i<n1 and j<n2:
        if T1[i][2]<T2[j][2]:
            T[i+j]=T1[i]
            i+=1
        else:
            T[i+j]=T2[j]
            j+=1
    while i<n1:
        T[i+j]=T1[i]
        i+=1
    while j<n2:
        T[i+j]=T2[j]
        j+=1 
    return T      

def merge_sort(T):
    n=len(T)
    if n==1:
        return T
    q=n//2
    return merge(merge_sort(T[q:]),merge_sort(T[:q]))

def graph_to_edges(G):
    n=len(G)
    edges=[]

    for u in range(n):
        for v,c in G[u]:
            if u<v:
                edges.append((u,v,c))
    edges=merge_sort(edges)
    return edges
            

            
def beautree(G):
    n=len(G)
    E=graph_to_edges(G)
    V=[Node(i)for i in range(n)]
    m=len(E)

    found=False

    sum_c=0
    i=0
    i_plus=0
    while i<m:
        u,v,c=E[i]
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            sum_c+=c
            found=True
        else:
            f1=findset(V[0])
            for v in range(1,n):
                if f1!=findset(V[v]):
                    V=[Node(i)for i in range(n)]
                    sum_c=0
                    i=i_plus
                    i_plus+=1
                    found=False

                    break
        i+=1
    f1=findset(V[0])
    for v in range(1,n):
        if f1!=findset(V[v]):
            return None
    if found:
        return sum_c
    return None


    

G = [ [(1,3), (2,1), (4,2)],
[(0,3), (2,5) ],
[(1,5), (0,1), (3,6)],
[(2,6), (4,4) ],
[(3,4), (0,2) ] ]
Ge2 = [ [(1,2), (2,3)], # 0
        [(0,2), (2,1), (3,5), (4,6)], # 1
        [(0,3), (1,1), (3,9), (4,4)], # 2
        [(1,5), (2,9), (4,10), (5,8)], # 3
        [(2,4), (1,6), (3,10), (5,7)], # 4
        [(3,8), (4,7)] ] # 5
runtests( beautree, all_tests = True )
#print(beautree(Ge2))