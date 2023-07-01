from egzP3btesty import runtests 
from queue import PriorityQueue
class Node():
    def __init__(self,val):
        self.par=self
        self.rank=0
        self.val=val
def findset(x):
    if x.par!=x:
        x.par=findset(x.par)
    return x.par
def union(x,y):
    x=findset(x)
    y=findset(y)
    if x.rank>y.rank:
        y.par=x
    else:
        x.par=y
        if x.rank==y.rank:
            y.rank+=1

def graph_to_edges(G):
    n=len(G)
    E=[]
    sum=0
    for i in range(n):
        for j in range(len(G[i])):
            if i<G[i][j][0]:
                E.append((i,G[i][j][0],G[i][j][1]))
                sum+=G[i][j][1]
    return E,sum
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    T=[0 for _ in range(n1+n2)]

    while i<n1 and j<n2:
        if T1[i][2]>T2[j][2]:
            T[i+j]=T1[i]
            i+=1
        else:
            T[i+j]=T2[j]
            j+=1
    
    while i<n1:
        T[i+j]=T1[i]
        i+=1
    
    while j<n2:
        T[i+j]=T2[j]
        j+=1
    
    return T

def merge_sort(T):
    n=len(T)
    if n==1:
        return T
    q=n//2
    T1=T[:q]
    T2=T[q:]

    return merge(merge_sort(T1),merge_sort(T2))

def lufthansa ( G ):
    E,all_sum=graph_to_edges(G)
    E=merge_sort(E)
    n=len(G)
    m=len(E)
    taken=[False for i in range(m)]
    V=[Node(i) for i in range(n)]
    A=[]
    sum=0
    max_edge=0
    #max_ind=0
    for i in range(m):
        e=E[i]
        u,v,c=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            #A.append(e)
            taken[i]=True
            sum+=c
        elif max_edge<c:
            max_edge=c
            #max_ind=i

    sum+=max_edge
    #A.append(E[max_ind])
    return all_sum-sum
        


runtests ( lufthansa, all_tests=True )
G = [
[(1, 15), (2, 5), (3, 10) ],
[(0, 15), (2, 8), (4, 5), (5, 12)],
[(0, 5), (1, 8), (3, 5), (4, 6) ],
[(0, 10), (2, 5), (4, 2), (5, 11)],
[(1, 5), (2, 6), (3, 2), (5, 2) ],
[(1, 12), (4, 2), (3, 11) ]
]
print(lufthansa(G))