def matrices(A):
    n=len(A)
    F=[[float('inf') for i in range(n)]for _ in range(n)]

    for i in range(n):
        F[i][i]=0
        if i<n-1:
            F[i][i+1]=A[i][0]*A[i][1]*A[i+1][1]
        
    
    for j in range(2,n):
        for i in range(n-j):       
            for k in range(i,i+j):
                F[i][i+j]=min(F[i][i+j],F[i][k]+F[k+1][i+j]+A[i][0]*A[k][1]*A[i+j][1])

    return F[0][n-1]





A1 = [(1, 3), (3, 5)] # 15
A2 = [(1, 3), (3, 5), (5, 7)] # 50
A3 = [(40, 20), (20, 30), (30, 10), (10, 30)] # 26000 = (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30
A4 = [(10, 20), (20, 30), (30, 40), (40, 30)] # 30K
A4 = [(2, 2), (2, 8), (8, 6), (6, 9), (9, 9), (9, 2), (2, 1), (1, 9), (9, 6)] # 287
A5 = [(2, 2), (2, 8), (8, 6), (6, 9), (9, 9), (9, 2), (2, 1)] # 221

for A in (A1, A2, A3, A4, A5):
    print(matrices(A))