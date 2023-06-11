def binary_search(T,p,r,x):
    n=r-p
    if p==r:
        if T[r][0]==x:
            return p
        return None
    q=n//2+p
    #print(T,q,p,r)
    if T[q][0]==x:
        return q
    if T[q][0]>x:
        return binary_search(T,p,q-1,x)
    else:
        return binary_search(T,q+1,r,x)

def insert(T,r,x):
    j=r
    while j>0 and T[j-1][0]>x:
        #print(j)
        T[j][0]=T[j-1][0]
        T[j][1]=T[j-1][1]
        j-=1
    T[j][0]=x
    T[j][1]=1

def max_word(w,k):
    n=len(w)
    B=[[None,None] for _ in range(n)]
    m=0

    for i in range(n-k+1):
        a=binary_search(B,0,m,w[i:i+k])
        if a==None:
            insert(B,m,w[i:i+k])
            m+=1
        else:
            B[a][1]+=1
    print(B)
    return counting_sort(B,m)

def counting_sort(T,n):
    B=[0 for _ in range(n)]
    R=[None for _ in range(n)]
    
    for i in range(n):
        B[T[i][1]]+=1
    for i in range(1,n):
        B[i]+=B[i-1]
    for i in range(n-1,-1,-1):
        R[B[T[i][1]]-1]=T[i][0]
        B[T[i][1]]-=1
    print(R)
    return R[n-1]




# T=[[0,5],[1,5],[5,1],[6,8],[8,9],[34,1],[56,1],[87,1]]
# print(binary_search(T,4,len(T)-1,34))
w="ababaaaabb"
print(len(w))
print(max_word(w,3))