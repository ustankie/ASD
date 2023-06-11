from zad6testy import runtests
from collections import deque

def findbiggest(M):
    n=len(M)
    biggest=0
    for p in range(n):
        for m in M[p]:
            biggest=max(biggest,m)
    #print(biggest)
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
        G.append([[n+m+1,1,0]])    
    G.append([[i,1,0] for i in range(n)])
    G.append([[i,0,0]for i in range(n,m+n)])
    for u in range(n):
        for v in range(len(G[u])):
            G[G[u][v]+n].append([u,0,0])
            G[u][v]=[G[u][v]+n,1,0]
        G[u].append([n+m,0,0])      
            


    for u in range(n+m):
        G[u]=merge_sort(G[u])
    return G
def BFS2(G,s,t):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        #print(u)
        for el in G[u]:
            v,c,f=el
            #if c>0:
            #     cp=c-f               
            if not vis[v] and (c-f)>0: 
                #print(u,v,c,f)                  
                vis[v]=True
                par[v]=u

                if v==t:
                    return True,par
                Q.append(v)
    return False,par
def binsearch(G,el):
    #print(G)
    n=len(G)
    i=0
    j=n-1
    q=(i+j)//2
    while i<j:
        q=(i+j)//2
        if G[q][0]==el:
            #print("q: ",q,G[q][0],el)
            return q
        if G[q][0]>el:
            j=q-1
        else:
            i=q+1
    #if G[i][0]==el:
    #print(i,G[i][0],el)
    return i
        
def binworker(M):
    G=convert2(M)
    print(*G,sep="\n")
    n=len(G)
    max_flow=0
    s=n-2
    t=n-1

    augm,par=BFS2(G,s,t)
    
    while augm:
        p=t
        #print(par)
        #print()
        while p!=s:
            m=len(G[par[p]])
            i=binsearch(G[par[p]],p)
            #print(G[par[p]][i],p)
            G[par[p]][i][2]+=1
            j=binsearch(G[p],par[p])
            G[p][j][2]=1          
            p=par[p]
        max_flow+=1
        augm,par=BFS2(G,s,t)
    #print(*G,sep="\n")
    #print(par)
    return max_flow

    

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( binworker, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4
M2=[[0, 1], [0, 1], [0]]
print(binworker(M))