# from BST import printTree
from queue import PriorityQueue
from copy import deepcopy


class BSTNode():
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.par = None
        self.data = []
        self.span = [0, 0]


def printTree(root, is_left=True, has_right=True, has_left=True, prefix="    ",):
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
        print(prefix + '└──>', root.key, " : ", root.span, " : ", root.data)
    else:
        print(prefix + '┌──>', root.key, " : ", root.span, " : ", root.data)
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


def insert(root, x):
    p = root
    q = p
    new = BSTNode(x)
    if root == None:
        return new
    while p != None:
        q = p
        if x == p.key:
            return root
        if x < p.key:
            p = p.left
        else:
            p = p.right

    if q.key > x:
        q.left = new
        new.par = q
    else:
        q.right = new
        new.par = q
    return root


def add_leaves(root):
    if root.left != None:
        add_leaves(root.left)
    else:
        new = BSTNode('leave')
        root.left = new
        new.par = root
    if root.right != None:
        add_leaves(root.right)
    else:
        new = BSTNode('leave')
        root.right = new
        new.par = root


def printData(root, A, x):
    if root == None or not root.span[0] <= x <= root.span[1]:
        return A
    if root.left != None:
        A = printData(root.left, A, x)

    for i in range(len(root.data)):
        A.put((root.data)[i])

    if root.right != None:
        A = printData(root.right, A, x)
    return A


def add_span(root):
    if root.par == None:
        root.span = [-float('inf'), float('inf')]
    else:
        if root.par.right == root:
            root.span = [root.par.key, root.par.span[1]]
        else:
            root.span = [root.par.span[0], root.par.key]

    if root.left != None:
        add_span(root.left)

    if root.right != None:
        add_span(root.right)


def boarder(root, T):
    n = len(T)
    for i in range(n):
        root = insert(root, T[i][0])
        root = insert(root, T[i][1])

    add_leaves(root)
    add_span(root)
    return root


def insert_range(root, rang, tmp):
    if root.span == tmp:
        root.data.append(rang)
        return
    if root.left != None:
        insert_range(root.left, rang, [tmp[0], min(root.key, tmp[1])])
    if root.right != None:
        insert_range(root.right, rang, [max(root.key, tmp[0]), tmp[1]])


def find_point(root, x):
    r = root
    q = r
    while r != None:
        if x == r.key:
            return r
        if r.key == 'leave':
            return r
        if x < r.key:
            r = r.left
        else:
            r = r.right


def dump_ranges(root, x):
    p = find_point(root, x)
    A = PriorityQueue()
    if p.key == x:
        A = printData(p, A, x)
    while p != None:
        A.put(p.data)
        p = p.par
    B = []
    B.append(A.get())
    while not A.empty():
        a = A.get()
        while not A.empty() and a == B[len(B)-1]:
            a = A.get()
        if a != B[len(B)-1]:
            B.append(a)
    return B


T = [[0, 10], [5, 20], [7, 12], [10, 15]]
n = len(T)
root = None
root = boarder(root, T)

for i in range(n):
    insert_range(root, T[i], T[i])
printTree(root)
print(dump_ranges(root, 10))
