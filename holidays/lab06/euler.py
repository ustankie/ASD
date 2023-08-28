def euler(G):
    n=len(G)
    last=[0 for _ in range(n)]
    R=[]
    for i in range(n):
        if len(G[i])%2==1:
            return []
        #G2.append([0 for _ in range(len(G[i]))])

    def DFS(u):
        for v in range(last[u],len(G[u])):
            last[u]+=1
            if G[u][v]!=None:
                
                a=G[u][v]
                for x in range(last[a],len(G[a])):
                    if G[a][x]==u:
                        G[a][x]=None
                G[u][v]=None
                DFS(a)
            
        R.append(u)
    
    for u in range(n):
        if last[u]<len(G[u]):
            DFS(u)
    
    return R[::-1]


G=[[1,2],[3,0,6,2,4,5],[0,1,6,4,3,5],[1,4,2,5],[5,2,3,1],[2,3,4,1],[1,2]]
G3=[[1,2],[0,3],[0,3,4,6],[1,2,5,7],[2,5],[4,3],[7,2],[3,6]]
G2=[[1],[],[0,3],[1,4],[5],[],[4,0]]
print(euler(G))

