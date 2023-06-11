from random import randint
from math import log

def binary_search(T,p,r,x):
    if p>r:
        return None
    n=r-p

    if n==0:
        if T[p][0]==x:
            return p
        else:
            return None
    q=n//2 +p

    if T[q][0]==x:
        return q
    if T[q][0]<x:
        return binary_search(T,q+1,r,x)
    else:
        return binary_search(T,p,q-1,x)

def insert(T,v,k):
    j=k
    while j>0 and T[j-1][0]>v:
        T[j][0]=T[j-1][0]
        T[j][1]=T[j-1][1]
        j-=1

    T[j][0]=v
    T[j][1]=1

def sort_logn(T):
    n=len(T)
    S=[[None,None] for _ in range(n)]
    R=[0 for _ in range(n)]
    k=0
    for i in range(n):
        
        if k>0:
            x=binary_search(S,0,k-1,T[i])
            if x!=None:
                S[x][1]+=1
            else:
                insert(S,T[i],k)
                k+=1
        else:
                insert(S,T[i],k)
                k+=1


    for i in range(1,k):
        S[i][1]+=S[i-1][1]          
    for i in range(n):
        x=binary_search(S,0,k-1,T[i])
        R[S[x][1]-1]=T[i]
        S[x][1]-=1
    for i in range(n):
        T[i]=R[i]         


n=60

T1=[randint(0,int(log(n))) for i in range(n)]
T3=[randint(1,3) for i in range(20)]
T2=[1,1,2,1,2]
print(T1)
sort_logn(T1)
print()
print(T1)