def euler(G):
    def DFS(G,u):
        #last[u]+=1
        # print(G[u])
        # print(last[u])
        #print(u)
        for i in range(last[u],len(G[u])):
            v=G[u][i]
            last[u]+=1
            if v!=None:
                #print(v,last[v],G[v])
                for x in range(last[v],len(G[v])):
                    if G[v][x]==u:
                        G[v][x]=None
                G[u][i]=None
                DFS(G,v)
        T.append(u)

    n=len(G)
    last=[0 for _ in range(n)]
    T=[]
    for u in range(n):
        if len(G[u])%2==1:
            return None
    
    count=0
    for u in range(n):
        if last[u]<len(G[u]):
            #print(G)
            DFS(G,u)
            count+=1
    #print(count)
        if count>1:
            return None
    T.reverse()
    return T

G=[[1,2],[3,0,6,2,4,5],[0,1,6,4,3,5],[1,4,2,5],[5,2,3,1],[2,3,4,1],[1,2]]
G3=[[1,2],[0,3],[0,3,4,6],[1,2,5,7],[2,5],[4,3],[7,2],[3,6]]
G2=[[1],[],[0,3],[1,4],[5],[],[4,0]]
print(euler(G))