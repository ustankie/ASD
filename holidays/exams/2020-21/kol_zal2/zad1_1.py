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
    
    def rec(best_przec,i):
        nonlocal n
        if i==n:
            return
        curr_przeciecie_0=whole_przeciecie[i-1]
        curr_przeciecie_1=przeciecie(best_przec,D[i])
        pole0=pole(curr_przeciecie_0)
        pole1=pole(curr_przeciecie_1)
        

        if pole0>pole1:
            F[i]=i
            best_pole[i]=pole0
            best_przeciecie[i]=curr_przeciecie_0
            rec(curr_przeciecie_0,i+1)
        elif pole0<pole1:
            F[i]=F[i-1]
            best_pole[i]=pole1
            best_przeciecie[i]=curr_przeciecie_1
            rec(curr_przeciecie_1,i+1)
        else:
            a=rec(curr_przeciecie_0,i+1)
            b=rec(curr_przeciecie_1,i+1)
            if a>b:
                F[i]=i
                best_pole[i]=pole0
                best_przeciecie[i]=curr_przeciecie_0
                rec(curr_przeciecie_0,i+1)
            else:
                F[i]=F[i-1]
                best_pole[i]=pole1
                best_przeciecie[i]=curr_przeciecie_1
                rec(curr_przeciecie_1,i+1)
        
        return best_pole[i]
                    
    whole_przeciecie[0]=D[0]
    for i in range(1,n):
        whole_przeciecie[i]=przeciecie(whole_przeciecie[i-1],D[i])

    pole_0=pole(D[0])
    pole_1=pole(D[1])
    if pole_0>pole_1:
        F[1]=1
        best_przeciecie[1]=D[0]
        best_pole[1]=pole_0
        rec(D[0],2)
    elif pole_0<pole_1:
        F[1]=0
        best_przeciecie[1]=D[1]
        best_pole[1]=pole_1
        rec(D[1],2)
    else:
        a=rec(D[1],2)
        b=rec(D[0],2)
        if a>b:
            F[1]=0
            best_przeciecie[1]=D[1]
            best_pole[1]=pole_1
            rec(D[1],2)
        else:
            F[1]=1
            best_przeciecie[1]=D[0]
            best_pole[1]=pole_0
            rec(D[0],2)


    

    # for i in range(2,n):
    #     curr_przeciecie_0=whole_przeciecie[i-1]
    #     curr_przeciecie_1=przeciecie(best_przeciecie[i-1],D[i])

    #     # print(curr_przeciecie_0)

    #     pole0=pole(curr_przeciecie_0)
    #     pole1=pole(curr_przeciecie_1)
        

    #     if pole0>pole1:
    #         F[i]=i
    #         best_pole[i]=pole0
    #         best_przeciecie[i]=curr_przeciecie_0
    #     else:
    #         F[i]=F[i-1]
    #         best_pole[i]=pole1
    #         best_przeciecie[i]=curr_przeciecie_1

    print(F)
    return F[n-1]




    
runtests( rect )
T=[(6, 4, 7, 5), (2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]
print(rect(T))


