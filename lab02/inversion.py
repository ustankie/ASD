#merge sort
inv=0
def merge(T1,T2):
    global inv
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
    return T


def MergeSort(T,):
    n=len(T)
    if (n==1):
        return T
    mid=n//2
    L=T[:mid]
    R=T[mid:n]

    return merge(MergeSort(L),MergeSort(R))



T=[1,234,3,12,324,5,4,1,0]
T,inv=MergeSort(T,0)
print(T)
print(inv)


    