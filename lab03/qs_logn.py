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

def qs_logn(T,p,r):
    while p<r:
        q=partition(T,p,r)
        if (q-p)>(r-q):
            qs_logn(T,q+1,r)
            r=q-1
        else:
            qs_logn(T,p,q-1)
            p=q+1
T=[1,2,53,15,22,0,12,43,2,0,6,7,54,67]

qs_logn(T,0,len(T)-1)
print(T)
