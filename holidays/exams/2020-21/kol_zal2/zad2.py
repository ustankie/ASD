from zad2testy import runtests
def find_max(L,M):
    n=len(L)
    maxi=0

    for i in range(n):
        maxi=max(maxi,L[i]//M,L[i]%M)
    
    return maxi+1

def create_graph(L,M,n):
    m=len(L)
    G=[[]for _ in range(n)]

    out_edges=[0 for _ in range(n)]
    in_edges=[0 for _ in range(n)]

    for i in range(m):
        u=L[i]//M
        v=L[i]%M
        G[v].append(u)
        out_edges[v]+=1
        in_edges[u]+=1
    
    return G,out_edges,in_edges

def find_beginning(out_edges,in_edges,n):
    begin=None
    end=None
    a=True
    for i in range(n):
        if out_edges[i]>in_edges[i]:
            if begin==None:
                begin=i
            else:
                a=False
                break
        elif in_edges[i]>out_edges[i]:
            if end==None:
                end=i
            else:
                a=False
                break
    if a:
        if end==begin==None:
            return None,True
        
        if end==None or begin==None:
            return None,False
        
        return begin,out_edges
    return None,False

def euler(G,out_edges,in_edges,n,L,M):
    begin,exists=find_beginning(out_edges,in_edges,n)
    
    if not exists:
        return []
    
    if begin==None:
        for i in range(n):
            if len(G[i])>0:
                begin=i
                break
    
    last=[0 for _ in range(n)]
    T=[]

    def DFS(u):
        m=len(G[u])
        for i in range(last[u],m):
            v=G[u][i]
            last[u]+=1
            if v!=None:
                G[u][i]=None
                DFS(v)
        T.append(u)
    
    DFS(begin)
    
    R=[]
    m=len(T)

    for i in range(m-1):
        R.append(T[i]*M+T[i+1])
    return R


def order(L,K):
    M=10**K
    n=find_max(L,M)
    G,out_edges,in_edges=create_graph(L,M,n)
    return euler(G,out_edges,in_edges,n,L,M)

    

    
runtests( order )


