from zad7ktesty import runtests 
from collections import deque
def simplify(T,D):
    n=len(T)
    m=len(T[0])
    d=len(D)
    R=[0 for _ in range(d)]
    Q=deque()
    dir=[(0,1),(-1,0),(0,-1),(1,0)]
    vis=[[False for _ in range(m)]for _ in range(n)]
    for j in range(d):
        i=D[j]       
        vis[0][i]=True
        #print(T[0][i])
        #if T[0][i]:
        Q.append((0,i))
        while len(Q)>0:
            u1,u2=Q.popleft()
            R[j]+=T[u1][u2]
            
            
            for a,b in dir:
                v1=a+u1
                v2=b+u2
                if n-1>=v1>=0 and m-1>=v2>=0:
                    if not vis[v1][v2] and T[v1][v2]>0:
                        vis[v1][v2]=True

                        Q.append((v1,v2))
        
    return R

def ogrodnik (T, D, Z, l):
    #print(T,D,Z,l)
    T=simplify(T,D)
    #print(T)
    n=len(T)
    F=[[0 for _ in range(l+1)]for _ in range(n)]

    for i in range(T[0],l+1):
        F[0][i]=Z[0]
    for i in range(n-1):
        for j in range(l+1):
            F[i+1][j]=F[i][j]
            if j-T[i+1]>=0:
                F[i+1][j]=max(F[i][j],F[i][j-T[i+1]]+Z[i+1])
    #print(*F,sep="\n")
    return max(F[n-1])

runtests( ogrodnik, all_tests=True )

T=[[0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0], 
   [0, 0, 0, 0, 2, 0, 0, 0, 0, 6, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0], 
   [0, 0, 0, 0, 1, 0, 0, 0, 3, 1, 0, 0, 2, 2, 2, 0, 2, 4, 2, 0, 0], 
   [0, 0, 0, 1, 2, 0, 0, 1, 4, 6, 0, 2, 1, 3, 0, 0, 3, 1, 0, 0, 0]
    ] 
D=[4, 9, 12, 16] 
Z=[13, 11, 15, 4] 
l=32

print(ogrodnik(T,D,Z,l))