from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    F=[[float('inf') for _ in range(E+1)]for _ in range(n)]
    
    #for i in range(E+1):
    F[0][0]=0
    for i in range(n):
        if T[i][0]!=i:
            F[T[i][0]][0]=min(F[T[i][0]][0],F[i][0]+T[i][1])
        for j in range(E+1):

            for k in range(i,n):
                dist=D[k]-D[i]
                if dist<=j:
                    for l in range(j-dist):
                        F[k][l]=min(F[k][l],F[i][j])
                else:
                    to_tank=dist-j
                    if to_tank<=E:
                        for l in range(E-to_tank+1):
                            F[k][l]=min(F[k][l],F[i][j]+C[i]*(to_tank+l))
    #print(*F,sep="\n")
    return min(F[n-1])


            

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
D= [0, 5, 10, 20]
C=  [2, 1, 3, 8]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E= 10
print(planets(D,C,T,E))
