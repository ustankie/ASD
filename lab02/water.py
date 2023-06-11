
def make_tab(T):
    n=len(T)
    #print(n)
    k=2*n
    r=[[0,0] for _ in range(k)]
    i=0
    j=0
    while i<k:
        #print(i)
        width=T[j][1][0]-T[j][0][0]
        r[i]=[T[j][0][1],-width]
        i+=1
        r[i]=[T[j][1][1],width]
        i+=1
        j+=1
    return r

def filled(T,p):
    n=len(T)
    r=make_tab(T)
    r=MergeSort(r)
    #print(r)
    s=0
    w=0
    i=0
    full=0
    while i<2*n and s<p:
        while True:
            w+=r[i][1]
            #print(w,i)
            if r[i][1]<0:
                full+=1
            i+=1
            if i>=2*n or r[i][0]!=r[i-1][0]:
                 break
        s+=w
        #print(w,s,i,full)
    

    return full

def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)

    i=0
    j=0
    r=[[0,0]for _ in range(n1+n2)]
    while i<n1 and j<n2:
        if T1[i][0]>T2[j][0]:
            r[i+j]=T2[j]
            j+=1
        else:
            r[i+j]=T1[i]
            i+=1
    
    while i<n1:
        r[i+j]=T1[i]
        i+=1
    while j<n2:
            r[i+j]=T2[j]
            j+=1
    
    return r

def MergeSort(T):
    n=len(T)
    if n==1:
        return T
    mid=n//2
    L=T[:mid]
    R=T[mid:]

    return merge(MergeSort(L),MergeSort(R))

    
        






T=[[(1,3),(2,1)],[(3,4),(10,2)],[(5,7),(7,5)],[(11,2),(12,0)]]
print(filled(T,20))
