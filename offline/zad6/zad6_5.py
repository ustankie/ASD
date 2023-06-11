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

def DFS(G,s,vis):
    n=len(G)

    par=[None for _ in range(n)]
    vis[s]=True

    stack=deque()
    stack.append(s)
    
    while len(stack)>0:
        u=stack.pop()
        for v,c in G[u]:
            if not vis[v] and c>0:
                vis[v]=True
                par[v]=u
                stack.append(v)
    length=0
    return False,par,u

def BFS(G,s,match_p):
    n=len(G)
    Q=deque()
    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    vis[s]=True
    Q.append((s,1))
    u=s 
    while len(Q)>0 and (len(G[u])>1 or u==s):
        u,m=Q.pop()
        for v in G[u]:
            if ((match_p[v]==u and not m) or(match_p[v]!=u and m))and not vis[v]:
                vis[v]=True
                d[v]=d[u]+1
                par[v]=u
                Q.append((v,1-m))
    #print(u,par)
    a=0
    for i in range(n):
        if d[i]>a and d[i]%2==1:
            a=d[i]
            u=i
    if d[u]%2==0:
        u=par[u]
    if u!=s and u!=None:
        p=u
        while par[p]!=s:
            #print(p)
            match_p[p]=par[p]
            match_p[par[p]]=p
            p=par[par[p]]
            #p=par[p]
        match_p[p]=par[p]
        match_p[par[p]]=p
        #print(match_p)
        return True
    return False




def binworker(M):
    p=len(M)
    G=convert2(M)
    #print(*G,sep="\n")
    n=len(G)
    match_p=[None for _ in range(n)]

    for i in range(p):
        for m in G[i]:
            if match_p[i]==None and match_p[m]==None:
                match_p[i]=m 
                match_p[m]=i
                break
    #print(match_p)
    
    a=True
    while a:
        a=False
        for i in range(n):
            if match_p[i]==None:
                a=a or BFS(G,i,match_p)
    count=0
    for i in range(n):
        if match_p[i]!=None:
            count+=1
    #print(match_p)
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