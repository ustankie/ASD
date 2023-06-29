
def przedzialy(T):
    n=len(T)
    r=[0 for _ in range(n)]
    heap_sort(T)
    print(T)
    for i in range(1,n):
        j=i-1
        while j>=0 and r[j]<j:
            if T[j][0]>=T[i][0] and T[j][1]<=T[i][1]:
                r[i]+=1
            j-=1
        if j>0 and r[j]==j:
            r[i]+=1
    max_val=0
    k=0
    for i in range(n):
        if max_val<r[i]:
            k=i
            max_val=r[i]
    return T[k]
def binary_search(T,x):
    n=len(T)
    i=0
    j=n-1
    q=n//2
    while i<j and (T[q][0][0]!=x[0] or T[q][0][1]!=x[1]):
        #print(i,q,j)
        if T[q][0][1]<x[1]:
            i=q+1
        else:
            j=q-1
        q=(j-i)//2+i
    if j==i:
        return i
    q+=1
    while q<n and T[q]==T[q-1]:
        q+=1
    q-=1
    return q
def optimize(T):
    n=len(T)
    r=[[0,0] for _ in range(n)]
    i=1
    j=-1
    count=1
    while i<n:
        while i<n and T[i-1]==T[i]:
            i+=1
            count+=1
        if i<n:
            i-=1
            j+=1
            r[j]=[T[i],count]
            i+=1
        if i<n: 
            i+=1
        count+=1

    i-=1
    j+=1
    r[j]=[T[i],count]
    i+=1
    r=r[:j+1]
    # for i in range(1,j+1):
    #     r[i][1]+=r[i-1][1]
    return r
def optimize2(T):
    n=len(T)
    r=[[0,0] for _ in range(n)]
    i=1
    j=0
    r[0]=[T[0],0]
    count=0
    while i<n:
        count=0
        while i<n and T[i-1][0]==T[i][0]:
            while i<n and T[i-1]==T[i]:
                i+=1
                count+=1
            if i<n:
                j+=1
                r[j]=[T[i],r[j-1][1]]
                i+=1
            # else:
            #     i-=1
            #     j+=1
            #     r[j]=[T[i],r[j-1][1]]
            #     i+=1
            count+=1
        count+=1
        if i<n:
            j+=1
            r[j]=[T[i],count+r[j-1][1]]
        # else:
        #     i-=1
        #     j+=1
        #     r[j]=[T[i],r[j-1][1]]
        
        i+=1
    # j+=1
    # i-=2
    # r[j]=[T[i],count]
    r=r[:j+1]
    # for i in range(1,j+1):
    #     r[i][1]+=r[i-1][1]
    return r


def przedzialy2(T):
    n=len(T)
    R=T[:]
    L=T[:]
    print(T)
    heap_sort(R,1)
    heap_sort(L,2)
    print(R)
    print(L)
    R=optimize(R)
    L=optimize2(L)
    print(R)
    print(L)
    n=len(L)
    maximum=0
    biggest=0
    for i in range(n):
        a=L[i][0]
        x=binary_search(R,a)
        print(x,i)
        x=R[x][1]-L[i][1]
        if x>maximum:
            maximum=x
            biggest=L[i]
    biggest=biggest[0]
    return biggest,maximum

###############################################################################
#rozw O(nlogn)

def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i):return (i-1)//2

def heapify(T,i,n,p):
    r=right(i)
    l=left(i)
    max_ind=i
    if p==1:
        if l<n and ((T[l][1]>T[max_ind][1])or(T[l][1]==T[max_ind][1]and T[l][0]<T[max_ind][0])): max_ind=l
        if r<n and ((T[r][1]>T[max_ind][1])or(T[r][1]==T[max_ind][1]and T[r][0]<T[max_ind][0])): max_ind=r
    else:
        if l<n and ((T[l][0]>T[max_ind][0])or(T[l][0]==T[max_ind][0]and T[l][1]<T[max_ind][1])): max_ind=l
        if r<n and ((T[r][0]>T[max_ind][0])or(T[r][0]==T[max_ind][0]and T[r][1]<T[max_ind][1])): max_ind=r
    if i!=max_ind:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify(T,max_ind,n,p)

def build_heap(T,p):
    n=len(T)
    for i in range(n-1,-1,-1):
        heapify(T,i,n,p)


def heap_sort(T,p):
    n=len(T)
    build_heap(T,p)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T,0,i,p)


def binary_search3(T,x):
    n=len(T)
    i=0
    j=n-1
    q=n//2
    while i<j and (T[q][0]!=x[0] or T[q][1]!=x[1]):

        if T[q][1]<x[1] or (T[q][1]==x[1] and T[q][0]>x[0]): #uwagaa
            i=q+1
        else:
            j=q-1
        q=(j-i)//2+i
    if j==i:
        return i
    q+=1
    while q<n and T[q]==T[q-1]: #ostatni chcemy wziac
        q+=1
    q-=1
    return q

def przedzialy3(T):
    n=len(T)
    R=T[:]
    L=T[:]


    heap_sort(R,1)
    heap_sort(L,2)
    print(L)
    print(R)
    maximum=0
    biggest=0
    for i in range(n):
        a=L[i]
        x=binary_search3(R,a)

        x=x-i

        if x>maximum:
            maximum=x
            biggest=L[i]

    return biggest,maximum




T = [[1,2],[2,4],[1,9],[1,5],[1,4],[1,7],[2,8],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[16,17]]
#heap_sort(T,1)
#print(T)
print(przedzialy3(T))