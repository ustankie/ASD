from collections import deque
#mój pomysł
def BFS(G,s):
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range(n)]
    val=[None for v in range(n)]

    val[s]=0
    visited[s]=True

    Q=deque()
    Q.append(s)


    while (len(Q)>0):
        u=Q.popleft()
        if val[u]>2: 
            return False
        for v in range(n):
            if G[u][v]:
                if not visited[v]:
                    visited[v]=True
                    val[v]=val[u]+1
                    parent[v]=u
                    Q.append(v)
                elif val[u]==2 and val[v]==1 and parent[u]!=v: 
                    # print(val)
                    # print(parent)
                    return True
    return False

def cycle1(G):
    n=len(G)
    for v in range(n):
        if(BFS(G,v)):
            return True
    return False

#pary wierzcholkow
def cycle2(G):
    n=len(G)
    for i in range(n-1):
        for j in range(i+1,n):
            count=0
            for k in range(n):
                if G[i][k] and G[j][k]:
                    count+=1
            if count==2:
                return True
    return False
#czwórki wierzchołków
def cycle3(G):
    n=len(G)
    for i in range(n-1):
        for j in range(i+1,n-1):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if G[i][k] and G[i][l] and G[j][k] and G[j][l]: #and k!=l and k!=i and k!=j and i!=j and i!=l and j!=l
                        return True
    return False



G=[[0,1,0,0,0,0,0],[1,0,0,0,0,1,1],[0,0,0,1,1,1,0],[0,0,1,0,0,1,1],[0,0,1,0,0,0,0],[0,1,1,1,0,0,0],[0,1,0,1,0,0,0]]
G2=[[0,1,0,0,0,0,0],[1,0,1,0,0,0,0],[0,1,0,1,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,0,1,1],[0,0,0,0,1,0,1],[0,0,0,1,1,1,0]]
print(cycle3(G2))