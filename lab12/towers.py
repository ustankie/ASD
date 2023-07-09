class Node():
    def __init__(self):
        self.T=[]
        self.next=None
        self.prev=None
        self.height=None

def print_list(p):
    p=p.next
    while p!=None:
        print(p.T,p.height)
        p=p.next

def towers(A):
    n=len(A)
    C=[]
    # all=[]

    all=[]
    p=Node()

    A[0].sort(reverse=True)
    child=Node()
    child.T=A[0]
    child.height=sum(A[0])
    for i in range(1,n):
        all.append((sum(A[i]),i))

    all.sort(key=lambda x: x[0])

    for i in range(n-1):
        a=Node()
        A[all[i][1]].sort()
        a.T=A[all[i][1]]
        a.height=all[i][0]
        if p.next!=None:
            p.next.prev=a
        a.next=p.next
        p.next=a
        a.prev=p
    
    print_list(p)
    print()

    k=p
    while p.next!=None and child.height<=p.next.height:
        k=p
        k=k.next
        best=0
        win=float('inf')
        print(child.height)

        while k!=None:
            if k==p.next and k.next!=None and k.height>0 and k.next.height>k.height-k.T[len(k.T)-1]:
                s= k.next.height
            elif k==p.next and k.height>0:
                s=k.height-k.T[len(k.T)-1]
            else:
                s=p.next.height
            if k.height>0 and win>s-(child.height+k.T[len(k.T)-1]):
                win=s-child.height-k.T[len(k.T)-1]
                best=k.T[len(k.T)-1]
            k=k.next
        k=p
        k=k.next
        if k.next!=None and k.height>0 and k.next.height>k.height-k.T[len(k.T)-1]:
            s= k.next.height
        else:
            s=k.height-k.T[len(k.T)-1]

        while k!=None and not (k.height>0 and win==s-(child.height+k.T[len(k.T)-1])):

            s=p.next.height
            
            k=k.next
        k.T.pop()
       
        k.height-=best
        child.height+=best
        C.append(best)

        while k.next!=None and k.height<k.next.height:
            k.prev.next=k.next
            k.next.prev=k.prev
            d=k.next
            k.prev=k.next
            k.next=k.next.next
            d.next=k
            
        print_list(p)        
        print() 
        

    return C








W0 = [2.5, 3.5]


W1 = [4] * 8
W2 = [10]
W3 = [10, 6]
W4 = [2.75] * 6
W5 = [4, 6, 2]
A = (W0,W1, W2, W3, W4, W5)





print(towers(A))

