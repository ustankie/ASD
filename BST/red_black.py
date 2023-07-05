from copy import deepcopy
BLACK=0
RED=1
class BSTNode():
    def __init__(self,key=None):
        self.key=key
        self.left=self.right=self.par=None
        self.data=None
        self.color=RED
sentinel=BSTNode()
sentinel.color=BLACK
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
        print(prefix + COLOR+  '└──>',COLOR+str(root.key)+CEND)
    else:
        print(prefix  + COLOR+ '┌──>'+CEND,COLOR+str(root.key)+CEND)
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

def remove(root,key):
    find=search(root,key)
    if find==None:
        return root
    x=find
    if find.right!=None and find.left!=None:
        x=succ(find)

    if x.right==None:
        y=x.left
    else:
        y=x.right

    if y!=None:
        y.par=x.par

    if x.par==None:
        root=y
    elif x==x.par.left:
        x.par.left=y
    else:
        x.par.right=y
    
    if find!=x:
        find.key=x.key
    return root


def search(root,key):
    #print(root,key)
    while root!=None:
        if root.key==key:
            return root
        elif key<root.key:
            root=root.left
        else:
            root=root.right
    return None
def insert(root,key):
    q=root
    r=root
    new=BSTNode(key)
    new.left=new.right=sentinel
    if root==sentinel:
        root=new
        return root,new

    while root!=sentinel:
        q=root
        #print(root,sentinel)
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
def rot_L(root,A,B):
    p=A.par
    B=A.right
    if B==sentinel:
        return root
    
    A.right=B.left

    if A.right!=None:
        A.right.par=A
    B.left=A
    B.par=p
    A.par=B

    if p!=sentinel:
        if p.right==A:
            p.right=B
        else:
            p.left=B
    else:
        root=B
    return root
def rot_R(root,A,B):
    p=A.par
    B=A.left
    if B==sentinel:
        return root

    A.left=B.right
    if A.left!=None:
        A.left.par=A

    B.right=A
    A.par=B
    B.par=p
    if p!=sentinel:
        if p.right==A:
            p.right=B
        else:
            p.left=B
    else:
        root=B
    return root

def insert_rb(root,key):
    root,new=insert(root,key)
    #printTree(root,True,True,True)

    if root==new:
        new.color=BLACK
        return root
    while new!=root and new.par.color==RED:
        # if new.par.color==BLACK:
        #     return root
        
        B=new.par
        A=B.par

        if A.left==B:
            C=A.right
        else:
            C=A.left
        

        if C!=None and C.color==RED:
            C.color=BLACK
            A.color=RED
            B.color=BLACK
            new=A
            # if root==A:
            #     A.color=BLACK

            # return root
        elif C==None:
            A.color=RED
            B.color=BLACK

            # if root==A:
            #     A.color=BLACK

            #return root
        else:
            if A.left==B:
                if B.right==new:

                    root=rot_L(root,B,new)                
                    new=new.par
                    B=new.par
                    A=B.par
                    #new=B
                                
                B.color=BLACK
                A.color=RED
                root=rot_R(root,A,B)
            else:
                if B.left==new:

                    root=rot_R(root,B,new)                
                    new=new.par
                    B=new.par
                    A=B.par
                    #new=B


                B.color=BLACK
                A.color=RED
                root=rot_L(root,A,B)
    root.color=BLACK
    return root
    

def printBST(root):
    CEND = '\033[0m'
    CRED = '\033[91m'
    CGREY    = '\33[90m'
    if root.color==RED:
        COLOR=CRED
    else:
        COLOR=CGREY
    if root==None:
        return    
    if root.left!=None:
        printBST(root.left)
    print(COLOR+str(root.key)+CEND)
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
    
A=[20,17,5,27,30,35,19,18,17,40,50,100]
A=[3 ,23, 12, 2, 17, 27, 24, 31, 13, 6, 10, 15, 16, 1, 8]
A=[18, 10, 2, 13 ,3 ,5, 29, 9 ,30 ,6 ,19, 28 ,26 ,25 ,21, 7]
n=len(A)
print("len(A): ",n)
root=sentinel
for i in range(n):
    root =insert_rb(root,A[i])
    printTree(root,False,True,True)
    #printBST(root)
    #print()
printBST(root)
print()
a=search(root,40)
q=maximum(root)
#print(a.key)
#print(a.par.key,a.right.key)
# print(succ(a).key)
# print(pred(a))
# printTree(root,False,True,True)
# root=remove(root,17)
# root=remove(root,17)
# print()
# printBST(root)

printTree(root,False,True,True)

#printBST(a)
#print("\n",a.key,a.right.right.key,a.left)

