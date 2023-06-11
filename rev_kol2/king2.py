from collections import deque
from queue import PriorityQueue
def relax(d,par,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False
def king(G,s,t):
    n=len(G)
    par=[None for _ in range(n*n)]
    vis=[False for _ in range(n*n)]
    neighbour=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    d=[float('inf') for _ in range(n*n)]
    m=len(neighbour)

    Q=PriorityQueue()
    Q.put((G[s[0]][s[1]],s))
    d[s[0]*n+s[1]]=G[s[0]][s[1]]
    vis[s[0]*n+s[1]]=True

    while not Q.empty():
        c,u=Q.get()
        
        ind_u=u[0]*n+u[1]
        print(c,u,d[ind_u])
        vis[ind_u]=True
        if c==d[ind_u]:
            print("a    ")
            for v in range(m):
                i=u[0]+neighbour[v][0]
                j=u[1]+neighbour[v][1]
                ind_v=i*n+j
                print(i,j)
                if i<n and j<n and i>=0 and j>=0:
                    print(i,j,d[ind_v])
                    if relax(d,par,ind_u,ind_v,G[i][j]):#and not vis[ind_v]:
                        
                        Q.put((d[ind_v],(i,j)))
    T=[]
    print(d)
    cost=0
    p=t[0]*n+t[1]
    while p!=None:
        T.append((p//n,p%n))
        cost+=G[p//n][p%n]
        p=par[p]
    T=T[::-1]
    return T,cost

G=[


[5, 1, 5, 5, 1, 3, 4, 5, 1, 4, 5, 3],
[4, 4, 4, 2, 1, 1, 4, 1, 5, 3, 3, 4],
[5, 5, 3, 5, 1, 5, 5, 2, 5, 4, 1, 1],
[1, 5, 3, 1, 5, 2, 1, 3, 3, 5, 2, 1],
[1, 2, 3, 2, 5, 3, 5, 1, 3, 3, 2, 4],
[2, 2, 3, 5, 1, 4, 4, 1, 5, 1, 3, 2],
[1, 4, 2, 3, 3, 1, 1, 2, 1, 5, 2, 5],
[2, 5, 3, 4, 1, 5, 2, 5, 3, 2, 2, 1],
[2, 4, 5, 5, 5, 1, 3, 3, 1, 5, 1, 2],
[2, 4, 4, 3, 1, 2, 1, 3, 1, 2, 2, 4],
[5, 4, 3, 5, 3, 5, 1, 5, 2, 3, 1, 3],
[5, 5, 1, 3, 5, 4, 2, 3, 5, 3, 2, 3],
]
print(king(G,[0,0],[len(G)-1,len(G)-1]))
            
