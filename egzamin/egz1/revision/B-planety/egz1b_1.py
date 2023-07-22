from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    F=[[float('inf') for _ in range(E+1)]for _ in range(n)]
    
    #for i in range(E+1):
    F[0][0]=0
    for i in range(n):
        next=T[i][0]
        dist=D[next]-D[i]
        #for t in range(len(T[i])):  
        if dist>0:
            for j in range(E+1):

                minimum_tank=dist-j
                burn=j-dist
                print(dist,burn)
                if minimum_tank>=0:
                    for l in range(minimum_tank,E+1):
                        #print(l)
                        a=burn+l
                        if  a<=E and F[next][a]>F[i][j]+C[i]*l+T[i][1]:
                            F[next][a]=F[i][j]+C[i]*l+T[i][1]
                print(*F,sep="\n")
                print()
    print(*F,sep="\n")
    return F[n-1][E]


            

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( planets, all_tests = False )
D= [0, 5, 10, 20]
C=  [2, 1, 3, 8]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E= 10
print(planets(D,C,T,E))
