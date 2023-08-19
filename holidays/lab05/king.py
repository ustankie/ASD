from collections import deque
def king(G,s,t):
    n=len(G)
    vis=[[False for _ in range(n)]for _ in range(n)]
    par=[[None for _ in range(n)]for _ in range(n)]
    cost=[[0 for _ in range(n)]for _ in range(n)]
    step=[[0,1],[-1,0],[1,0],[0,-1]]

    Q=deque()
    Q.append(s)
    vis[s[0]][s[1]]=True

    while len(Q)>0:
        u1,u2=Q.popleft()
        u=[u1,u2]
        if G[u1][u2]>0:
            G[u1][u2]-=1
            Q.append([u1,u2])
        else:
            for a,b in step:
                v1=u1+a
                v2=u2+b
                if 0<=v1<n and 0<=v2<n:
                    if not vis[v1][v2]:
                            vis[v1][v2]=True
                            par[v1][v2]=[u1,u2]
                            cost[v1][v2]=cost[u1][u2]+G[v1][v2]
                            G[v1][v2]-=1
                            
                            Q.append([v1,v2])
                            print(u,v1,v2,cost[v1][v2])
        if u==t:
            break


    
    R=[]
    print(vis)
    p=t

    while p!=None:
         R.append(p)
         p=par[p[0]][p[1]]
    
    return R[::-1],cost[t[0]][t[1]]


G=[[2,1,3],[2,15,1],[1,0,1]]
print(king(G,[0,0],[2,2]))