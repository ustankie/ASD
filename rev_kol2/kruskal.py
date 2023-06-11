class Node():
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.par=self

def findset(x):
    if x!=x.par:
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
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    T=[0 for _ in range(n1+n2)]

    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][2]<T2[j][2]:
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
    T1=T[:n//2]
    T2=T[n//2:]
    return merge(merge_sort(T1),merge_sort(T2))


def kruskal(E,n):
    E=merge_sort(E)
    #print(E)
    V=[Node(i) for i in range(n)]
    
    T=[]
    for e in E:
        u,v,c=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            T.append(e)
    return T

E=[(1,0,1),(0,2,3),(2,5,6),(3,5,2),(2,3,4),(3,4,7),(1,3,5),(1,4,8)]
print(kruskal(E,6))
