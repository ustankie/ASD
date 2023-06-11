from zad1testy import runtests

def move_f(w,k,n):
    diff_l=w-k
    if w==n or k==n:
        diff_l-=1
        if diff_l>0:
            w=diff_l
            k=0
        else:
            w=0
            k=-diff_l
    return w,k

def move_b(w,k,n):
    diff_l=w-k
    if w<0 or k<0:
        diff_l+=1
        if diff_l>0:
            w=n-1
            k=n-1-diff_l
        else:
            w=n-1+diff_l
            k=n-1
    return w,k

def pivot(T,i1,j1,i2,j2):
    n=len(T)

    p=T[i2][j2]
    w=i1-1
    k=j1-1

    i,j=i1,j1


    while (i!=i2 or j!=j2):
        if T[i][j]<=p:
            w+=1
            k+=1
            w,k=move_f(w,k,n)
            T[w][k],T[i][j]=T[i][j],T[w][k]
        i+=1
        j+=1
        i,j=move_f(i,j,n)
        
    w+=1
    k+=1

    w,k=move_f(w,k,n)

    T[w][k],T[i2][j2]=T[i2][j2],T[w][k]
    
    return w,k


def QuickSort(T,i1,j1,i2,j2):
    diff_l=i1-j1
    diff_r=i2-j2
    n=len(T)

    if diff_l>diff_r or (diff_l==diff_r and i1<i2):
        
        pivi,pivj=pivot(T,i1,j1,i2,j2)

        pivi1=pivi-1
        pivj1=pivj-1
        pivi1,pivj1=move_b(pivi1,pivj1,n)
        
        pivi2=pivi+1
        pivj2=pivj+1
        pivi2,pivj2=move_f(pivi2,pivj2,n)
        
        QuickSort(T,i1,j1,pivi1,pivj1)
        QuickSort(T,pivi2,pivj2,i2,j2)


def Median(T):
    # tu prosze wpisac wlasna implementacje
    n=len(T)
    i1=n-1
    j1=0
    i2=0
    j2=n-1
    QuickSort(T,i1,j1,i2,j2)

    #return T



runtests( Median ) 
# T= [[ 23, 3, 5],  
#     [ 7,11,13],
#     [17,19,2]]
# T=Median(T)
# wypisz(T)
