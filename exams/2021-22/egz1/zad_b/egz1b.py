from egz1btesty import runtests
from copy import deepcopy
from egz1btest_spec import gentest,my_randint,MY_random,TEST_SPEC
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

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
        print(prefix +  '└──>',root.x)
    else:
        print(prefix  +  '┌──>',root.x)
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

def tree_to_graph(T):
    def LVR(root):
        nonlocal count
        count+=1
        if root.left!=None:
            LVR(root.left)
        if root.right!=None:
            LVR(root.right)
    def LVR2(root):
        nonlocal count
        count+=1
        a=count-1
        L[a]=root
        h[d[a]]+=1
        #print(count)
        if root.left!=None:
            A[count-1].append(count)
            A[count].append(count-1)
            d[count]=d[count-1]+1
            LVR2(root.left)
        if root.right!=None:
            A[a].append(count)
            A[count].append(a)
            d[count]=d[a]+1
            LVR2(root.right)
    count=0
    LVR(T)
    n=count
    A=[[]for _ in range(n)]
    d=[0 for _ in range(n)]
    L=[None for _ in range(n)]
    h=[0 for _ in range(n)]

    count=0

    LVR2(T)
    return A,d,L,h

def count_None(T):
    def LVR(root):
        nonlocal count
        if root.x==None:
            count+=1
            return
        if root.left!=None:
            LVR(root.left)
        if root.right!=None:
            LVR(root.right)
    count=0
    LVR(T)
    return count
def wideentall( T ):

    A,d,L,h=tree_to_graph(T)
    # print(A)
    # print(d)
    # print(*L,sep="\n")
    # print(h)
    n=len(h)
    max_node=0
    max_ind=0
    for i in range(n):
        if h[i]>=max_node:
            max_node=h[i]
            max_ind=i

    for i in range(n-1,-1,-1):
        if d[i]==max_ind:
            L[i].x=True
        if L[i].x:
            for v in (A[i]):
                if v<i:
                    L[v].x=True
    

    #printTree(T,True,True,True)
    return max(0,count_None(T))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )

A0=[0,1,2,3,4,10,22]
A=[0,1,2,3,4,5,10]

B=(gentest(1,A,0))[0]
printTree(B,True,True,True)

print(wideentall(B))