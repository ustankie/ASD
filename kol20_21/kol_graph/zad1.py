from zad1testy import runtests
from collections import deque
def floyd(G):
    n=len(G)
    S=[[float('inf') for _ in range(n)]for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if G[x][y]:
                S[x][y]=G[x][y]

    for x in range(n):
        S[x][x]=0

    for t in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y],S[x][t]+S[t][y])

    return S

def make_graph(M,d,s,t):
    m=len(M)
    G=[]
    S=floyd(M)
    ind1=0
    ind2=0
    i=0
    for x in range(m):
        for y in range(m):
            if S[x][y]>=d:
                G.append([(x,y,i)])
                if (x,y)==(s,t):
                    ind1=i
                if (x,y)==(t,s):
                    ind2=i
                i+=1
                
    
    n=len(G)

    for x in range(n):
        for y in range(n):
            if x!=y:
                u1=G[x][0][0]
                u2=G[x][0][1]
                v1=G[y][0][0]
                v2=G[y][0][1]
                
                if ((M[u1][v1] and M[u2][v2]) or (u1!=v1 and M[u1][v1] and u2==v2) or (u2!=v2 and M[u2][v2] and u1==v1)) and not (u1==v2 and u2==v1):
                    #print(u1,u2,v1,v2)
                    G[x].append(G[y][0])
        
    #print(G)
    return G,ind1,ind2
# def find_ind(G,u):
#     n=len(G)
#     for i in range(n):
#         if G[i][0]==u:
#             return i
def BFS(G,s,t):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s[2]]=True

    while len(Q)>0:
        u=Q.popleft()
        #print(u)
        for v in G[u[2]]:
            if not vis[v[2]]:
                vis[v[2]]=True
                par[v[2]]=u[2]
                if v==t:
                    return par
                Q.append(v)
    return par
                
    
def atomic(M,s,t,d):
    G,ind1,ind2=make_graph(M,d,s,t)
    par=BFS(G,(s,t,ind1),(t,s,ind2))
    T=[]
    p=ind2
    while p!=None:
        T.append((G[p][0][0],G[p][0][1]))
        p=par[p]
    return T[::-1]


M=[
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]
M1 =[
[0, 5, 1, 0, 0, 0],
[5, 0, 0, 5, 0, 0],
[1, 0, 0, 1, 0, 0],
[0, 5, 1, 0, 1, 0],
[0, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0]
]
#print(atomic(M1,0,5,4)) 
runtests( atomic)
