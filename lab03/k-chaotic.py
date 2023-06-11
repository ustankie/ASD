def partition(T,p,r):
    x=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i

def select(T,p,r,k):
    while p<r:
        q=partition(T,p,r)
        if q==k:
            return T[q]
        if k>q:
            return select(T,q+1,r,k)
        else:
            return select(T,p,q-1,k)

def k_chaotic(T,p,r,k):
    n=len(T)
    # for i in range(k+1,n,k+1):
    #     select(T,i-k,n-1,i)
    if k<(r-p):
        q=(r-p)//2+p
        select(T,p,r,q)
        k_chaotic(T,p,q-q,k)
        k_chaotic(T,q+1,r,k)
        
    

T=[1,2,53,15,22,0,12,4,2,0,6,7,54,67]
k_chaotic(T,0,len(T)-1,5)
print(T)