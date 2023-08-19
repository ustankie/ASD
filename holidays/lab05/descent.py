def descent(G,x,y):
    n=len(G)
    par=[None for _ in range(n)]

    def DFS(u,k):
        for v in range(n):
            if 0<G[u][v]<k:
                par[v]=u
                if v==y:
                    return True
                if DFS(v,G[u][v]):
                    return True
        return False

    R=[]
    a= DFS(x,float('inf'))    
    if a:
        p=y
        while p!=None:
            R.append(p)
            p=par[p]
    return a,R[::-1]


G=[[0,1,0,4,3,0,0],[1,0,1,0,0,0,0],[0,1,0,0,0,0,0],[4,0,0,0,0,2,3],[3,0,0,0,0,2,0],[0,0,0,2,2,0,1],[0,0,0,3,0,1,0]]
print(descent(G,0,6))
    