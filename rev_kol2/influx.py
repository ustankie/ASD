def influx(G):
    n=len(G)

    i=0
    j=0

    while i<n and j<n:
        if G[i][j]==0:
            j+=1
        else:
            i+=1
    
    t=min(i,j)
    if t<n:
        for i in range(n):
            if (G[t][i]!=0 or G[i][t]!=1) and i!=t:
                return None
    return t

G=[[0,1,1,0],[0,0,0,0],[1,1,0,0],[1,1,0,0]]
G2=[[0,1,0,0,0,0,0],[1,0,0,0,0,1,1],[0,0,0,1,1,1,0],[0,0,1,0,0,1,1],[0,0,1,0,0,0,0],[0,1,1,1,0,0,0],[0,1,0,1,0,0,0]]

print(influx(G2))