from zad4testy import runtests
from collections import deque
def BFS(G,s,t):
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
            if d[v]==inf:
                d[v]=d[u]+1
                par[v]=u
                if v==t:
                    return d
                Q.append(v)
    return d
        
def longer( G, s, t ):
    n=len(G)
    d=BFS(G,s,t)

    num_wave=0
    wave=[0 for _ in range(d[t]+1)]
    vis=[False for _ in range(n)]

    Q=deque()
    Q.append(t)
    i=1
    wave[0]=1
    last=t
    curr=None

    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if d[u]==d[v]+1 and not vis[v]:
                vis[v]=True
                wave[i]+=1
                curr=v
                Q.append(v)

        num_wave+=1
        
        if num_wave==wave[i-1]:
            num_wave=0
            if i>0 and wave[i]==1==wave[i-1]:
                return (last,curr)
            i+=1
            if i>d[t]:
                return None
            last=curr
    return None
            
    






                





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
G=[[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
G2=[[1, 2], [0, 2], [0, 1]]
print(longer(G2,0,2))