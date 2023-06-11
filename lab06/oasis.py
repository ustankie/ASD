from collections import deque
def BFS(G,O):
    n=len(G)
    vis=[False for _ in range(n)]
    G2=[[0 for _ in range(n)]for _ in range(n)]
    Q=deque()
    Q.append(0)
    while len(Q)>0:
        u=Q.popleft()
        u_in_o=u in O
        for v in range(n):
            if G[u][v]:
                if u_in_o and v in O: 
                    repair(G,O,u,v)
                if not vis[v]:
                    vis[v]=True
                    Q.append(v)



    return G
def repair(G,O,u,v):
    n=len(G)
    G[u][v]=0
    for x in range(n):
        if G[v][x]:                              
            G[v][x]=0
            G[x][v]=0
            if G[u][x]==0:
                G[u][x]=1
                G[x][u]=1
                if x in O:
                    repair(G,O,u,x)

def transform(G):
    n=len(G)
    G2=[[0 for _ in range(n)]for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G2[u][v]=1
    return G2

def vert_to_edge(G):
    n=len(G)
    m=2
    
    for u in range(n):
        for v in range(n):
            if G[u][v]==1:
                G[u][v]=m
                G[v][u]=m
                m+=1
    E=[0 for _ in range(m)]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                E[G[u][v]]=(u,v)

    G2=[[0 for _ in range(m)]for _ in range(m)]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                m=G[u][v]
                #print(m)
                for i in range(n):
                    k=G[u][i]
                    if k and i!=v:
                        G2[m][k]=1
                for i in range(n):
                    k=G[i][v]
                    if k and i!=u:
                        G2[m][k]=1
    return G2,E

def euler(G):
    def DFS(u):
        for v in range(last[u],n):
            last[u]+=1
            if G[u][v]:
                #print(u,v)
                exists[u]=1
                G[u][v]=0
                G[v][u]=0              
                DFS(v)
        if exists[u]:
            T.append(u)
                
    n=len(G)
    last=[0 for _ in range(n)]
    exists=[0 for _ in range(n)]
    T=[]
    for u in range(n):
        m=0
        for v in range(m):
            if G[u][v]:
                m+=1
        if m%2==1:
            return None
    count=0
    
    for u in range(2,n):
        if last[u]<n:
            count+=1
            DFS(u)
        if count>1:
            #print(T[::-1])
            return None
    return T[::-1]



def oasis(G,O):
    n=len(G)
    m=len(O)
    G2=transform(G)
    BFS(G2,O)

    
    G3,E=vert_to_edge(G2)
    # print()
    # print(*G3,sep="\n")
    path=euler(G3)
    # print(E)
    # print(path)
    T=[]
    for i in range(len(path)-1):
        a=E[path[i]][0]
        b=E[path[i]][1]

        c=E[path[i+1]][0]
        d=E[path[i+1]][1]

        #print(a,b,c,d)

        if a==c or a==d:
            if not a in O:
                T.append(a)
                #print(T)
        else:
            if not b in O:
                T.append(b)
                #print(T)
    return T








G=[[1,5],[0,2,3],[1,3,4],[1,2,8],[6,7],[0,6],[4,5],[4,8],[3,7]]
O=[1,2,3,4,5]


print(oasis(G,O))