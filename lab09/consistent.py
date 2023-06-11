from collections import deque
#reprezentacja macierzowa
def BFS(G,F,E,s,t):
    n=len(G)

    min_cap=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            c=G[u][v]-F[u][v]
            
            if c>0 and not vis[v]:
                par[v]=u
                vis[v]=True
                if min_cap[u]>c:
                    E.append((u,v))
                min_cap[v]=min(min_cap[u],c)
                if v==t:
                    return True,par,min_cap[t]
                Q.append(v)
    return False,par,0

def flow(G,s,t):
    n=len(G)
    max_flow=0
    F=[[0 for _ in range(n)] for _ in range(n)]
    E=[]


    augm,par,min_cap=BFS(G,F,E,s,t)
    while augm:
        p=t
        while p!=s:
            F[p][par[p]]=min_cap
            F[par[p]][p]+=min_cap
            p=par[p]
      
        max_flow+=min_cap
        augm,par,min_cap=BFS(G,F,E,s,t)

    R=[]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                R.append(((u,v),F[u][v],G[u][v]))

    

    return max_flow,E


def cons(G):
    n=len(G)
    s=0
    P=[]
    tc=0

    min_c=float('inf')
    for t in range(1,n):
        c,R=flow(G,s,t)
        if min_c>c:
            P=R
            tc=t
        min_c=min(min_c,c)
  
    return min_c,tc,P

G2=[
    [0,1,1,0,0,0],
    [1,0,1,0,1,0],
    [1,1,0,1,1,1],
    [0,0,1,0,1,1],
    [0,1,1,1,0,1],
    [0,0,1,1,1,0],

]

G=[
    [0,1,1,1,0,0,0],
    [1,0,1,1,0,0,0],
    [1,1,0,1,0,0,0],
    [1,1,1,0,1,0,0],
    [0,0,0,1,0,1,1],
    [0,0,0,0,1,0,1],
    [0,0,0,0,1,1,0],

]
print(cons(G))