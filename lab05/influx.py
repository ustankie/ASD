def influx(G):
    n=len(G)
    i=0
    j=0
    while i<n and j<n:
        print(i,j)

        if G[i][j]==0:
            j+=1
        else:
            i+=1
    i=min(i,j)
    
    for k in range(n):
        if (G[i][k]!=0 or G[k][i]!=1) and k!=i:
            return False
    return True,i
G=[[0,1,1,0],[0,0,0,0],[1,1,0,0],[1,1,0,0]]
G2=[[0,1,0,0,0,0,0],[1,0,0,0,0,1,1],[0,0,0,1,1,1,0],[0,0,1,0,0,1,1],[0,0,1,0,0,0,0],[0,1,1,1,0,0,0],[0,1,0,1,0,0,0]]

print(influx(G2))