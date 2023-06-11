from collections import deque

def friends(G):
    n=len(G)
    vis=[False for _ in range(n)]
    val=[None for _ in range(n)]
    # par=[None for _ in range(n)]

    Q=deque()
    Q.append(0)
    vis[0]=True
    val[0]=0

    max_friends=0
    fr=[]
    day=0
    while (len(Q)>0):
        u=Q.popleft()
        T=deque()
        count=0
        for v in G[u]:
            if not vis[v]:
                T.append(v)
                vis[v]=True
                val[v]=val[u]+1
                count+=1
                Q.append(v)
        if count>max_friends:
            max_friends=count
            fr=T
            day=val[u]+
    f
    # print(vis)
    # print(val)
    return day,fr

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]
print(friends(G2))
