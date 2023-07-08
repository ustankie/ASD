from zad2testy import runtests
from math import ceil,sqrt

class Node():
    def __init__(self,val):
        self.val=val
        self.par=self
        self.rank=0

def findset(x):
    if x.par!=x:
        x.par=findset(x.par)
    return x.par

def union(x,y):
    x=findset(x)
    y=findset(y)

    if x!=y:
        if x.rank>y.rank:
            y.par=x
        else:
            x.par=y
            if x.rank==y.rank:
                y.rank+=1
def DFS(G):
    def rec(u):
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                rec(v)

    n=len(G)
    vis=[False for _ in range(n)]
    
    k=0
    for i in range(n):
        if not vis[i]:
            if k==1:
                return False
            k=1
            vis[i]=True
            rec(i)
    return True

def create(A):
    n=len(A)
    G=[]
    for i in range(n):
        for j in range(n):
            if i!=j:
                G.append(((i,j),ceil(sqrt((A[i][0]-A[j][0])*(A[i][0]-A[j][0])+(A[i][1]-A[j][1])*(A[i][1]-A[j][1])))))
                
    return G    

def convert(E,p,n,j):
    m=len(E)
    G=[[]for _ in range(n)]
    for i in range(p,p+j):
        #print(E[i][0][0],E[i][0][1])
        #print(i)
        G[E[i][0][0]].append(E[i][0][1])
        G[E[i][0][1]].append(E[i][0][0])
    return G


def highway(A):
    n=len(A)
    E=create(A)

    E.sort(key=lambda x:x[1])
    print(E)
    m=len(E)
    minimum=float('inf')
    for j in range(n-1,m):
        for i in range(m-j):
            G=convert(E,i,n,j)
            #print(*G,sep="\n")
            if DFS(G):               
                minimum=min(minimum,E[i+j][1]-E[i][1]) 
    return minimum
def highway2(A):
    n=len(A)
    E=create(A)

    E.sort(key=lambda x:x[1])
    V=[Node(i)for i in range(n)]
    A=[]
    min_diff=float('inf')
    Flag=True
    while Flag:
        A=[]
        Flag=False
        V=[Node(i)for i in range(n)]
        for e in E:
            k,c=e
            #print(k)
            u,v=k

            if findset(V[u])!=findset(V[v]):
                union(V[u],V[v])
                A.append(c)
                Flag=True
        Flag2=True
        for i in range(1,n):
            if findset(V[i])!=findset(V[i-1]):
                Flag2=False
        if Flag2:
            min_diff=min(min_diff,A[len(A)-1]-A[0])
        if len(E)>0:
            E=E[::-1]
            E.pop()
            E=E[::-1]
            print(E)

    print(A)
    return min_diff
    





runtests(highway2)
A = [(10, 10), (15, 25), (20, 20), (30, 40)]
print(highway2(A))
