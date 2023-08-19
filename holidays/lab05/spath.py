from collections import deque
def get_solution(par,k):
    n=len(par)

    p=k
    R=[]

    while p!=None:
        R.append(p)
        p=par[p]

    return R[::-1]

def spath(G,s,k):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                par[v]=u
                if v==k:
                    return get_solution(par,k)
                Q.append(v)
    print(par,vis)
    return []

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]

print(spath(G2,0,5))