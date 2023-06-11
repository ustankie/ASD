from zad4testy import runtests
from collections import deque
def longer( G, s, t ):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    child=[None for _ in range(n)]
    val=[[None,None] for _ in range(n)]

    vis[s]=True
    val[s][0]=0
    Q=deque()
    Q.append(s)

    while (len(Q))>0:
        u=Q.popleft()
        if t==u:break
        for v in G[u]:
            #print(par,vis)
            if not vis[v]:
                vis[v]=True
                par[v]=u
                val[v][0]=val[u][0]+1
                Q.append(v)

    #child[s]=p


    n=len(G)
    vis=[False for _ in range(n)]
    
    #child=[None for _ in range(n)]
    val=[[None,None] for _ in range(n)]

    p=t
    while p!=s:
        val[p][1]="P"
        child[par[p]]=p
        p=par[p]
    print(child)
    print(val) 
    val[p][1]="P"
    vis[s]=True
    val[s][0]=0
    Q=deque()
    Q.append(s)
    par=[None for _ in range(n)]
    while (len(Q))>0:
        u=Q.popleft()
        #if t==u:break
        for v in G[u]:
            #print(par,vis)
            if not vis[v]:
                vis[v]=True
                par[v]=u
                val[v][0]=val[u][0]+1
                Q.append(v)
            elif par[u]!=v :
                
                p=par[v]
                q=u
                Flag=False
                while p!=q and p!=s and q!=s:
                    if (val[p][1]=="P" or val[q][1]=="P"):
                        Flag=True
                        print("a")
                    print(p,q)
                    p=par[p]
                    q=par[q]
                if (val[v][1]=="P"):
                    Flag=True
                print(p,q)
                print()
                if q!=p:
                    p=min(p,q)
                    print(p,child[p],val[child[p]][1])
                    if val[child[p]][1]=="P":
                        return p,child[p]



            


    return None
                





# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( longer, all_tests = True )
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
print(longer(G3,0,2))