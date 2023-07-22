from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    F=[[float('inf') for _ in range(E+1)]for _ in range(n)]
    
    #for i in range(E+1):
    F[0][0]=0
    # def rec(i,j):
    #     if F[i][j]<float('inf'):
    #         return F[i][j]

    for i in range(1,n):
        for j in range(E+1):
            for k in range(j,E+1):
                if i-k>=0: 
                    dist=D[i]-D[i-k]
                    if k+dist<=E:
                        F[i][j]=min(F[i][j],F[i-k][k+dist]+C[i-k]*D[i-k])
    print(*F,sep="\n")
    return F[n-1][E]


            

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( planets, all_tests = False )
D= [0, 5, 10, 20]
C=  [2, 1, 3, 8]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E= 10
print(planets(D,C,T,E))
