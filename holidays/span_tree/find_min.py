
from math import log2
# class Node():
#     def __init__(self,val):
#         self.val=val
#         self.right=self.left=self.par=None

def find_min(T,rang):
    n=len(T)
    _n=1<<(1+int(log2(n-1)))
    
    ST=[float('inf') for i in range(2*_n)]

    for i in range(n):
        ST[i+_n]=T[i]

    for i in range(_n-1,0,-1):
        ST[i]=min(ST[2*i],ST[2*i+1])


    def update(i,x):
        i+=_n
        ST[i]=x
        i//=2
        while i>0:
            ST[i]=min(ST[2*i],ST[2*i+1])
            i//=2
            
    def range_min(a,b):
        a+=_n
        b+=_n
        mini=float('inf')
        while a<=b:
            print(mini,a,b)
            if a%2==1:
                mini=min(mini,ST[a])
                a+=1
            if b%2==0:
                mini=min(mini,ST[b])
                b-=1
            a//=2
            b//=2
            
        return mini
    
    mini1=range_min(rang[0],rang[1])
    update(5,-1)
    mini2=range_min(rang[0],rang[1])
    return mini1,mini2

T=[0,7,5,3,1,8,6,12,3]
rang=[1,6]

print(find_min(T,rang))
