from egz2atesty import runtests


def dominance(P):
    n=len(P)
    for i in range(n):
        P[i]=(P[i],i)

    P1=sorted(P,key=lambda x: x[0][0])
    P2=sorted(P,key=lambda x: x[0][1])

    T_x=[0 for _ in range(n)]
    T_y=[0 for _ in range(n)]

    for i in range(n):
        T_x[P1[i][1]]=True
        T_y[P2[i][1]]=True

    for i in range(n):

    # print(T_x)
    # print(T_y)
    maxi=0
    for i in range(n):
        if T_x[P[i][0]]==T_y[P[i][1]]:
            maxi=max(maxi,T_x[P[i][0]])

    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = False )

P=[(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]
P=[(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))
