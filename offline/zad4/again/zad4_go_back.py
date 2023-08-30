from zad4testy import runtests
from collections import deque
def BFS(G,s,t,i,j,spath):
    n=len(G)
    inf=float('inf')
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    d[s]=0

    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if d[v]==inf and (u,v)!=(i,j) and (v,u)!=(i,j):
                d[v]=d[u]+1
                par[v]=u
                if v==t:
                    return d[t],par
                if d[v]>spath:
                    return d[v],par
                Q.append(v)
    return None,par
        
def longer( G, s, t ):
    n=len(G)
    spath,par=BFS(G,s,t,0,0,float('inf'))

    if spath==None:
        return None
    
    p=t
    i=0
    while p!=s:
        u=p
        v=par[p]

        spath2,par2=BFS(G,s,t,u,v,spath)
        if spath2==None or spath2>spath:
            return (v,u)
        
        a=t
        for j in range(i):
            a=par2[a]
        p=par[p]
        b=par2[a]

        while p!=s and b!=p:
            p=par[p]
            b=par2[b]
            
    return None




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
G=[[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
G2=[[1, 2], [0, 2], [0, 1]]
print(longer(G2,0,2))