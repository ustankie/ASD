from egz2atesty import runtests


def dominance(P):
    n=len(P)
    for i in range(n):
        P[i]=(P[i],sum(P[i]))
    P.sort(key=lambda x :x[0][0])
    # print(P)

    cnt=0
    for i in range(n-1):
        if P[i][0]<P[n-1][0] and P[i][1]<P[n-1][1]:
            cnt+=1
    
    P.sort(key=lambda x :x[0][1])
    # print(P)

    cnt2=0
    for i in range(n-1):
        if P[i][0]<P[n-1][0] and P[i][1]<P[n-1][1]:

            cnt2+=1
    P.sort(key=lambda x :x[1])
    cnt3=0
    for i in range(n-1):
        if P[i][0]<P[n-1][0] and P[i][1]<P[n-1][1]:
            cnt2+=1

    # for i in range(n):
    #     #if T_x[P[i][0]]==T_y[P[i][1]]:
    #     maxi=max(maxi,min(T_x[P[i][0]][i],T_y[P[i][1]][i]))

    return max(cnt,cnt2,cnt3)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

P=[(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]
P=[(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))
