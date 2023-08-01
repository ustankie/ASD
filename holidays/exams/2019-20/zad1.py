from zad1testy import runtests
from queue import PriorityQueue
def convert(G):
    n=len(G)
    G1=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                G1[i].append((j,G[i][j]))
    return G1

def relax(c,d,last,u,v):
    a=False
    if d[v][last]>d[u][(last+1)%3]+c:
        d[v][last]=d[u][(last+1)%3]+c
        a=True

    if d[v][last]>d[u][(last+2)%3]+c:
        d[v][last]=d[u][(last+2)%3]+c
        a=True

    return a
def islands(G , a , b ):
    n=len(G)
    G1=convert(G)
    inf=float('inf')
    d=[[inf,inf,inf] for _ in range(n)]

    d[a][0]=d[a][1]=d[a][2]=0

    Q=PriorityQueue()
    Q.put((0,a,0))
    Q.put((0,a,1))
    Q.put((0,a,2))

    while not Q.empty():
        c,u,l=Q.get()
        if c==d[u][l]:
            for v,k in G1[u]:
                if relax(k,d,l,u,v):
                    if k==1:
                        last=0
                    elif k==5:
                        last=1
                    else:
                        last=2
                    Q.put((d[v][l],v,last))
    return min(d[b])



        

runtests(islands)

G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]

print(islands(G1, 5, 2) )