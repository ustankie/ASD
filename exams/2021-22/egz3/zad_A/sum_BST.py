from egz3atesty import runtests
from copy import deepcopy


BLACK=0
RED=1

class BSTNode():
    def __init__(self,key):
        self.key=key
        self.left=self.right=self.par=None
        self.color=BLACK
        self.span=None
        self.data=[]
        self.snow=0

def printTree(root,is_left=True,has_right=True,has_left=True,prefix="    ",): 
    CEND = '\033[0m'
    CRED = '\033[91m'
    CGREY    = '\33[90m'
    if root.color==RED:
        COLOR=CRED
    else:
        COLOR=CGREY
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
        print(prefix + COLOR+  '└──>',COLOR+str(root.key)+CEND,root.span,root.snow)
    else:
        print(prefix  + COLOR+ '┌──>'+CEND,COLOR+str(root.key)+CEND,root.span,root.snow)
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

def insert(root,key):
    q=root
    r=root

    new=BSTNode(key)
    if root==None:
        return new,new
    
    while root!=None:
        q=root
        if root.key>key:
            root=root.left
        else:
            root=root.right
    if q.key<key:
        q.right=new
    else:
        q.left=new
    
    new.par=q
    return r,new

def l_rot(root,x):
    y=x.right
    if y==None:
        return root
    
    y.par=x.par

    if x.par==None:
        root=y
    elif x==x.par.right:
        x.par.right=y
    else:
        x.par.left=y
    
    x.right=y.left

    if x.right!=None:
        x.right.par=x

    y.left=x
    x.par=y

    return root


def r_rot(root,x):
    y=x.left
    if y==None:
        return root
    
    y.par=x.par

    if x.par==None:
        root=y
    elif x==x.par.right:
        x.par.right=y
    else:
        x.par.left=y
    
    x.left=y.right

    if x.left!=None:
        x.left.par=x

    y.right=x
    x.par=y

    return root

def rb_insert(root,key,Non):
    r=root
    root,z=insert(root,key)
    if Non:
        z.key=None
    z.color=RED
    while z.par!=None and z.par.color==RED:
        if z.par==z.par.par.right:
            y=z.par.par.left
            if y!=None and y.color==RED:
                z.par.color=BLACK
                y.color=BLACK
                z.par.par.color=RED
            else:
                if z==z.par.left:
                    z=z.par
                    root=r_rot(root,z)
                z.par.color=BLACK
                z.par.par.color=RED
                root=l_rot(root,z.par.par)
        else:
            y=z.par.par.right
            if y!=None and y.color==RED:
                z.par.color=BLACK
                y.color=BLACK
                z.par.par.color=RED
            else:
                if z==z.par.right:
                    z=z.par
                    root=l_rot(root,z)
                z.par.color=BLACK
                z.par.par.color=RED
                root=l_rot(root,z.par.par)
    root.color=BLACK
    return root,z

    
def insert_range(root,rang,temp):
    #print(rang,temp,root.span)
    if root.span==temp or   (rang[0]==rang[1]==root.span[0] and root.right==None==root.left):
        root.data.append(rang)
    else:
        if root.right!=None:
            a=max(temp[0],root.right.span[0])
            b=min(temp[1],root.right.span[1])
            if a<=b:
                insert_range(root.right,rang,(a,b))
        if root.left!=None:
            a=max(temp[0],root.left.span[0])
            b=min(temp[1],root.left.span[1])
            if a<=b:
                insert_range(root.left,rang,(a,b))
def insert_snow(root,rang,temp):
    if root.span==temp or   (rang[0]==rang[1]==root.span[0] and root.right==None==root.left):
        root.snow+=1
    else:
        if root.right!=None:
            a=max(temp[0],root.right.span[0])
            b=min(temp[1],root.right.span[1])
            if a<=b:
                insert_snow(root.right,rang,(a,b))
        if root.left!=None:
            a=max(temp[0],root.left.span[0])
            b=min(temp[1],root.left.span[1])
            if a<=b:
                insert_snow(root.left,rang,(a,b))
def LVR(root):
    if root==None:
        return 0
    s=root.snow
    return max(s+LVR(root.left),s+LVR(root.right))
def sum_BST( root ):
    def rec(root):
        if root==None:
            return 0
        s=root.key
        return (rec(root.right)+rec(root.left))+s
    while root.par!=None:
        root=root.par
    return rec(root)





import random


vals = list(set([random.randint(0, 20) for _ in range(10)]))
random.shuffle(vals)

t=None
A=[]
for n in vals:
    t,new=rb_insert(t,n,False)
    A.append(new)
    
print('Tree keys:')
print()
print('Expected sum:', sum(vals))
print('Calculated sum:', sum_BST(A[5]))