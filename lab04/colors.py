def are_all(C):
    k=len(C)
    for i in range(k):
        if C[i]==0:
            return False
    return True

def colors(T,k):
    n=len(T)
    C=[0 for _ in range(k)]
    i=0
    j=0
    min_length=float("inf")
    while j<n:
        while j<n and not are_all(C):
            C[T[j]]+=1
            j+=1
            #print(C,j)
        while i<j and are_all(C):
            C[T[i]]-=1
            i+=1
        min_length=min(min_length, j-i+1)
        j+=1
    return (min_length)
T=[0,1,1,0,0,0,2,3,2,1,3,2,1,1,0,0]
k=4
print(colors(T,k))