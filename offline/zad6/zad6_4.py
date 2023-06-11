from zad6testy import runtests
from collections import deque

def findbiggest(M):
    n=len(M)
    biggest=0
    for p in range(n):
        for m in M[p]:
            biggest=max(biggest,m)
    return biggest

def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    T=[0 for _ in range(n1+n2)]

    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][0]<T2[j][0]:
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
    
def convert2(G):
    m=findbiggest(G)+1
    n=len(G)
    for i in range(m):
        G.append([[n+m+1,1]])    
    G.append([[i,1] for i in range(n)])
    G.append([[i,0]for i in range(n,m+n)])
    for u in range(n):
        for v in range(len(G[u])):
            G[G[u][v]+n].append([u,0])
            G[u][v]=[G[u][v]+n,1]
        G[u].append([n+m,0])      
            


    for u in range(n+m):
        G[u]=merge_sort(G[u])
    return G

def DFS(G,s,t,vis):
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
                if v==t:
                    return True,par
                stack.append(v)
    return False,par

def binsearch(G,el):
    n=len(G)
    i=0
    j=n-1
    q=(i+j)//2
    while i<j:
        q=(i+j)//2
        if G[q][0]==el:
            return q
        if G[q][0]>el:
            j=q-1
        else:
            i=q+1
    return i
        
def binworker(M):
    G=convert2(M)
    #print(*G,sep="\n")
    n=len(G)
    max_flow=0
    s=n-2
    t=n-1
    vis=[False for _ in range(n)]

    augm,par=DFS(G,s,t,vis)  
    #print(augm,par)  
    while augm:
        #print(augm,par)
        p=t
        while p!=s:
            m=len(G[par[p]])
            i=binsearch(G[par[p]],p)
            G[par[p]][i][1]-=1
            j=binsearch(G[p],par[p])
            G[p][j][1]+=1          
            p=par[p]
        #print(*G,sep="\n")
        max_flow+=1
        #vis[t]=False
        vis=[False for _ in range(n)]

        augm,par=DFS(G,s,t,vis)

    return max_flow

    

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