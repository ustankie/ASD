from random import randint
class Node():
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def create(T):
    n=len(T)
    p=Node(T[0])
    q=p
    for i in range(1,n):
        a=Node(T[i])
        p.next=a
        p=a
    return q

def wypisz(p):
    while p!=None:
        print(p.val)
        p=p.next


def left(i):return 2*i+1
def right(i):return 2*i+2
def parent(i):return (i-1)//2

def heapify(T,i,n):
    max_ind=i
    l=left(i)
    r=right(i)

    if l<n and T[l]<T[max_ind]: max_ind=l
    if r<n and T[r]<T[max_ind]: max_ind=r

    if max_ind!=i:
        T[i],T[max_ind]=T[max_ind],T[i]
        heapify(T,max_ind,n)

def build_heap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)


def SortH(p,k):
    new=Node()
    q=new
    T=[0 for i in range(k)]

    i=0
    while p!=None and i<k:
        T[i]=p.val
        p=p.next
        i+=1
    build_heap(T)
    while p!=None:
        print(T)
        a=Node(T[0])
        new.next=a
        new=a
        T[0]=p.val
        p=p.next
        heapify(T,0,k)
    for i in range(k-1,0,-1):
        print(T,i)
        a=Node(T[i])
        new.next=a
        new=a
        T[0],T[i]=T[i],T[0]
        heapify(T,0,i)

    return q.next

    

    
T=[7,4,2,6,12,8]
p=create(T)
wypisz(p)
print()

q=SortH(p,3)
wypisz(q)