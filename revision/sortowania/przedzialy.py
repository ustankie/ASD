def left(i):return 2*i+1
def right(i):return 2*i+2
def par(i):return (i-1)//2
def heapify(A,i,n,k):
    max_ind=i
    l=left(i)
    r=right(i)
    if l<n and (A[l][k]>A[max_ind][k] or (A[l][k]==A[max_ind][k] and A[l][1-k]<A[max_ind][1-k])):max_ind=l
    if r<n and (A[r][k]>A[max_ind][k] or (A[r][k]==A[max_ind][k] and A[r][1-k]<A[max_ind][1-k])):max_ind=r
    if max_ind!=i:
        A[max_ind],A[i]=A[i],A[max_ind]
        heapify(A,max_ind,n,k)
def build_heap(A,k):
    n=len(A)
    for i in range(n-1,-1,-1):
        heapify(A,i,n,k)

def heap_sort(A,k):
    n=len(A)
    build_heap(A,k)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i,k)
def binsearch(A,i,j,x):
    if i<=j:
        q=(i+j)//2
        if A[q]==x:
            while q<=j and A[q]==x:
                q+=1
            return q-1
        if A[q][1]>x[1] or (A[q][1]==x[1] and A[q][0]<x[0]):
            return binsearch(A,i,q-1,x)
        else:
            return binsearch(A,q+1,j,x)
def span(T):
    n=len(T)
    L=T[:]
    R=T[:]
    heap_sort(L,0)
    heap_sort(R,1)
    print(L)
    print(R)
    #L=L[::-1]
    #print(binsearch(L,0,n-1,[1,2]))
    max_span=0
    max_ind=0
    for i in range(n):
        x=binsearch(R,0,n-1,L[i])-i
        if max_span<x:
            max_span=x
            max_ind=i
    return max_span,L[max_ind]


    #for i in range(n):

# A=[0,24,5,-1,3,43]
# heap_sort(A)
# print(A)

T = [[1,2],[2,4],[1,9],[1,5],[1,4],[1,7],[2,8],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[16,17]]
print(len(T))
print(span(T))