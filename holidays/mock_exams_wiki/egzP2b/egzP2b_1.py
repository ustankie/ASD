from egzP2btesty import runtests
from math import log10

class Node():
    def __init__(self,key):
        self.key=key
        self.left=self.right=None
        self.num=1
    
def insert(root,key):
    k=len(key)
    q=root
    for i in range(k-1,-1,-1):
        if key[i]=='0':
            if q.left==None:
                q.left=Node('0'+q.key)
            else:
                q.left.num+=1
            q=q.left
        else:
            if q.right==None:
                q.right=Node('1'+q.key)
            else:
                q.right.num+=1
            q=q.right            

def LVR(root):
    if root!=None:  
        print(root.key,root.num)
        LVR(root.right)
        LVR(root.left)

def search(root,key):
    n=len(key)
    i=0
    while root!=None:
        if root.key==key:
            return root.num
        elif key[n-i-1]=='0':
            root=root.left
        else:
            root=root.right
        i+=1
    
    return 0

def kryptograf( D, Q ):
    n=len(D)
    root=Node('')
    root.num=n
    for i in range(n):
        insert(root,D[i])
  
    
    count=1
    m=len(Q)
    for i in range(m):
        curr=search(root,Q[i])
        if curr:
            count*=curr

    return log10(count)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)

D=  ['0', '100', '1100', '1101', '1111']
Q=  ['', '1', '11', '0', '1101']
print(kryptograf(D,Q))