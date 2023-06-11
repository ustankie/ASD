from collections import deque
def transform(G,c):
    n=len(G)
    T=[deque() for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]==c:
                if ((i-1)*(n)+j)>=0 and G[i-1][j]==c:
                    T[i*n+j].append((i-1)*(n)+j)
                if (i*n+j-1)>=(n*i)and G[i][j-1]==c:
                    T[i*n+j].append(i*n+j-1)
                if (i*n+j+1)<(n*(i+1))and G[i][j+1]==c:
                    T[i*n+j].append(i*n+j+1)
                if ((i+1)*(n)+j)<(n*n)and G[i+1][j]==c:
                    T[i*n+j].append((i+1)*(n)+j)
    #print(*T,sep="\n")
    return T

def reverse(T):
    n=len(T)
    for i in range(n//2):
        T[i],T[n-i-1]=T[n-1-i],T[i]
    return T

def lakes(G):
    def Visit(G,s):
        nonlocal time
        time+=1
        vis[s]=True
        for v in T[s]:
            if not vis[v]:
                par[v]=s
                Visit(G,v)
    
    n=len(G)
    time=0
    T=transform(G,"W")
    vis=[False for _ in range(n*n)]
    par=[None for _ in range(n*n)]

    count=0
    max_lake=0
    for u in range(n*n):
        if not vis[u] and len(T[u])>0:
            count+=1
            Visit(G,u)
            max_lake=max(max_lake,time)
            time=0
    return count,max_lake

def dry_path(G,s,k):
    n=len(G)

    s1=s[0]*n+s[1]
    k1=k[0]*n+k[1]

    vis=[False for _ in range(n*n)]
    val=[None for _ in range(n*n)]
    par=[None for _ in range(n*n)]

    T=transform(G,"L")

    vis[s1]=True
    val[s1]=0
    
    Q=deque()
    Q.append(s1)

    while len(Q)>0:
        u=Q.popleft()
        for v in T[u]:
            if not vis[v]:
                vis[v]=True
                val[v]=val[u]+1
                par[v]=u
                Q.append(v)
        if u==k1:
            break
    if u!=k1:
        return None,-1

    p=k1
    R=deque()
    while par[p]!=s1:
        R.append((p//n,p%n))
        p=par[p]
    R.append((p//n,p%n))
    R.append(s)

    return reverse(R),val[k1]


w="W"
l="L"
G=[[l,w,l,l,l,l,l,l],[l,w,l,w,w,l,l,l],[l,l,l,w,w,l,w,l],[l,w,w,w,w,l,w,l],[l,l,w,w,l,l,l,l],
   [l,w,l,l,l,l,w,w],[w,w,l,w,w,l,w,l],[l,l,l,w,l,l,l,l]]
print(*G,sep="\n")
print(lakes(G))
print(*dry_path(G,(0,0),(7,7)),sep="\n")