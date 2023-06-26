def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    T=[0 for _ in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i]<T2[j]:
            T[i+j]=T1[i]
            i+=1
        else:
            T[i+j]=T2[j]
            j+=1
    while i<n1:
        T[i+j]=T1[i]
        i+=1
    while j<n2:
        T[i+j]=T2[j]
        j+=1        
    return T
def merge_sort(T):
    n=len(T)
    if n==1:
        return T
    q=n//2
    L=T[:q]
    R=T[q:]
    return merge(merge_sort(L),merge_sort(R))

T=[1,2,53,15,22,0,12,43,2,0,6,7,54,67]

T=merge_sort(T)
print(T)