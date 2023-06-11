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

T=[1,2,53,2,0,6,7,22,54,67]
print(select(T,0,len(T)-1,8))