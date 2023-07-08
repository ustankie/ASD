from zad6testy import runtests
from collections import deque

def convert(M):
    n=len(M)
    for i in range(n+1):
        M.append([])
    for i in range(n):
        for j in range(len(M[i])):
            M[M[i][j]+n].append(i)
            M[i][j]=M[i][j]+n
            

def binworker(M):
    m=len(M)
    convert(M)
    n=len(M)
    match=[None for _ in range(n)]
    for u in range(m):
        for v in M[u]:
            if match[u]==None and match[v]==None:
                match[u]=v
                match[v]=u
                break
    augm=True
    while augm:
        augm=False
        vis=[False for _ in range(n)]
        for u in range(n):
            if match[u]==None and augment(M,u,match,vis):
                augm=True
                break
    count=0
    for i in range(n):
        if match[i]!=None:
            count+=1
    return count//2
def augment(G,u,match,vis):
    vis[u]=True
    for v in G[u]:
        if match[v]==None:
            match[v]=u
            match[u]=v
            return True
    for v in G[u]:
        if not vis[match[v]] and augment(G,match[v],match,vis):
            match[v]=u
            match[u]=v
            return True
    return False




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