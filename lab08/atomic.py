from collections import deque
from zad1testy import runtests
def floyd(G):
    n=len(G)
    S=[[float('inf')for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        S[i][i]=0

    for u in range(n):
        for v in range(n):
            if G[u][v]:
                S[u][v]=G[u][v]


    for t in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y],S[x][t]+S[t][y])
    return S

def make_graph(G,d):
    n=len(G)
    S=floyd(G)

    A=[]
    for x in range(n):
        for y in range(n):
            if S[x][y]>=d:
                A.append([(x,y)])
    return A

def make_matrix(G):
    n=len(G)
    M=[[False for i in range(n)] for j in range(n)]
    for u in range(n):
        for v,c in G[u]:
            M[u][v]=True
            M[v][u]=True
    return M

def BFS(A,s,t):
    n=len(A)
    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]

    ind_s=None
    ind_t=None
    for i in range(n):
        if A[i][0][0]==s and A[i][0][1]==t:
            ind_s=i
        if A[i][0][1]==s and A[i][0][0]==t:
            ind_t=i
        if ind_s!=None and ind_t!=None:
            break
        

    if ind_s==None:
        return None
    
    vis[ind_s]=True
    Q=deque()
    Q.append(ind_s)

    while len(Q)>0:
        i=Q.popleft()
        m=len(A[i])
        for j in range(1,m):
            el=A[i][j]
            state,curr_ind=el
            if not vis[curr_ind]:
                vis[curr_ind]=True
                par[curr_ind]=i
                # if curr_ind==ind_t:
                #     return par,ind_s,ind_t
                Q.append(curr_ind)
    return par,ind_s,ind_t
    

def atomic(G,s,t,d):
    A=make_graph(G,d)
    M=G

    a=len(A)

    for x in range(a):
        u1,v1=A[x][0]
        for y in range(a):
            u2,v2=A[y][0]
            if not(u1==v2 and u2==v1): 

                if (M[v1][v2] and M[u1][u2] ) or(u1==u2 and M[v1][v2] ) or (v1==v2 and M[u1][u2] ):

                    A[x].append((A[y][0],y))
                    A[y].append((A[x][0],x))


    par,ind_s,ind_t=BFS(A,s,t)
    T=[]
    p=ind_t
    #print(A)
    #print(par)
    while p!=None:
        T.append(A[p][0])
        p=par[p]


    
    return T[::-1]





    




G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]
G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]
M=[
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]
print(atomic(M,0,3,2)) 
runtests( atomic)