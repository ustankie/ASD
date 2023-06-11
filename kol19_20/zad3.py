def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    n=n1+n2
    i=0
    j=0
    r=[0 for _ in range(n)]
    while i<n1 and j<n2:
        if T1[i]<T2[j]:
            r[i+j]=T1[i]
            i+=1
        else:
            r[i+j]=T2[j]
            j+=1
    while i<n1:
        r[i+j]=T1[i]
        i+=1
    while j<n2:
        r[i+j]=T2[j]
        j+=1
    return r

def merge_sort(T):
    n=len(T)
    if n==1:
        return T
    q=n//2
    L=T[:q]
    R=T[q:]
    return merge(merge_sort(L),merge_sort(R))

def binary_search(T,x,i):
    p=0
    q=i-1
    while p<q:
        a=T[p]+T[q]
        if a==x:
            return True
        if a>x:
            q-=1
        else:
            p+=1
    return False

def sum(T):
    n=len(T)
    T=merge_sort(T)
    #print(T)
    min_val=T[0]
    for i in range(1,n):
        if T[i]==min_val:
            continue
        if not binary_search(T,T[i],i):
            return False
    return True


T=[2, 1,1, 3, 5, 7, 9, 4, 13, 17, 19]
print(sum(T))