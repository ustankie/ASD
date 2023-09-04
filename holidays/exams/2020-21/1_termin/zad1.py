from zad1testy import runtests
def binsearch(A,x):
    i=0
    j=len(A)-1

    while i<=j:
        q=(i+j)//2
        if A[q]==x:
            return q
        if A[q]<x:
            i=q+1
        else:
            j=q-1
    return i

def chaos_index( T ):
    n=len(T)
    k=0
    for i in range(n):
        T[i]=(T[i],i)
    A=sorted(T)

    for i in range(n):
        x=binsearch(A,T[i])
        curr_k=abs(i-x)
        k=max(k,curr_k)



    return k


runtests( chaos_index )
