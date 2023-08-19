from collections import deque
#pary wierzchołków
def cycle(G):
    n=len(G)
    for i in range(n-1):
        for j in range(i+1,n):
            count=0
            for k in range(j+1,n):
                
                if G[i][k] and G[j][k]:
                    count+=1
                if count==2:
                    return True
    return False
#czwórki
def cycle2(G):
    n=len(G)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if G[i][j] and G[j][k] and G[k][l] and G[l][i]:
                        return True
    return False
#BFS

def BFS(G,s):
    n=len(G)
    Q=deque()
    Q.append(s)
    val=[None for _ in range(n)]
    par=[None for _ in range(n)]
    val[s]=0
    
    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            if G[u][v] and val[v]==None:
                val[v]=val[u]+1
                par[v]=u
                Q.append(v)
            elif G[u][v] and val[v]==1 and val[u]==2 and par[u]!=v:
                return True
    return False

def BFS_list(G,s):
    n=len(G)
    Q=deque()
    Q.append(s)
    val=[None for _ in range(n)]
    par=[None for _ in range(n)]
    val[s]=0
    
    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if val[v]==None:
                val[v]=val[u]+1
                par[v]=u
                Q.append(v)
            elif  val[v]==1 and val[u]==2 and par[u]!=v:
                return True
    return False

def cycle3(G):
    n=len(G)
    for i in range(n):
        if BFS_list(G,i):
            return True
    return False

G=[[0,1,0,0,0,0,0],[1,0,0,0,0,1,1],[0,0,0,1,1,1,0],[0,0,1,0,0,1,1],[0,0,1,0,0,0,0],[0,1,1,1,0,0,0],[0,1,0,1,0,0,0]]
G2=[[0,1,0,0,0,0,0],[1,0,1,0,0,0,0],[0,1,0,1,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,0,1,1],[0,0,0,0,1,0,1],[0,0,0,1,1,1,0]]
G3=[[1],
    [0,5,6],
    [3,4,5],
    [2,5,6],
    [2,6],
    [2],
    [1,2,3],
    [1,3]
    ]
G4=[[1],
    [0,2],
    [1,3],
    [2,6],
    [3,5,4],
    [5,6],
    [4,6]

]
print(cycle3(G4))