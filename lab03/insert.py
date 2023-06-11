def heapify(T,i,n):
    n=len(T)
    r=right(i)
    l=left(i)
    max_ind=i
    if l<n and T[l]>T[max_ind]: max_ind=l
    if r<n and T[r]>T[max_ind]: max_ind=r
    if max_ind!=i:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify(T,max_ind,n)


def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2

class Heap():
    def __init__(self,n):
        self.T=[0 for _ in range(n)]
        self.size=0
def insert(H,el):
    H.T[H.size]=el
    p=parent(H.size)
    q=H.size
    H.size+=1
    while p>=0 and H.T[q]>H.T[p]:
        H.T[p],H.T[q]=H.T[q],H.T[p]
        q=p
        p=parent(q)
        

def build(T,H):
    n=len(T)
    for i in range(n):
        insert(H,T[i])
    for i in range(n):
        print(H.T[i])
  
T=[1,2,53,2,0,6,7,22,54,67]
H=Heap(100)
build(T,H)