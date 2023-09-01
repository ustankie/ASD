from math import sqrt,ceil
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

def make_edge_list(G):
    n=len(G)
    E=[]

    for i in range(n-1):
        for j in range(i+1,n):
            dist=sqrt((G[j][1]-G[i][1])*(G[j][1]-G[i][1])+(G[j][0]-G[i][0])*(G[j][0]-G[i][0]))
            E.append((i,j,dist))
    return E

def highway(G):
    n=len(G)
    E=make_edge_list(G)
    E.sort(key=lambda x: x[2])
    m=len(E)
    
    V=[Node(i) for i in range(n)]

    min_diff=float('inf')
    R=[]
    for j in range(m):
        for i in range(n):
            A=[]
            V=[Node(i) for i in range(n)]
            
            for k in range(j,m):
                e=E[k]
                u,v,c=e
                if findset(V[u])!=findset(V[v]):
                    union(V[u],V[v])
                    A.append(e)
            if len(A)<n-1:
                return ceil(min_diff),R
            print(A)
            diff=A[len(A)-1][2]-A[0][2]
            if min_diff>diff:
                min_diff=diff
                R=A
    return ceil(min_diff),R



P = [(4, 4), (2, 3), (4.5, 0), (0, 0), (1, -1), (3, -2), (2, -4), (-1, 2), (-2, -2), (-4, 4), (-5, 0)]
# P = [(5, 5), (3, -5), (0, 3), (-5, 0)]
print(highway(P))

