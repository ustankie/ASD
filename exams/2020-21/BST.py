from copy import deepcopy
class BSTNode():
    def __init__(self,key):
        self.key=key
        self.left=self.right=self.par=None
        self.data=None

def printTree(root,is_left=True,has_right=True,has_left=True,prefix="    ",): 
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
        print(prefix +  '└──>',root.key)
    else:
        print(prefix  +  '┌──>',root.key)
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
    if root==None:
        
        return new

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
    return r

def printBST(root):
    if root==None:
        return    
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
    
# A=[20,17,5,27,30,35,19,18,17,40,50,100]
# #A=[3 ,23, 12, 2, 17, 27, 24, 31, 13, 6, 10, 15, 16, 1, 8]
# n=len(A)
# print("len(A): ",n)
# root=None
# for i in range(n):
#     root =insert(root,A[i])
# printBST(root)
# print()
# a=search(root,40)
# q=maximum(root)
# #print(a.key)
# #print(a.par.key,a.right.key)
# # print(succ(a).key)
# # print(pred(a))
# # printTree(root,False,True,True)
# # root=remove(root,17)
# # root=remove(root,17)
# # print()
# # printBST(root)

# printTree(root,False,True,True)

# #printBST(a)
# #print("\n",a.key,a.right.right.key,a.left)

