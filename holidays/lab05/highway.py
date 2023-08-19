from queue import PriorityQueue
def get_solution(par,t):
    p=t
    R=[]
    while p!=None:
        R.append(p)
        p=par[p]
    
    return R[::-1]

def highway(G,s,t):
    n=len(G)
    Q=PriorityQueue()
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    cost=[float('inf') for _ in range(n)]

    vis[s]=True
    Q.put((0,s))
    cost[s]=0

    while not Q.empty():
        c,u=Q.get()
        for v in range(n):
            if G[u][v]>=0 and (cost[u]+G[u][v]<cost[v]):
                vis[v]=True
                cost[v]=cost[u]+G[u][v]
                par[v]=u
                Q.put((G[u][v],v))
    if vis[t]:
        return get_solution(par,t),cost[t]
    return [],-1

G=[[-1,1,-1,1,0,-1,1],[1,-1,1,-1,-1,-1,-1],[-1,1,-1,-1,-1,-1,-1],[1,-1,-1,-1,-1,0,1],[0,-1,-1,-1,-1,0,-1],[-1,-1,-1,0,0,-1,0],[1,-1,-1,1,-1,0,-1]]
print(highway(G,0,6))