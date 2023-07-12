class Node():
    def __init__(self,val,children=[]):
        self.val=val
        self.children=children

def update_max_paths(max_paths, child_max):
    # Try to replace the lower value at first (we want to
    # maximize a sum of both paths' values so we have to get rid
    # of the lower one at first)
    if max_paths[0] > max_paths[1] and child_max > max_paths[1]:
        max_paths[1] = child_max
    elif child_max > max_paths[0]:
        max_paths[0] = child_max
        
        
def max_path(root):
    global_max = float('-inf')
    
    def recur(node):
        nonlocal global_max
        
        max_paths = [0, 0]
        for child in node.children:
            child_max = recur(child)
            update_max_paths(max_paths, child_max)
        
        global_max = max(global_max, node.val + sum(max_paths))
        # curr_max will be a single line straight path (thet means each next
        # node of a path will be deeper in a tree than the previous one)
        curr_max   = max(0, node.val + max(max_paths))
        return curr_max
        
    recur(root)
    
    return global_max

def tree1(root):
    print(root.val)
    
    def recur(u,sum):
        #sum=sum
        if len(u.children)==0:
            return sum+u.val
        a=0

        for i in range(len(u.children)):
            v=u.children[i]
            
            if v!=None:
                c=(recur(v,sum))
                if c>a:
                    a=c
                    if len(u.children)>1:
                        u.children[i]=None

        return a+u.val

    a=recur(root,0)
    print(a)
    b=recur(root,0)
    print(b)
    return a+b

def tree(root):
    print(root.val)
    
    def recur(u,sum1,sum2):
        #sum=sum
        if len(u.children)==0:
            return sum1+u.val,sum2+u.val
        a=0
        b=0
        for i in range(len(u.children)):
            v=u.children[i]
            c=(recur(v,sum1,sum2))

            # if c[0]>a:
            #     b=a
            #     a=c[0]
            # # if c[1]>a:
            # #     b=a
            # #     a=c[1]

            if a>b and c[0]>b:
                b=c[0]
            elif c[0]>a:    
                a=c[0]


        return a+u.val,b

    a=recur(root,0,0)
    print(a)
    # b=recur(root,0)
    # print(b)
    return a[0]+a[1]
root = Node(20, [
    Node(5, [
        Node(30), 
        Node(-20)
    ]), 
    Node(-20, [
        Node(1, [
            Node(30), 
            Node(22),
            Node(-15)
        ]), 
    ]), 
    Node(15),
    Node(-10, [
        Node(18),
        Node(23),
        Node(-20, [
            Node(100)
        ]),
        Node(-15)
    ])
])

print(tree1(root.children[0 ]))

print(max_path(root.children[0]))

