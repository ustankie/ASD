#Urszula Stankiewicz, nr albumu 415668
#Algorytm w pierwszej kolejności znajduje najkrótszą ścieżkę spath z s do t (BFS), 
#a później po kolei usuwa daną krawędź ze ścieżki i ponownie znajduje nową najkrótszą ścieżkę 
#za pomocą BFS. Jeśli ta nowa ścieżka jest dłuższa od pierwotnej, to znaczy, że usunięta krawędź spełnia warunki zadania. W celu przyspieszenia programu 
#zastosowałam następujące modyfikacje:
#   1)BFS każdorazowo jest wykonywany tylko do momentu napotkania wierzchołka t
#   2)Jeśli już w trakcie wykonywania BFS ścieżka okaże się o dłuższa od spath, BFS jest przerywany
#   3)Jeżeli ścieżka jest tej samej długości co spath, to znaczy, że jesteśmy w środku symetrycznego cyklu.
#     Nie musimy więc sprawdzać każdej kolejnej krawędzi tego cyklu, gdyż wiemy, że ścieżka nadal będzie długości spath.
#     Wystarczy więc, że cofniemy się do początku tego cyklu (miejsca gdzie spotka się parent^m krawędzi którą usunęliśmy z parentem^m krawędzi do niej symetrycznej w tym cyklu)
#Algorytm ma złożoność O((V+E)*C), gdzie V-ilość wierzchołków grafu G, E - ilość krawędzi, C - ilość symetrycznych cykli w spath, czyli C<=E/4, zatem O((V+E)*E)

from zad4testy import runtests
from collections import deque

def longer( G, s, t ):
    n=len(G)
    par=[None for _ in range(n)]
    T=[None for _ in range(n)]

    spath=BFS(G,s,t,par,float('inf'),0,0)

    if spath==None: return spath
    
    p=t
    count=1
    while p!=s:
        u=p
        v=par[p]

        T=[None for _ in range(n)]

        d=BFS(G,s,t,T,spath,u,v)
        if d==None or d>spath:
            return u,v
        i=par[v]

        j=T[t]
        for l in range(count):
            j=T[j]

        while (i!=j and i!=s and j!=s):
            i=par[i]
            j=T[j]
        if i==j:
            p=i
        else:
            p=s

        if p==u:
            p=v
        count+=1
        


def BFS(G,s,t,par,val_t,i,j):
    n=len(G)
    vis=[False for _ in range(n)]
    val=[None for _ in range(n)]

    vis[s]=True
    val[s]=0
    Q=deque()
    Q.append(s)
    while len(Q)>0:
        u=Q.popleft()        
        for v in G[u]:
            if not((v==i and u==j)or (v==j and u==i)):
                if not vis[v]:
                    vis[v]=True
                    par[v]=u
                    val[v]=val[u]+1

                    if t==v:return val[v]
                    if val[v]>val_t: return val[v]

                    Q.append(v)


    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
