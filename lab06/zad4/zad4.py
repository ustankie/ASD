from zad4testy import runtests
from collections import deque

def BFS(G,s,t,par):
    n=len(G)
    Q=deque()
    vis=[False for _ in range(n)]
    vis[s]=True
    Q.append(s)
    for u in range(n):
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                par[v]=u
                if v==t: return
                Q.append(v)
    
        
def longer( G, s, k ):

    def DFS(G,u):
        nonlocal t
        t+=1       
        time[u]=t
        low[u]=t
        #print(u)
        for v in G[u]:
            if not low[v]:
                if v==k:
                    Flag=True
                par[v]=u
                low[v]=t+1
                DFS(G,v)
                low[u]=min(low[u],low[v])
            elif v!=par[u]:                
                low[u]=min(low[u],time[v])

    Flag=False
    n=len(G)
    t=1
    time=[0 for _ in range(n)]
    low=[0 for _ in range(n)]
    par=[None for _ in range(n)]
    time[s]=1
    low[s]=1

    for v in range(n):
        if not low[v] and not Flag:
            DFS(G,v)
    
    path=[None for _ in range(n)]
    BFS(G,s,k,path)
    # print(path)
    # A=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    # print(A)
    # print(time)
    # print(low)
    p=k
    while p!=s:
        #print(p)
        # print(path[p])
        # print(low[path[p]])
        # print(time[path[p]])
        if path[p]!=None and (low[p]==time[p]):
            return (p,path[p])
        count1=0
        for v in range(n):
            if low[v]==low[p]:
                count1+=1
        q=p
        o=p
        count2=0
        while q!=s and low[q]==low[p]:
            #if low[q]==low[p]:
            count2+=1
            o=q
            q=path[q]
        #print(q,count1,count2)
        if path[p]!=None and count1>2*count2:
            return (p,path[p])
        if q==s:
            p=s
        else:
            p=o
    return None

    





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
G=[[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
G2=[[1, 2], [0, 2], [0, 1]]
G3=[[1,3],[0,2],[1,5,3],[0,2,4],[3],[2,7,6],[5,7],[6,5]]
G4 = [ [1,2], #0
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
G5=[[1,2],[0,3],[0,3],[1,2]]
print(longer(G5,0,3))