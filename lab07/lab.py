# 1) Zapimplementować algorytm Dijkstry v
# 2) najkrótsze ścieżki w DAGu -> posortować topologicznie, zaczynamy od pierwszego wierzchołka (na każdej iteracji relaksacja dokładnie raz -> jeden obieg bellmana forda)
#   start może wystąpić gdziekolwiek w topsort -> metoda sorted.index(s) - liniowe przeszukanie O(V) -> całość O(E+V) v
# 3) printowanie parentów v
# 4) najkrótsza ścieżka o najmniejszym możliwym iloczynie wag (wagi rzeczywiste dodatnie) -> wystarczy brać logarytmy w dijkstrze -> lepszy
#    bellman ford bo nie wiadomo czy nie wyjda ujemne
# 5) sieć dróg w mieście - wagi w km - Bob i Alice -> zmieniaja sie za kierownica w kazdym kolejnym miescie, Alice chce jak najmniejsza ilosc km    v
#   q.put(((50km,D,"A"))) -> info kto jechał -> wydluzamy tylko jesli alice ma pokonac kolejny odcinek
#   b) modyfikacja grafu - po dwa wierzcholki -> jesli Alice -> waga w, inaczej waga 0 (muszą być krawędzie skierowane, inaczej problem -> przejazdy 2 pod rząd)
#   Bellman Ford 2 razy (A,B),(A',B') -> jesli dodamy sztuczny wierzcholej, to wystarczy raz -> minusem zlozonosc, trudna implementacja
# 6) Kantor - kursy wymiany walut -> czy da sie taki cykl, zeby uzyskac z jednej sztuki waluty dwie (graf skierowany) -> 
#   Bellman Ford - szukamy cyklu ujemnego (wagi: logarytm z (ile musimy zaplacic w nowej, by uzyskac 1 pierwotnej 0,9A -> 1B, 0.9B->1C, 0.9C->1A -> macierz sąsiedztwa)) v
#     A     B       C
#   A 0    0.9      0
#   B 0     0       0.9
#   C 0.9   0       0
# 7) Implementacja Bellmana Forda w reprezentacji macierzowej v
# 8) Ścieżka w grafie o malejących wagach i jeszcze najoptymalniejsza ze ścieżek (o najmniejszej sumie wag) -> (start,u)

from math import inf 
from queue import PriorityQueue



#1)
def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=(d[u]+c)
        par[v]=u
        return True
    return False

def Dijkstra(G,a):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[a]=0
    Q=PriorityQueue()
    Q.put((d[a],a))

    while not Q.empty():
        w,u=Q.get()
        if w==d[u]:
            #d[u]=w
            for v,c in G[u]:
                if relax(par,d,v,c,u):
                    Q.put((d[v],v))
    return par,d

#2)

def DAG(G,s):
    n=len(G)
    V=topsort(G) #O(E+V)
    d=[inf for _ in range(n)]
    d[s]=0
    par=[None for _ in range(n)]
    #O(E)
    for i in V:
        for x,val in G[i]:
            relax(par,d,x,val,i)
    return d, par

def print_path_r(par,start,u):
    if u!=start:
        print_path_r(par,start,par[u])
    print(u)

def print_path(par,start,u):
    T=[]
    while u!=None:
        T.append(u)
        u=par[u]
    T.reverse()
    for i in range(len(T)):
        print(T[i])
    return T
def topsort(G):
    def DFS(G,u):
        vis[u]=True
        for v,c in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v)
        T.append(u)
        #print(T)
    n=len(G)
    vis=[False for _ in range(n)]
    T=[]
    #vis[0]=True
    for u in range(n):
        if not vis[u]:
            DFS(G,u)
    #print(T)
    T.reverse()
    return T

#7)
def bf(G,s):
    n=len(G)

    par=[None for _ in range(n)]
    d=[inf for _ in range(n)]

    d[a]=0
    for k in range(n):
        b=False
        for i in range(n):
            for j in range(n):
                if G[i][j]:
                    b|=relax(par,d,j,G[i][j],i) #or
        if not b: 
            return d, par
    if b: #jesli nie zrelaskowalismy, to sie nie da -> wykrycie ujemnego cyklu (ostatnia iteracja petli k na to -> normalnie wystarcza n-1 iteracji)
        return d,par,False
    return d,par,True





G2=[[(1,2),(2,5)],[(2,0),(4,3)],[],[],[(3,6),(6,0)],[(4,3),(2,1)],[]]
G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]
print(Dijkstra(G,0))
