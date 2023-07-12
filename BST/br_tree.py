from copy import deepcopy
RED = 0
BLACK = 1


class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.par = None
        self.data = None
        self.color = BLACK

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



def search(root, key):
    # print(root,key)
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def minimum(root):
    q = root
    while root != None:
        q = root
        root = root.left
    return q


def maximum(root):
    q = root
    while root != None:
        q = root
        root = root.right
    return q


def succ(x):
    if x == None:
        return x
    if x.right != None:
        return minimum(x.right)
    q = x
    x = x.par
    while x != None and x.right == q:
        q = x
        x = x.par

    return x


def pred(x):

    if x == None:
        return x
    if x.left != None:
        return maximum(x.left)
    q = x
    x = x.par
    while x != None and x.left == q:
        q = x
        x = x.par
    return x


def insert(root, key):
    q = root
    r = root
    new = BSTNode(key)
    if root == None:

        return new,new

    while root != None:
        q = root
        if root.key > key:
            root = root.left
        else:
            root = root.right

    if q.key < key:
        q.right = new
    else:
        q.left = new
    new.par = q
    return r,new


def l_rot(root, x):
    y = x.right
    if y == None:
        return
    y.par = x.par
    if x.par == None:
        root = y
    elif x == x.par.right:
        x.par.right = y
    else:
        x.par.left = y

    x.right = y.left
    if x.right != None:
        x.right.par = x
    y.left = x
    x.par = y
    return root


def r_rot(root, x):
    y = x.left
    if y == None:
        return
    y.par = x.par
    if x.par == None:
        root = y
    elif x == x.par.right:
        x.par.right = y
    else:
        x.par.left = y

    x.left = y.right
    if x.left != None:
        x.left.par = x
    y.right = x
    x.par = y
    return root


def rb_insert(root, key):
    r = root
    root,z = insert(root, key)
    z.color = RED
    #print(root,z)

    while z.par != None and z.par.color == RED:
        if z.par == z.par.par.right:
            y = z.par.par.left
            if y != None and y.color == RED:
                z.par.color = BLACK
                y.color = BLACK
                z.par.par.color = RED
                z = z.par.par
            else:
                if z == z.par.left:
                    z = z.par
                    root=r_rot(root, z)
                z.par.color = BLACK
                z.par.par.color = RED
                root = l_rot(root, z.par.par)
        else:
            y = z.par.par.right
            if y != None and y.color == RED:
                z.par.color = BLACK
                y.color = BLACK
                z.par.par.color = RED
                z = z.par.par
            else:
                if z == z.par.right:
                    z = z.par
                    root=l_rot(root, z)
                z.par.color = BLACK
                z.par.par.color = RED
                root = r_rot(root, z.par.par)

        #print(root)
    root.color = BLACK
    return root

A=[20,17,5,27,30,35,19,18,17,40,50,100]
#A=[3 ,23, 12, 2, 17, 27, 24, 31, 13, 6, 10, 15, 16, 1, 8]
n=len(A)
print("len(A): ",n)
root=None
for i in range(n):
    root =rb_insert(root,A[i])
printTree(root)