

def pascal(S,P):
    n=len(S)
    F=[[0 for _ in range(n)]for _ in range(P+1)]
    
    sums=[[]for _ in range(n)]

    for i in range(n):
        S[i]=S[i][::-1]
        m=len(S[i])
        sums[i]=[0 for _ in range(m)]
        sums[i][0]=S[i][0]
        for j in range(1,m):
            sums[i][j]=sums[i][j-1]+S[i][j]

    m=len(S[0])
    for i in range(1,min(m,P+1)):
        F[i][0]=sums[0][i-1]
    
    for i in range(1,P+1):
        for j in range(1,n):
            m=len(S[j])
            F[i][j]=F[i][j-1]
            for k in range(1,min(i,m,P)+1):
                F[i][j]=max(F[i][j],F[i-k][j-1]+sums[j][k-1])


    return (F[P][n-1])


    

plates = [
    [9, 0, 3, 2, 8, 1],
    [33, 20, 1, 0, 0, 3],
    [5, 9, 1, 8, 1, 10],
    [3, 4, 8, 2, 6, 7]
]
guests = 17

print(pascal(plates,guests))
