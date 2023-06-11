def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    r=[0 for _ in range(n1+n2)]
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
def Merge_Sort(T):
    # print(T)
    # n=len(T)
    # if n==1:
    #     return T[0]
    # A=merge(T[0],T[1])
    # T=T[1:]
    # T[0]=A
    # return Merge_Sort(T)
    n=len(T)
    i=1
    while n>1:
        i=1
        while i<n:
            n-=1
            print(i)
            print(T)
            A=merge(T[i-1],T[i])
            T=T[1:]
            T[0]=A
            i+=2
    return T[0]


def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2


def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and T[max_ind]>T[l]:
        max_ind=l
    if r<n and T[max_ind]>T[r]:
        max_ind=r
    if i!=max_ind:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify(T,max_ind,n)

def build_heap(T):
    n=len(T)
    for i in range(n-1,-1,-1):
        heapify(T,i,n)

def heap_sort(T):
    n=len(T)
    build_heap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T,0,i)

def merge_heap(T):
    n=len(T)
    k=0
    for i in range(n):
        k+=len(T[i])
    res=[0 for _ in range(k)]
    i=1
    while n>1:
        i=1
        while i<n:
            n-=1
            print(i)
            print(T)
            A=
            T=T[1:]
            T[0]=A
            i+=2
    return T[0]






T=[[1,2,5,64,289,290],[0,1,2,5,7,8,9,33,54,230],[18,19],[90,10000]]
A=merge_heap(T)
print(A)
