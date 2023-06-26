def left(i):return 2*i+1
def right(i):return 2*i+2
def par(i):return (i-1)//2
def heapify(A,i,n):
    max_ind=i
    l=left(i)
    r=right(i)
    if l<n and A[max_ind]<A[l]:max_ind=l
    if r<n and A[max_ind]<A[r]:max_ind=r
    if max_ind!=i:
        A[max_ind],A[i]=A[i],A[max_ind]
        heapify(A,max_ind,n)

def build_heap(A):
    n=len(A)
    for i in range(n-1,-1,-1):
        heapify(A,i,n)

def heapsort(A):
    n=len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i)
    

A=[0,24,5,-1,3,43]
heapsort(A)
print(A)