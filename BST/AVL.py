from copy import deepcopy
BLACK=0
RED=1
class BSTNode():
    def __init__(self,key):
        self.key=key
        self.left=self.right=self.par=None
        self.data=None
        self.color=BLACK
        self.bf=0

def printTree(root,is_left,has_right,has_left,prefix="    ",): 
    if root.right!=None:
        new_prefix=deepcopy(prefix)
        if has_left:
            new_prefix+="    "
        else:
            new_prefix+="|   "
        printTree(root.right,False,False,True,new_prefix)

    if is_left:
        if root.left!=None:
            print(prefix+"    |   ")
        else:
            print(prefix)
        print(prefix +  '└──>',root.key," : ",root.bf)
    else:
        print(prefix  +  '┌──>',root.key," : ",root.bf)
        if root.right!=None:
            print(prefix+"    |   ")
        else:
            print(prefix)

    if root.left!=None:
        new_prefix=deepcopy(prefix)
        if has_right:
            new_prefix+="    "
        else:
            new_prefix+="|   "
        printTree(root.left,True,True,False,new_prefix)

def search(root,key):
    while root!=None:
        if root.key==key:
            return root
        elif key<root.key:
            root=root.left
        else:
            root=root.right
    return None

def RR(root,A):
    B=A.right
    p=A.par
    A.right=B.left

    if A.right!=None:
        A.right.par=A

    B.left=A
    B.par=p
    if p!=None:
        if p.left==A:
            p.left=B
        else:
            p.right=B
    else:
        root=B
    
    if B.bf==-1:
        A.bf=0
        B.bf=0
    else:
        A.bf=-1
        B.bf=1
    
    return root
def LL(root,A):
    B=A.left
    p=A.par

    A.left=B.right
    if A.left!=None:
        A.left.par=A

    B.right=A
    B.par=p

    if p!=None:
        if p.left==A:
            p.left=B
        else:
            p.right=B
    else:
        root=B
    if B.bf==1:
        A.bf=0
        B.bf=0
    else:
        A.bf=1
        B.bf=-1
    return root



def insert(root,key):
    q=root
    p=root
    new=BSTNode(key)
    if p==None:
        return new

    while p!=None:
        q=p
        if p.key>key:
            p=p.left
        else:
            p=p.right
   
    if q.key<key:
        q.right=new
    else:
        q.left=new
    new.par=q

    p=q
    if p.bf!=0:
        p.bf=0
        return root
    
    if p.left==new:
        p.bf=1
    else:
        p.bf=-1
    r=p.par
    t=False
    while r!=None:
        if r.bf!=0:
            t=True
            break
        if r.left==p:
            r.bf=1
        else:
            r.bf=-1
        p=r
        r=r.par
    if r!=None:
        print(r.key,p.key,t)
        
    else:
        print(r,p.key,t)
    if t:
        #print(r.key)
        printTree(root,True,True,True)
        if r.bf==1:
            if r.right==p:
                r.bf=0
            elif p.bf==-1:
                print("LR")
                print(r.key,p.key)
                printTree(root,True,True,True)
                root=RR(root,r.left)
                root=LL(root,r)
            else: 
                print("LL")
                root=LL(root,r.left)
        else:
            if r.left==p:
                r.bf=0
            elif p.bf==1:
                print("RL")
                print(r.right)
                root=RR(LL(root,r.right),r)
            else:
                print("RR",r.key,r.right.key) 
                root=RR(root,r.right)

    
    return root

def printBST(root):
    if root.left!=None:
        printBST(root.left)
    print(root.key)
    if root.right!=None:
        printBST(root.right)

def minimum(root):
    q=root
    while root!=None:
        q=root
        root=root.left
    return q
def maximum(root):
    q=root
    while root!=None:
        q=root
        root=root.right
    return q

def succ(x):
    if x==None:
        return x
    if x.right!=None:
        return minimum(x.right)
    q=x
    x=x.par
    while x!=None and x.right==q:
        q=x
        x=x.par

    return x
def pred(x):
    if x==None:
        return x
    if x.left!=None:
        return maximum(x.left)
    q=x
    x=x.par
    while x!=None and x.left==q:
        q=x
        x=x.par
    return x

#A=[23, 3, 26, 11, 4, 2, 28, 9 ,7 ,10, 5, 18, 20, 21, 12, 15, 25, 17, 30, 6 ,29 ,19, 16, 14, 22, 13, 1, 24, 31, 32, 8, 27]
A=[3 ,23, 12, 2, 17, 27, 24, 31, 13, 6, 10, 15, 16, 1, 8]
#A=[20,17,5,27,30,35,19,18,17,40,50,100,28]
n=len(A)
print("len(A): ",n)
root=None
for i in range(n):
    root =insert(root,A[i])
    #printTree(root,True,True,True)
    #print("\n\n\n")
# printTree(root,True,True,True)
# a=search(root,35)
# root=RR(root,a)
# a=search(root,19)
# root=LL(root,a)
printTree(root,True,True,True)
printBST(root)
