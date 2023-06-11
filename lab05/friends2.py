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

    max_friends=0
    fr=deque()
    day=0
    curr_day=0
    day_size=0

    while (len(Q)>0):
        u=Q.popleft()
        #Sprawdzamy,czy rozpoczęliśmy nowy dzień (nową falę BFS)
        if curr_day<val[u]:
            curr_day=val[u]
            #długość kolejki+1 to ilość osób, które tego dnia otrzymały wiadomość
            day_size=len(Q)+1
            if day_size>max_friends:
                max_friends=day_size
                day=curr_day

        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                val[v]=val[u]+1
                Q.append(v)

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

    T=[[] for i in range(max_val+1)]
    for i in range(n):
        T[G[i][0]].append(G[i][1])
        T[G[i][1]].append(G[i][0])
    #print(T)
    return T



# G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
# G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]
# G3=[[1,2],[0,3],[0,4,5],[1],[2],[2]]
#print(friends(G3))
G4=[(0,2),(0,1),(1,3),(2,4),(2,5)]
G5=[(0,1),(1,6),(1,5),(2,5),(2,3),(2,4),(3,5),(3,6)]
print(friends(G4))