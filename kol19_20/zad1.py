def count(x):
    r=[0 for _ in range(10)]

    while x>0:
        r[x%10]+=1
        x//=10
    one=0
    more=0
    for i in range(10):
        if r[i]==1:
            one+=1
        elif r[i]>0:
            more+=1
    return [one,more]

def right(i):
    return 2*i+2
def left(i): 
    return 2*i+1
def parent(i):
    return (i-1)//2

def heapify(T,R,i,n):
    r=right(i)
    l=left(i)
    max_ind=i
    if r<n and (R[r][0]<R[max_ind][0] or (R[r][0]==R[max_ind][0] and R[r][1]>R[max_ind][1])): 
        max_ind=r

    if l<n and (R[l][0]<R[max_ind][0] or (R[l][0]==R[max_ind][0] and R[l][1]>R[max_ind][1])): 
        max_ind=l
    if i!=max_ind:
        T[max_ind],T[i]=T[i],T[max_ind]
        R[max_ind][0],R[i][0]=R[i][0],R[max_ind][0]
        R[max_ind][1],R[i][1]=R[i][1],R[max_ind][1]
        heapify(T,R,max_ind,n)

def build_heap(T,r):
    n=len(T)
    for i in range(n-1,-1,-1):
        heapify(T,r,i,n)

def heap_sort(T,r):
    n=len(T)
    build_heap(T,r)
    for i in range(n-1,0,-1):
        T[i],T[0]=T[0],T[i]
        r[i][0],r[0][0]=r[0][0],r[i][0]
        r[i][1],r[0][1]=r[0][1],r[i][1]
        heapify(T,r,0,i)
    


def pretty_sort(T):
    n=len(T)
    r=[count(T[i]) for i in range(n)]
    heap_sort(T,r)
    


T=[455,1266,2344,67333,123,43,114577]
pretty_sort(T)
print(T)