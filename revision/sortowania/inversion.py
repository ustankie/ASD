def merge(T1,T2,inv):
    n1=len(T1)
    n2=len(T2)
    #inv=0
    r=[0 for _ in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i]<=T2[j]:
            r[i+j]=T1[i]
            i+=1
        else:
            r[i+j]=T2[j]
            inv+=n1-i
            j+=1
    #inv+=n1-i
    while i<n1:
        r[i+j]=T1[i]
        i+=1
    while j<n2:
        r[i+j]=T2[j]
        j+=1       
    return r,inv
def merge_sort(T,inv):
    n=len(T)
    if n==1:
        return T,inv
    q=n//2
    L=T[:q]
    R=T[q:]
    L,inv1=merge_sort(L,inv)
    R,inv2=merge_sort(R,inv)
    return merge(L,R,inv+inv1+inv2)

T=[1,234,3,12,324,5,4,1,0]
T,inv=merge_sort(T,0)
print(T)
print(inv)
