from collections import deque
def transform(G):
    n=len(G)
    T=[deque() for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            if ((i-1)*(n)+j)>=0:
                T[i*n+j].append((i-1)*(n)+j)
            if (i*n+j-1)>=(n*i):
                T[i*n+j].append(i*n+j-1)
            if (i*n+j+1)<(n*(i+1)):
                T[i*n+j].append(i*n+j+1)
            if ((i+1)*(n)+j)<(n*n):
                T[i*n+j].append((i+1)*(n)+j)
    return T

def king(G,s,k):
    n=len(G)
    s1=s[0]*n+s[1]
    k1=k[0]*n+k[1]
    
    T=transform(G)
    vis=[False for _ in range(n*n)]
    par=[None for _ in range(n*n)]
    cost=[0 for _ in range(n*n)]

    Q=deque()
    Q.append(s1)

    while (len(Q)>0):
        u=Q.popleft()
        if G[u//n][u%n]>0:
                G[u//n][u%n]-=1
                Q.append(u)
        else:
            for v in T[u]:
                if not vis[v]:
                    vis[v]=True
                    par[v]=u
                    cost[v]=cost[u]+G[v//n][v%n]
                    G[v//n][v%n]-=1
                    Q.append(v)
                    print(cost[v])

        if(u==k1):
            break

    R=deque()
    p=k1

    while par[p]!=s1:
        R.append([p//n,p%n])
        p=par[p]
    R.append([p//n,p%n])
    R.append(s)

    c=cost[k1]
    return reverse(R),c

def reverse(T):
    n=len(T)
    for i in range(n//2):
        T[i],T[n-i-1]=T[n-1-i],T[i]
    return T

                







# def king(G,s):
#     n=len(G)
#     visited=[[-1 for v in range(n)] for _ in range
#     parent=[None for v in range(n)]
#     D=[0 for _ in range(n)]
#     Q=deque()
#     Q.append((s,0))
#     while (len(Q))>0:
#         v,c=Q.popleft()
#         for x in range(n):
#             if visited[x]==(-1):
#                 if c==1:
#                     visited[x]=1
#                     parent[x]=v
#                     Q.append(x)
#                 else:
#                     Q.append((x,c-1))
#                     D[x]+=1
 
#     return min(D)
G=[[2,1,3],[2,15,1],[3,0,1]]
print(king(G,[0,0],[2,2]))