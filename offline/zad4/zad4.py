from zad4testy import runtests
from collections import deque
def longer( G, s, t ):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    val=[None for _ in range(n)]

    vis[s]=True
    val[s]=0
    Q=deque()
    Q.append(s)

    while (len(Q))>0:
        u=Q.popleft()
        
        for v in G[u]:
            #print(par,vis)
            if not vis[v]:
                vis[v]=True
                par[v]=u
                val[v]=val[u]+1
                Q.append(v)
            #elif par[u]!=v:
        #if u==t: break

    # vis1=[False for _ in range(n)]
    # par1=[None for _ in range(n)]
    # val1=[None for _ in range(n)]

    # vis2=[False for _ in range(n)]
    # par2=[None for _ in range(n)]
    # val2=[None for _ in range(n)]

    # vis1[s]=True
    # val1[s]=0

    # vis2[t]=True
    # val2[t]=0

    # Q1=deque()
    # Q1.append(s)
    
    # Q2=deque()
    # Q2.append(t)
    # while (len(Q))>0:
    #     u1=Q1.popleft()
    #     u2=Q2.popleft()
    #     for v in G[u1]:
    #         if not vis1[v]:
    #             vis1[v]=True
    #             par1[v]=u1
    #             val1[v]=val1[u]+1
    #             Q1.append(v)
    #     for v in G[u2]:
    #         if not vis2[v]:
    #             vis2[v]=True
    #             par2[v]=u2
    #             val2[v]=val2[u]+1
    #             Q2.append(v)
    if u!=t: return None
    T=deque()
    p=t
    while par[p]!=s:
        T.append(p)
        p=par[p]
    T.append(p)
    T.append(s)
    #print(T)

    vis1=[False for _ in range(n)]
    par1=[None for _ in range(n)]
    val1=[None for _ in range(n)]

    vis1[t]=True
    val1[t]=0
    m=len(T)
    # for i in range(n):
    #     val[T[i]]=(m-i-1,m-i-1)
    Q=deque()
    Q.append(t)

    while (len(Q))>0:
        u=Q.popleft()
        m=len(G[u])
        for x in range(m-1,-1,-1):
            #print(par,vis)
            v=G[u][x]
            if not vis1[v]:
                vis1[v]=True
                par1[v]=u
                val1[v]=val[u]+1
                #if val1[v]>val[v]: return (par[v],v)
                Q.append(v)
    print(par1)
    print(s)
    T2=deque()
    p=s
    while par1[p]!=t:
        T2.append(p)
        p=par1[p]
    T2.append(p)
    T2.append(t)
    #print(T)
    if val1[s]==val[t]: 
        for i in range(1,m):
            if T2[i]==T[i]: return None
    for i in range(1,m):
        if T2[i]==T[i]: return (i-1,i)

    # print(vis1)
    # print(val1)
    # print(par1)




            


    return None
                





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = False )
G=[[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
G2=[[1, 2], [0, 2], [0, 1]]
#print(longer(G2,0,2))