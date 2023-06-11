from collections import deque
from queue import PriorityQueue
def king(G,s,t):
    n=len(G)
    vis=[False for _ in range(n*n)]
    par=[None for _ in range(n*n)]
    neighbour=[(-1,-1),(0,-1),(1,-1),(-1,0),(-1,1),(-1,1),(0,1),(1,1)]
    d=[None for _ in range(n*n)]
    m=len(neighbour)

    Q=PriorityQueue()
    Q.put((0,s))
    vis[s[0]*n+s[1]]=True
    d[s[0]*n+s[1]]=0

    while not Q.empty():
        c,u=Q.get()
        print(u)
        ind_u=u[0]*n+u[1]

        for v in range(m):
            i=u[0]+neighbour[v][0]
            j=u[1]+neighbour[v][1]
            ind_v=i*n+j
            if i<n and j<n and i>=0 and j>=0 and not vis[i*n+j]:
                vis[ind_v]=True
                par[ind_v]=ind_u
                d[ind_v]=d[ind_u]+G[i][j]
                if  [i,j]==t:
                    print(i,j)
                    T=[]
                    p=t[0]*n+t[1]
                    cost=0
                    while p!=None:
                        T.append((p//n,p%n))
                        cost+=G[p//n][p%n]
                        p=par[p]
                    return T[::-1],cost
                Q.put((G[i][j],(i,j)))

G=[[2,1,3],[2,15,1],[3,0,1]]
print(king(G,[0,0],[2,2]))
            
