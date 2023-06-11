from collections import deque
class Node():
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class stack():
    def __init__(self):
        self.head=Node("head")
        self.size=0
    def empty(self):
        return self.size==0
    def push(self,val):
        n=Node(val)
        n.next=self.head.next
        self.head.next=n
        self.size+=1
    def pop(self):
        p=self.head.next
        self.head.next=self.head.next.next
        self.size-=1
        return p.val
def partition(T,p,r):
    x=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i
    
def qs_stack(T,p,r):
    s=stack()
    s.push((p,r))
    while not s.empty():
        p,r=s.pop()
        if p<r:
            q=partition(T,p,r)
            if (q-p)<(r-q):
                s.push((q+1,r))
                s.push((p,q-1))
            else:
                s.push((p,q-1))
                s.push((q+1,r))

s=stack()
s.push(2)
s.push(3)
s.push(5)
T=[1,2,53,2,0,6,7,22,54,67]
qs_stack(T,0,len(T)-1)
print(T)    