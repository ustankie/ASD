from zad4testy import runtests
from collections import deque
def longer( G, s, t ):
    n=len(G)
    m=0
    for u in range(n):
        m+=len(G[u])
        

    m//=2
    V=[[False for _ in range(n)]for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            V[v][u]=True
    par=[None for _ in range(n)]
    T=[None for _ in range(n)]
    k=DFS(G,s,t,V,par,float('inf'))
    #print(k)
    if k==None: return k
    #print(par)
    
    p=t
    count=1
    while p!=s:
        u=p
        v=par[p]
        #if not cycle: return None
        if V[u][v]:
            V[u][v]=False
            V[v][u]=False
            T=[None for _ in range(n)]

            d=DFS(G,s,t,V,T,k)
            #print(d)
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
            # if not d[1]:
            #     return u,v
            V[u][v]=True
            V[v][u]=True
        if p==u:
            p=v
        count+=1
        


def DFS(G,s,t,V,par,val_t):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    #child=[None for _ in range(n)]
    val=[None for _ in range(n)]

    vis[s]=True
    val[s]=0
    Q=deque()
    Q.append(s)

    while (len(Q))>0:
        u=Q.popleft()
        #print(u)
        
        for v in G[u]:
            if V[v][u]:
                if not vis[v]:
                    vis[v]=True
                    par[v]=u
                
                    val[v]=val[u]+1
                    if t==v:return val[v]
                    if val[v]>val_t: return val[v]
                    Q.append(v)

    return None

# def DFS2(G,s,t,V):
#     n=len(G)
#     vis=[False for _ in range(n)]
#     par=[None for _ in range(n)]
#     #child=[None for _ in range(n)]
#     val=[[None,None] for _ in range(n)]
#     cycle=False

#     vis[s]=True
#     val[s][0]=0
#     Q=deque()
#     Q.append(s)

#     while (len(Q))>0:
#         u=Q.popleft()
#         #print(u)
#         if t==u:return par
#         for v in G[u]:
#             if V[v][u]:
#                 if not vis[v]:
#                     vis[v]=True
#                     par[v]=u
                
#                     val[v][0]=val[u][0]+1
                    
#                     Q.append(v)
#                 else:  cycle=True

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
print(longer(G3,0,12))