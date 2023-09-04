
def colors(T,k):
    n=len(T)
    print(n)
    C=[0 for _ in range(k)]
    col_num=0
    min_length=float("inf")
    rang=(0,0)
    for i in range(k):
        if C[T[i]]==0:
            col_num+=1
        C[T[i]]+=1
    if col_num==k:
        rang=(0,k-1)
        min_length=k
        return rang
    i=0
    j=k
    
    while i+k-1<=j and j<n:
        print(i,j,col_num)
        if col_num==k:
            min_length=j-i
            rang= (i,j-1)
            C[T[i]]-=1
            if C[T[i]]==0:
                col_num-=1
            i+=1
        if col_num<k and j<n:
            
            if C[T[j]]==0:
                col_num+=1       
            C[T[j]]+=1
            j+=1
            
            #print(C,j)

    return (rang,min_length)
T=[0,1,1,0,0,0,2,3,2,1,3,2,1,1,0,0]
k=4
print(colors(T,k))