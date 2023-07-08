from kolutesty import runtests
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    T=[0 for _ in range(n1+n2)]
    while i<n1 and j<n2:
        if T1[i]>T2[j]:
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


def MergeSort(T):
    n=len(T)
    if (n==1):
        return T
    mid=n//2
    L=T[:mid]
    R=T[mid:n]

    return merge(MergeSort(L),MergeSort(R))
def partition(T,p,r):
    x=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]>x:
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

def ice_cream( T ):
    n=len(T)
    qs_logn(T,0,n-1)
    #print(T)
    sum=0
    i=0
    while i<n and T[i]-i>0:
        sum+=T[i]-i
        i+=1
        # if T[i]-i>=0:
        #     print(T[i])
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
T=[11, 16, 5, 6, 15, 12, 9, 18, 11, 16]
print(ice_cream(T))
