from zad6testy import runtests
from collections import deque

def convert(M):
    n=len(M)
    for i in range(n+1):
        M.append([])
    M.append([])
    M.append([])

    for i in range(n):
        M[2*n+1].append([i,1])
        M[2*n+2].append([i+n,0])
        for j in range(len(M[i])):
            M[M[i][j]+n].append([i,0])
            M[i][j]=[M[i][j]+n,1]
            
    for i in range(n):
        #M[i+n].append([2*n+1,0])
        M[i+n].append([2*n+2,1])
        
        M[i].append([2*n+1,0])
    M[2*n].append([2*n+2,1])
    #M[2*n].append([2*n+2,0])
    M[2*n+2].append([2*n,0])
    for i in range(2*n+1):
        M[i]=sorted(M[i],key=lambda x:x[0])

def DFS(G,s,t):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    stack=deque()
    stack.append(s)
    vis[s]=True
    while len(stack)>0:
        u=stack.pop()
        for v,c in G[u]:
            if c>0 and not vis[v]:
                vis[v]=True
                par[v]=u
                if v==t:
                    return True,par
                stack.append(v)
    return False,par

def binsearch(T,x):
    i=0
    j=len(T)-1
    while i<j:
        q=(i+j)//2
        if T[q][0]==x:
            return q
        if x<T[q][0]:
            j=q-1
        else:
            i=q+1
    return i

def binworker(M):
    n=len(M)
    s=2*n+1
    t=2*n+2
    convert(M)
    #print(*M,sep="\n")
    augm,par=DFS(M,s,t)
    max_flow=0

    while augm:
        p=t
        while p!=s:
            i=binsearch(M[par[p]],p)
            M[par[p]][i][1]-=1
            j=binsearch(M[p],par[p])
            M[p][j][1]+=1
            
            # print(*M,sep="\n")
            # print("\n",p,"\n")
            p=par[p]
        max_flow+=1
        # print(par)
        # print(*M,sep="\n")
        # print("\n\n")
        augm,par=DFS(M,s,t)
    return max_flow




runtests( binworker, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4
M1=[[0, 1], [0, 1], [0]]
M2=[[16, 5, 6], [9, 12], [1, 2, 11, 16, 19], [2, 9, 10, 11, 12, 13], [3, 6, 9, 12, 13, 16], [2, 4, 7, 15, 17], [1, 2, 5, 7, 12], [8, 9, 11, 12, 18], 
    [3, 5, 6, 8, 18], [1, 10, 4, 7], [1, 10, 7], [1, 18, 15], [0, 1, 6, 9, 15], [0, 3, 4, 14, 15, 17], [16, 6, 7], [2, 19, 12, 13], [0, 1, 11], [0, 7, 11, 17, 18], [8, 6, 15], [11, 4, 14]]
print(binworker(M1))