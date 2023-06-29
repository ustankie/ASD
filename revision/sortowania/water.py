def convert(T):
    n=len(T)
    r=[[0,0]for _ in range(2*n)]
    i=0
    j=0
    while j<n:
        width=T[j][1][0]-T[j][0][0]
        r[i]=[T[j][1][1],width]
        i+=1
        r[i]=[T[j][0][1],-width]
        i+=1
        j+=1
    return r
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    r=[[0,0]for _ in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][0]<T2[j][0]:
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

def fill(T,p):
    n=len(T)
    r=convert(T)
    print(r)
    r=merge_sort(r)
    print(r)
    s=0
    i=0
    w=0
    filled=0
    while s<p:
        while True:
            w+=r[i][1]
            if r[i][1]<0:
                filled+=1
            i+=1
            if i==(2*n) or r[i][0]!=r[i-1][0]:
                break
        s+=w
    return filled


T=[[(1,3),(2,1)],[(3,4),(10,2)],[(5,7),(7,5)],[(11,2),(12,0)]]
print(fill(T,20))