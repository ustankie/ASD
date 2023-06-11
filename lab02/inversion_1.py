#merge sort
inv=0
def merge(T1,T2,inv):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    T=[0 for _ in range(n1+n2)]
    #print(T1,T2)
    while i<n1 and j<n2:
        if T1[i]<=T2[j]:
            T[i+j]=T1[i]

            i+=1
            
        else:
            T[i+j]=T2[j]
            inv+=(n1-i)
            #print(T1[i],T2[j],inv)
            #print(T1)
            j+=1
    
    while i<n1:
            T[i+j]=T1[i]
            i+=1
    
    while j<n2:
            T[i+j]=T2[j]
            j+=1
    return T,inv


def MergeSort(T,inv):
    n=len(T)
    if (n==1):
        return T,inv
    mid=n//2
    L=T[:mid]
    R=T[mid:n]
    a1,b1=MergeSort(L,inv)
    a2,b2=MergeSort(R,inv)
    return merge(a1,a2,inv+b1+b2)



T=[1,234,3,12,324,5,4,1,0]
T,inv=MergeSort(T,0)
print(T)
print(inv)


    