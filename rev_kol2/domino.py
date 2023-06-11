from collections import deque
def transform(D):
    n=len(D)
    G=[]
    for i in range(n):
        a,b=D[i]
        while a>(len(G)-1):
            G.append([])
            #print(a)
        while b>(len(G)-1):
            G.append([])
            #print(b)
        G[a].append(b)
    return G

def reverse(G):
    n=len(G)
    G2=[[]for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G2[v].append(u)
    return G2
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    T=[0 for _ in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][0]<T2[j][0]:
            T[i+j]=T2[j]
            j+=1
        else:
            T[i+j]=T1[i]
            i+=1
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
def domino(D):
    def DFS(G,u,d,w):
        nonlocal time
        stack=deque()
        stack.append((-1,u))
        
        while len(stack)>0:
            t,u=stack.pop()
            have_children=False
            if not vis[u]:
                first=True
                vis[u]=True               
                for v in G[u]:
                    if not vis[v]:
                        print(u,v)
                        if first_vis[u]<0:
                            first_vis[u]=v
                        par[v]=u
                        have_children=True
                        if first:
                            stack.append((u,v) ) 
                            first=False
                        else:
                            stack.append((-1,v) )
            if not have_children: 
                print(u,have_children) 
                d[u][0]=time
                time+=1 
                T[w].append(u)
                print(T)
            for i in range(n):
                if first_vis[i]==u and d[i][0]==0:
                    d[i][0]=time
                    time+=1 
                    T[w].append(i)
                    break

            
            
        # for u in range(n):
        #     if par[u]>=0:
        #         T[w].append(u)

    G=transform(D)
    time=1
    n=len(G)
    vis=[False for _ in range(n)]
    d=[[0,i] for i in range(n)]
    T=[[]]
    first_vis=[-1 for _ in range(n)]
    par=[-1 for _ in range(n)]

    for u in range(n):
        if not vis[u]:
            DFS(G,u,d,0)
    
    G2=reverse(G)

    d=merge_sort(d)
    vis=[False for _ in range(n)]
    print(d)
    d2=[[0,i] for i in range(n)]
    first_vis=[-1 for _ in range(n)]
    T=[]
    w=-1
    
    for i in range(n):
        if not vis[d[i][1]]:
            w+=1
            T.append([])
            first_vis=[-1 for _ in range(n)]
            DFS(G2,d[i][1],d2,w)
    return T,w+1

G=[[1],[2],[0,3,7],[5],[3],[6],[4,7],[10,8],[9],[7],[9]]


E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6),
     (4, 7), (4, 6), (5, 9), (10, 0), (15, 14), (15, 11), (15, 11), (11, 13), (14, 13), (5, 13),
     (16, 8), (0, 12), (12, 3)]
E1 = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)]

print(domino(E1))





    
