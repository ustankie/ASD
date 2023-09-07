from egz2atesty import runtests


def dominance(P):
    n=len(P)
    # print(P)
    C=[0 for _ in range(n+1)]
    B=[0 for _ in range(n)]

    for i in range(n):
        C[P[i][0]]+=1

    for i in range(1,n+1):
        C[i]+=C[i-1]
    print(C)
    
    for i in range(n-1,-1,-1):
        B[C[P[i][0]]-1]=P[i]
        C[P[i][0]]-=1

    T_y=[0 for _ in range(n+1)]

    for i in range(n):
        T_y[B[i][1]]+=1
    
    for i in range(1,n+1):
        T_y[i]+=T_y[i-1]
    print(B)
    print(T_y)
    maxi=0
    for i in range(n):
        for j in range(B[i][1]):
            T_y[j]-=1
        maxi=max(n-T_y[B[i][1]])



    # for i in range(n):
    #     #if T_x[P[i][0]]==T_y[P[i][1]]:
    #     maxi=max(maxi,min(T_x[P[i][0]][i],T_y[P[i][1]][i]))

    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( dominance, all_tests = False )

P=[(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]
P=[(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))
