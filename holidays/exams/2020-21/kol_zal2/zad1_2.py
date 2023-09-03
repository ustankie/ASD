from zad1testy import runtests

def pole(A):
    x1,y1,x2,y2=A
    if (x2-x1)<0 or (y2-y1)<0:
        return 0
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
    whole_przeciecie2=[0 for _ in range(n)]
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
    
    whole_przeciecie2[n-1]=D[n-1]
    for i in range(n-2,-1,-1):
        # print(i)
        whole_przeciecie2[i]=przeciecie(whole_przeciecie2[i+1],D[i])
    
    best_pole=pole(whole_przeciecie2[1])
    best_ind=0
    for i in range(1,n-1):
        przec=przeciecie(whole_przeciecie[i-1],whole_przeciecie2[i+1])
        
        pol=pole(przec)
        if pol>best_pole:
            best_pole=pol
            best_ind=i

    przec=whole_przeciecie[n-2]
    pol=pole(przec)
    print(pol)
    if pol>best_pole:
        best_pole=pol
        best_ind=n-1

    return best_ind




    
runtests( rect )
T=[(6, 4, 7, 5), (2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]
print(rect(T))


