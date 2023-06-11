def partition(T,p,r,pivot):
    x=T[pivot]
    i=p-1
    for j in range(p,r):
        if T[j]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[pivot],T[i]=T[i],T[pivot]
    return i
def heapify_b(T,i,n):
    r=right(i)
    l=left(i)
    max_ind=i
    if l<n and T[l][0]>T[max_ind][0]: max_ind=l
    if r<n and T[r][0]>T[max_ind][0]: max_ind=r
    if max_ind!=i:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify_b(T,max_ind,n)
def heapify_s(T,i,n):
    r=right(i)
    l=left(i)
    max_ind=i
    if l<n and T[l][0]<T[max_ind][0]: max_ind=l
    if r<n and T[r][0]<T[max_ind][0]: max_ind=r
    if max_ind!=i:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify_s(T,max_ind,n)

def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2

class Heap():
    def __init__(self,n):
        self.T=[0 for _ in range(n)]
        self.size=0
def insert_b(H,el):
    H.T[H.size]=el
    p=parent(H.size)
    q=H.size
    H.size+=1
    while p>=0 and H.T[q]>H.T[p]:
        H.T[p],H.T[q]=H.T[q],H.T[p]
        q=p
        p=parent(q)
def insert_s(H,el):
    H.T[H.size]=el
    p=parent(H.size)
    q=H.size
    H.size+=1
    while p>=0 and H.T[q]<H.T[p]:
        H.T[p],H.T[q]=H.T[q],H.T[p]
        q=p
        p=parent(q)      

def build(T,H):
    n=len(T)
    for i in range(n):
        insert(H,T[i])
    for i in range(n):
        print(H.T[i])

def pop(H):
    a=H.T[0]
    for i in range(H.size-1):
        H.T[i]=H.T[i+1]
    H.size-=1
    return a
def extract_median(T):
    n=len(T)
    k=max(T)
    B=[0 for i in range(k+1)]
    R=[0 for _ in range(n)]
    for i in range(n):
        B[T[i]]+=1
    
    for i in range(1,k+1):
        B[i]+=B[i-1]

    for i in range(n-1,-1,-1):
        R[B[T[i]]-1]=T[i]
        B[T[i]]-=1
    for i in range(n):
        T[i]=R[i]
    return n//2

def extract_median2(T):
    n=len(T)
    print(T)
    B=Heap(n)
    S=Heap(n)
    x=[T[0],0]
    for i in range(1,n//2+1):
        insert_b(S,[T[i],i])
    for i in range(n//2+1,n):
        insert_s(B,[T[i],i])
    print(B.T,S.T,x)

    while (B.size>0 and x[0]>B.T[0][0]) or (S.size>0 and x[0]<S.T[0][0]):
        print(B.T,S.T,x)

        if x[0]>B.T[0][0]:
            x,B.T[0]=B.T[0],x
            #print(x,B.T,S.T)
            heapify_s(B.T,0,B.size-1)
        

        if x[0]<S.T[0][0]:
            x,S.T[0]=S.T[0],x
            heapify_b(S.T,0,S.size-1)
        #print(x,B.T,S.T)

    print(x)
    return x[1]

def divide(T,p,r):
    n=r-p-4
    print(n,len(T),p,r)
    M=[extract_median2(T[i+p:i+p+5]) for i in range(0,n,5)]
    print("M: ",M)
    return extract_median2(M)


def select(T,p,r,k):
    while p<r:
        x=divide(T,p,r)
        print(x)
        q=partition(T,p,r,x)
        if q==k:
            return T[q]
        if k>q:
            return select(T,q+1,r,k)
        else:
            return select(T,p,q-1,k)
    

T=[2,2,6,7,8,45,6,7,7,5,45,3,5,0,7]
print(select(T,0,len(T)-1,10))
extract_median(T)
print(T)