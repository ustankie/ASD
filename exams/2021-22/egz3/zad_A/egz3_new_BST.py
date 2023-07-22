from egz3atesty import runtests
from copy import deepcopy


BLACK = 0
RED = 1


class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.par = None
        self.color = BLACK
        self.span = None
        self.data = []
        self.snow = 0


def printTree(root, is_left=True, has_right=True, has_left=True, prefix="    ",):
    CEND = '\033[0m'
    CRED = '\033[91m'
    CGREY = '\33[90m'
    if root.color == RED:
        COLOR = CRED
    else:
        COLOR = CGREY
    if root.right != None:
        new_prefix = deepcopy(prefix)
        if has_left:
            new_prefix += "    "
        else:
            new_prefix += "|   "
        printTree(root.right, False, False, True, new_prefix)

    if is_left:
        if root.left != None:
            print(prefix+"    |   ")
        else:
            print(prefix)
        print(prefix + COLOR + '└──>', COLOR +
              str(root.key)+CEND, root.span, root.snow)
    else:
        print(prefix + COLOR + '┌──>'+CEND, COLOR +
              str(root.key)+CEND, root.span, root.snow)
        if root.right != None:
            print(prefix+"    |   ")
        else:
            print(prefix)

    if root.left != None:
        new_prefix = deepcopy(prefix)
        if has_right:
            new_prefix += "    "
        else:
            new_prefix += "|   "
        printTree(root.left, True, True, False, new_prefix)


def insert(root, key):
    q = root
    r = root

    new = BSTNode(key)
    if root == None:
        return new, new

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
    return r, new


def l_rot(root, x):
    y = x.right
    if y == None:
        return root

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
    y = x.leftt
    if y == None:
        return root

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


def rb_insert(root, key, Non):
    r = root
    root, z = insert(root, key)
    if Non:
        z.key = None
    z.color = RED
    while z.par != None and z.par.color == RED:
        if z.par == z.par.par.right:
            y = z.par.par.left
            if y != None and y.color == RED:
                z.par.color = BLACK
                y.color = BLACK
                z.par.par.color = RED
            else:
                if z == z.par.left:
                    z = z.par
                    root = r_rot(root, z)
                z.par.color = BLACK
                z.par.par.color = RED
                root = l_rot(root, z.par.par)
        else:
            y = z.par.par.right
            if y != None and y.color == RED:
                z.par.color = BLACK
                y.color = BLACK
                z.par.par.color = RED
            else:
                if z == z.par.right:
                    z = z.par
                    root = l_rot(root, z)
                z.par.color = BLACK
                z.par.par.color = RED
                root = l_rot(root, z.par.par)
    root.color = BLACK
    return root


def setspans(root, T):
    if root == None:
        return
    if root.par == None:
        root.span = (0, T)
        # print(root.span)
    else:
        # print(root.par.key,root.par.span)
        left = root.par.span[0]
        right = root.par.span[1]
        # if root.left!=None and root.left.key!=None:
        #     left=max(left,root.left.key)
        # if root.right!=None and root.right.key!=None:
        #     right=min(right,root.right.key)
        if root.par.right == root:
            left = max(left, root.par.key)
        else:
            right = min(right, root.par.key)
        root.span = (left, right)
    setspans(root.right, T)
    setspans(root.left, T)


def add_leaves(root):
    if root.right == None:
        new = BSTNode(None)
        root.right = new
        new.par = root
    else:
        add_leaves(root.right)
    if root.left == None:
        new = BSTNode(None)
        root.left = new
        new.par = root
    else:
        add_leaves(root.left)


def insert_range(root, rang, temp):
    # print(rang,temp,root.span)
    if root.span == temp or (rang[0] == rang[1] == root.span[0] and root.right == None == root.left):
        root.data.append(rang)
    else:
        if root.right != None:
            a = max(temp[0], root.right.span[0])
            b = min(temp[1], root.right.span[1])
            if a <= b:
                insert_range(root.right, rang, (a, b))
        if root.left != None:
            a = max(temp[0], root.left.span[0])
            b = min(temp[1], root.left.span[1])
            if a <= b:
                insert_range(root.left, rang, (a, b))


def insert_snow(root, rang, temp):
    if root.span == temp or (rang[0] == rang[1] == root.span[0] and root.right == None == root.left):
        root.snow += 1
    else:
        if root.right != None:
            a = max(temp[0], root.right.span[0])
            b = min(temp[1], root.right.span[1])
            if a <= b:
                insert_snow(root.right, rang, (a, b))
        if root.left != None:
            a = max(temp[0], root.left.span[0])
            b = min(temp[1], root.left.span[1])
            if a <= b:
                insert_snow(root.left, rang, (a, b))


def LVR(root):
    if root == None:
        return 0
    s = root.snow
    return max(s+LVR(root.left), s+LVR(root.right))


def snow(I, T):
    n = len(T)

    P = []
    for i in range(n):
        if T[i][0]==T[i][1]:
            print(T[i])
        P.append(T[i][0])
        P.append(T[i][1])

    P.sort()
    # print(P)

    A = [0, P[0]]

    root = None
    # root=rb_insert(root,P[0])
    for i in range(1, 2*n):
        if P[i] != P[i-1]:
            A.append(P[i])
    A.append(I)
    #print(A)
    m = len(A)
    for i in range(m):
        root = rb_insert(root, A[i], False)

    add_leaves(root)
    setspans(root, I)
    for i in range(n):
        insert_snow(root, T[i], T[i])

    #printTree(root)
    maxi = LVR(root)
    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
T = 100
I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
print(snow(T, I))
