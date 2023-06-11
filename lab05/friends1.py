from collections import deque

def friends(G):
    G=transform(G)

    n=len(G)
    vis=[False for _ in range(n)]
    val=[None for _ in range(n)]

    Q=deque()
    Q.append(0)
    vis[0]=True
    val[0]=0

    while (len(Q)>0):
        u=Q.popleft()
        T=deque()
        for v in G[u]:
            if not vis[v]:
                T.append(v)
                vis[v]=True
                val[v]=val[u]+1
                Q.append(v)

    #zliczamy ludzi, którzy otrzymali wiadomość danego dnia
    max_friends=0
    fr=deque()
    day=0
    count=[0 for i in range(n)]

    for i in range(n):
        count[val[i]]+=1

    #znajdujemy dzień o największej liczbie osób
    for i in range(n):
        if count[i]>max_friends:
            max_friends=count[i]
            day=i
    # W kolejce fr zapisujemy wszystkich ludzi, którzy otrzymali wiadomość tego dnia
    for i in range(n):
        if val[i]==day:
            fr.append(i)

    return day,fr

#przekształca z listy par na listę sąsiedztwa -> O(n), gdzie n - liczba par, czyli O(v choose 2)=O(v^2)
def transform(G):
    n=len(G)
    max_val=0
    for i in range(n):
        max_val=max(max_val,G[i][0],G[i][1])

    T=[deque() for i in range(max_val+1)]
    for i in range(n):
        T[G[i][0]].append(G[i][1])
        T[G[i][1]].append(G[i][0])
    return T



# G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
# G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]
# G3=[[1,2],[0,3],[0,4,5],[1],[2],[2]]
#print(friends(G3))
G4=[(0,2),(0,1),(1,3),(2,4),(2,5)]
print(friends(G4))