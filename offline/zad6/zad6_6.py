from zad6testy import runtests
from collections import deque

def findbiggest(M):
    n=len(M)
    biggest=0
    for p in range(n):
        for m in M[p]:
            biggest=max(biggest,m)
    return biggest

    
def convert2(G):
    m=findbiggest(G)+1
    n=len(G)
    for i in range(m):
        G.append([])    

    for u in range(n):
        for v in range(len(G[u])):
            G[G[u][v]+n].append(u)
            G[u][v]=G[u][v]+n
    return G

def augment(G,u,match_p,vis):

    vis[u]=True
    for v in G[u]:
        if match_p[v]==None:
            match_p[v]=u
            match_p[u]=v
            return True
              
    for v in G[u]:
        if not vis[match_p[v]] and augment(G,match_p[v],match_p,vis):
            match_p[v]=u
            match_p[u]=v
            return True
    return False

def check(match_p,G,n,vis):

    return False

def binworker(M):
    p=len(M)
    G=convert2(M)
    n=len(G)
    match_p=[None for _ in range(n)]

    for i in range(p):
        for m in G[i]:
            if match_p[i]==None and match_p[m]==None:
                match_p[i]=m 
                match_p[m]=i
                break
    augm=True
    while augm:
        augm=False
        vis=[False for _ in range(n)]
        for u in range(n):
            if match_p[u]==None and augment(G,u,match_p,vis):
                augm=True
                break
    count=0

    for i in range(n):
        if match_p[i]!=None:
            count+=1
    return count//2


    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4
M2=[[16, 5, 6], [9, 12], [1, 2, 11, 16, 19], [2, 9, 10, 11, 12, 13], [3, 6, 9, 12, 13, 16], [2, 4, 7, 15, 17], [1, 2, 5, 7, 12], [8, 9, 11, 12, 18], 
    [3, 5, 6, 8, 18], [1, 10, 4, 7], [1, 10, 7], [1, 18, 15], [0, 1, 6, 9, 15], [0, 3, 4, 14, 15, 17], [16, 6, 7], [2, 19, 12, 13], [0, 1, 11], [0, 7, 11, 17, 18], [8, 6, 15], [11, 4, 14]]
print(binworker(M))