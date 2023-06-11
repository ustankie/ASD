
class Node():
    def __init__(self, val=None,next=None):
        self.val=val
        self.next=next

def wypisz(p):
    while p!=None:
        print(p.val)
        p=p.next

def create(T,p):
    n=len(T)
    q=p
    p.val=(T[0])

    for i in range(1,n):
        a=Node(T[i])
        p.next=a
        p=a
def k_lists(T):
    k=len(T)
    L=[0 for _ in range(k)]
    for i in range(k):
        L[i]=Node()
        p=L[i]
        create(T[i],p)
    return L
def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2

def heapify(L,i,n):
    max_ind=i
    l=left(i)
    r=right(i)
    if L[i]==None:
        if l<n and L[l]!=None:
            max_ind=l
        elif r<n:
            max_ind=r
    if l<n  and L[l]!=None and L[l].val <L[max_ind].val:
        max_ind=l
    if r<n and L[r]!=None and L[r].val<L[max_ind].val:
        max_ind=r
    if max_ind!=i:
        L[max_ind],L[i]=L[i],L[max_ind]
        heapify(L,max_ind,n)

def build_heap(L):
    n=len(L)
    for i in range(n-1,-1,-1):
        heapify(L,i,n)
        # for i in range(n):
        #     print(L[i].val)
        # print()

def sort_lists(L):
    n=len(L)
    build_heap(L)
    p=L[0]
    q=p
    L[0]=L[0].next
    for i in range(n):
        print(L[i].val)
    print()
    wypisz(p)
    heapify(L,0,n)

    while L[0]!=None:
        p.next=L[0]
        L[0]=L[0].next
        p=p.next
        heapify(L,0,n)
    return q



    





p=Node()
T=[[0,1,2,3,4,5,23,4436,6545,6766],[123,1245,4654],[0,2,3,6,8,33],[1,23,54,54,75,93,505,4000]]
k=len(T)
L=k_lists(T)
# for i in range(k):
#     print(L[i].val)
# print()
p=sort_lists(L)
print("a\n")
wypisz(p)
