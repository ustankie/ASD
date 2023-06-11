from zad4testy import runtests
from collections import deque
def longer( G, s, t ):
    n=len(G)
    par=[None for _ in range(n)]
    T=[None for _ in range(n)]

    k=DFS(G,s,t,par,float('inf'),0,0)

    if k==None: return k
    
    p=t
    count=1
    while p!=s:
        u=p
        v=par[p]

        T=[None for _ in range(n)]

        d=DFS(G,s,t,T,k,u,v)
        if d==None or d>k:
            return u,v
        i=par[v]

        j=T[t]
        for l in range(count):
            j=T[j]

        while (i!=j and i!=s and j!=s):
            i=par[i]
            j=T[j]
        if i==j:
            p=i
        else:
            p=s

        if p==u:
            p=v
        count+=1
        


def DFS(G,s,t,par,val_t,i,j):
    n=len(G)
    vis=[False for _ in range(n)]
    val=[None for _ in range(n)]

    vis[s]=True
    val[s]=0
    Q=deque()
    Q.append(s)

    while (len(Q))>0:
        u=Q.popleft()        
        for v in G[u]:
            if not((v==i and u==j)or (v==j and u==i)):
                if not vis[v]:
                    vis[v]=True
                    par[v]=u
                    val[v]=val[u]+1

                    if t==v:return val[v]
                    if val[v]>val_t: return val[v]

                    Q.append(v)

    return None


                





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
G=[[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
G2=[[1, 2], [0, 2], [0, 1]]
G3=[ [1,2], #0
       [0,3], #1
       [0,4], #2
       [1,5,6], #3
       [2,7], #4
       [3,8], #5
       [3,8], #6
       [4,8], #7
       [5,6,7,9], #8    
       [8,10,11], #9
       [9,12], # 10
       [9,12], # 11
       [10,11]]
#print(longer(G3,0,12))