def partition(A,p,k):
    x=A[k]
    j=p-1
    for i in range(p,k):
        if A[i]<x:
            j+=1
            A[i],A[j]=A[j],A[i]
    j+=1
    A[k],A[j]=A[j],A[k]
    return j

def quicksort(A,p,k):
    while p<k:
        q=partition(A,p,k)
        if (q-p)>(k-q):
            quicksort(A,q+1,k)
            k=q-1
        else:
            quicksort(A,p,q-1)
            p=q+1

T=[1,2,53,15,22,0,12,43,2,0,6,7,54,67]

quicksort(T,0,len(T)-1)
print(T)



