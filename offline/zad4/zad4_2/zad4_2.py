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

    last_val=0
    while (len(Q))>0:
        u=Q.popleft()
        # if last_val!=val[u]:
        #     print(len(Q))
        #     if u!=s and len(Q)==0:
        #         return u,par[u]
        #     last_val=val[u]

        #if t==u:break
        for v in G[u]:
            #print(par,vis)
            if not vis[v]:
                vis[v]=True
                par[v]=u
               
                val[v][0]=val[u][0]+1
                Q.append(v)
            elif val[v][0]==(val[u][0]+1):
                val[v][1]=True
            elif val[v][1]==None:
                print(v,val[v][0])
                val[v][1]=False
    p=t
    while p!=s:

        child[par[p]]=p
        p=par[p]
    print(val)
    val_num=[0 for _ in range]
    v=t
    while v>s:
        count=0
        while v!=s and val[v][0]==val[par[v]][0]:
            v=par[v]
            count+=1
        if count==0 and v!=s and not val[v][1]:
            print(par)
            return par[v],v
        if count==0:
            return v,child[v]
        v=par[v]


                





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