
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
        ST[i]=(ST[2*i]+ST[2*i+1])


    def update(i,x):
        i+=_n
        ST[i]=x
        i//=2
        while i>0:
            ST[i]=(ST[2*i]+ST[2*i+1])
            i//=2
            
    def range_sum(a,b):
        a+=_n
        b+=_n
        sum=0
        while a<=b:
            #print(mini,a,b)
            if a%2==1:
                sum+=ST[a]
                a+=1
            if b%2==0:
                sum+=ST[b]
                b-=1
            a//=2
            b//=2
            
        return sum
    
    sum1=range_sum(rang[0],rang[1])
    update(5,-1)
    sum2=range_sum(rang[0],rang[1]) 
    T[5]=-1
    A1=T[rang[0]:rang[1]+1]
   
    sum3=sum(A1)
    return sum1,sum2,sum3

T=[0,7,5,3,1,8,6,12,3]
rang=[1,6]

print(find_min(T,rang))
