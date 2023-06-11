
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
    if l<n and T[max_ind]<T[l]:
        max_ind=l
    if r<n and T[max_ind]<T[r]:
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
        

T=[0,34,5,4,2,4,54,5,65,3,46,67]
heap_sort(T)
print(T)