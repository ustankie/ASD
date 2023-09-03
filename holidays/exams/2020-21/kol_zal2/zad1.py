from zad1testy import runtests

def pole(A):
    x1,y1,x2,y2=A
    return (x2-x1)*(y2-y1)

def przeciecie(A,B):
    x1a,y1a,x2a,y2a=A
    x1b,y1b,x2b,y2b=B
    x1=max(x1a,x1b)
    x2=min(x2a,x2b)
    y1=max(y1a,y1b)
    y2=min(y2a,y2b)
    return (x1,y1,x2,y2)

def rect(D):
    n=len(D)
    F=[0 for _ in range(n)]
    best_pole=[0 for _ in range(n)]
    best_przeciecie=[0 for _ in range(n)]
    whole_przeciecie=[0 for _ in range(n)]
    # print(D)

    pole_0=pole(D[0])
    pole_1=pole(D[1])
    if pole_0>pole_1:
        F[1]=1
        best_przeciecie[1]=D[0]
        best_pole[1]=pole_0
    else:
        F[1]=0
        best_przeciecie[1]=D[1]
        best_pole[1]=pole_1
    
    # print(przeciecie((3,1,4,2),(6,1,7,2)))
    whole_przeciecie[0]=D[0]
    for i in range(1,n):
        whole_przeciecie[i]=przeciecie(whole_przeciecie[i-1],D[i])
    for i in range(2,n):
        curr_przeciecie_0=whole_przeciecie[i-1]
        curr_przeciecie_1=przeciecie(best_przeciecie[i-1],D[i])

        # print(curr_przeciecie_0)
        
        pole0=pole(curr_przeciecie_0)
        pole1=pole(curr_przeciecie_1)

        if curr_przeciecie_0[0]>curr_przeciecie_0[2] or curr_przeciecie_0[1]>curr_przeciecie_0[3]:
            pole0=0

        if curr_przeciecie_1[0]>curr_przeciecie_1[2] or curr_przeciecie_1[1]>curr_przeciecie_1[3]:
            pole1=0

        if pole0>pole1:
            F[i]=i
            best_pole[i]=pole0
            best_przeciecie[i]=curr_przeciecie_0
        else:
            F[i]=F[i-1]
            best_pole[i]=pole1
            best_przeciecie[i]=curr_przeciecie_1

    # print(F)
    # a=whole_przeciecie[0]
    # for i in range(2,n):
    #     a=przeciecie(a,D[i])
    # b=whole_przeciecie[2]
    # for i in range(4,n):
    #     b=przeciecie(b,D[i])
    # print(a,b,pole(a),pole(b))
    return F[n-1]




    
runtests( rect )
T=[(6, 4, 7, 5), (2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]
print(rect(T))


