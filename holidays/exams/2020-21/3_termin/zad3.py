from zad3testy import runtests
from math import log2
class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.right   = None  # prawe poddrzewo
    self.parent  = None  # rodzic drzewa jesli istnieje
    self.key     = None  # klucz

def maxim( T, C ):
    m=len(C)
    maxi=-float('inf')

    for c in C:
        if c%2==0:
            a=c+1
        else:
            a=c
        c_=1<<(1+int(log2(a)))

        p=T
        lim=c_//2+c_//4
        while c_>2:
            if lim<=c:
                p=p.right
                c-=c_//2
            else:
                p=p.left
                c-=c_//4

            c_//=2
            lim=c_//2+c_//4

        maxi=max(maxi,p.key)
    return maxi

def findplace_(p,d):
    if p.left == None or p.right == None:
        return d, p
    g1, p1 = findplace_(p.left, d+1)
    g2, p2 = findplace_(p.right, d+1)
    if p1 == None:
        return g2, p2
    if p2 == None:
        return g1, p1
    if g1 <= g2:
        return g1, p1
    return g2, p2
               
def CreateTree_(C):
  x = Node()
  x.key = C[0]
  for i in range (1, len(C)):
    d, p = findplace_(x, 1)
    n = Node()
    n.parent = p
    n.key = C[i]
    if p.left == None:
        p.left = n
    else:
        p.right = n
  return x  
    
runtests( maxim )

T=[5,2,3,1,0,8,15]
C=[3,4,6]
T=[34,12,22,11,0,-5,17,22,33,44,45,21,13,14,15]
C=[2, 4, 5, 8, 9]

p=CreateTree_(T)
print(maxim(p,C))



