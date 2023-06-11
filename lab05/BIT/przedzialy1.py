def build(T):
    m=len(T)
    n=0
    for i in range(m):
        n=max(n,T[i][1])
    G=[[]for _ in range(n+1)]
    #print(G)
    for i in range(m):
        G[T[i][0]].append(T[i][1])
        for j in range(i+1,m):
            minp=min(T[i][0],T[j][0])
            maxp=max(T[i][0],T[j][0])
            mink=min(T[i][1],T[j][1])
            maxk=max(T[i][1],T[j][1])
            #print(i,j)
            
            if (G[T[i][0]]<=G[T[j][1]] and G[T[i][0]]>=G[T[j][0]]) or (G[T[j][0]]<=G[T[i][1]] and G[T[i][0]]>=G[T[i][0]])\
            or (G[T[j][0]]>=G[T[i][0]] and G[T[j][1]]<=G[T[i][1]]) or (G[T[j][0]]<=G[T[i][0]] and G[T[j][1]]>=G[T[i][1]]):
                #print(G)
                second=min(maxp,mink)
                third=max(maxp,mink)
            
                G[minp].append(second)
                G[second].append(third)
                G[third].append(maxk)
        #print(G)

    return G

def przedzialy(T,s,k):
    def Visit(G,u):
        if u>=k: 
            return True
        vis[u]=True
        for v in G[u]:
            if v>=k: 
                return True
            if not vis[v]:           
                par[v]=u
                Visit(G,v)

    G=build(T)
    #print(*G,sep="\n")
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    vis[s]=True
    for u in G[s]:
        if not vis[u]:
            if(Visit(G,u)): 
                return True

    return False
            


T=[(1,3),(2,6),(3,4),(1,2),(5,8)]
print(przedzialy(T,4,8))