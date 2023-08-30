from zad1_testy import runtests
def binsearch(T,x):
    i=0
    j=len(T)-1
    while i<=j:
        q=(i+j)//2
        if T[q]==x:
            return q
        if T[q]<x:
            i=q+1
        else:
            j=q-1
    return i

def perform_DFS(G,s,t,m):
    n=len(G)
    vis=[False for _ in range(n)]
    vis_edge=[0 for i in range(m)]


    def DFS(u):
        vis[u]=True
        for v,i in G[u]:
            vis_edge[i]=True
            if not vis[v]:
                vis[v]=True
                DFS(v)
    
    DFS(s)
    return vis_edge

def intuse(I, x, y):
    n=len(I)

    indices1=[]
    for i in range(n):
        indices1.append(I[i][0])
        indices1.append(I[i][1])
    indices1.sort()
    if indices1[2*n-1]<y or indices1[0]>x:
        print('a')
        return []
    # print(indices1)
    indices=[indices1[0]]
    for i in range(1,2*n):
        if indices1[i]!=indices[len(indices)-1]:
            indices.append(indices1[i])
    
    m=len(indices)
    G=[[]for _ in range(m)]
    G2=[[]for _ in range(m)]


    for i in range(n):
        a=binsearch(indices,I[i][0])
        b=binsearch(indices,I[i][1])
        G[a].append((b,i))
        G2[b].append((a,i))
    
    for i in range(m):
        G[i].sort()
    
    p=binsearch(indices,y)
    q=binsearch(indices,x)
    vis_x=perform_DFS(G,q,p,n)
    
    vis_y=perform_DFS(G2,p,q,n)
    
    R=[]

    for i in range(n):
        if vis_x[i] and vis_y[i]:
            R.append(i)
    return R



runtests(intuse)

I = [(4, 4), (4, 10), (2, 15), (6, 16), (3, 8), (2, 14),
     (6, 21), (3, 1), (0, 5), (7, 15), (3, 19), (2, 17),
     (4, 24), (7, 10), (5, 8), (4, 21), (6, 22), (9, 27),
     (2, 18), (1, 6), (5, 14), (5, 13), (0, 18), (10, 16),
     (9, 24), (11, 24), (5, 7), (6, 14), (1, 7), (3, 19),
     (11, 18), (6, 9), (11, 19), (9, 27), (7, 11),
     (13, 17), (10, 24), (8, 16), (11, 25), (11, 25),
     (11, 26), (12, 30), (4, 9), (5, 11), (10, 20),
     (6, 12), (14, 33), (13, 18), (8, 25), (15, 26)]
I = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
# I = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7),
#      (5, 8), (6, 9), (7, 10), (8, 11), (9, 12)]
x = 1
y = 6
print(intuse(I, x, y))
