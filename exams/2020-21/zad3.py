from zad3testy import runtests
from queue import PriorityQueue
def transform(G):
    n=len(G)
    G1=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                G1[i].append((j,G[i][j]))
    return G1

def relax(par,d,u,v,c,m):
    if m==1:
        if d[v][1]>d[u][0]+c:
            d[v][1]=d[u][0]+c
            par[v][1]=u
            return True
    else:
        a=min(d[u])
        if d[v][0]>a+c:
            d[v][0]=a+c
            par[v][0]=u
            return True
    return False

def jumper(G,s,t):
    n=len(G)
    G=transform(G)
    #print(G)

    d=[[float('inf'),float('inf')] for _ in range(n)]
    par=[[None,None] for _ in range(n)]

    Q=PriorityQueue()
    Q.put((0,None,None,s,1))
    d[s]=[0,0]
    
    while not Q.empty():
        c,c_prev,u_prev,u,m=Q.get()

        if d[u][m]<=c:
            for v,k in G[u]:
                if relax(par,d,u,v,k,0):
                    Q.put((d[v][0],k,u,v,0))

                if not m and u_prev!=v and relax(par,d,u_prev,v,max(c_prev,k),1):
                    Q.put((d[v][1],k,u_prev,v,1))
    
    return min(d[t])#,path[::-1]

                    

runtests(jumper)

G=[[0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]]
G=[[0, 1, 200, 200, 200, 200],
              [1, 0, 2, 200, 200, 200],
              [200, 2, 0, 40, 200, 200],
              [200, 200, 40, 0, 40, 200],
              [200, 200, 200, 40, 0, 117],
              [200, 200, 200, 200, 117, 0]]
s=0
t=4
print(jumper(G,s,t))