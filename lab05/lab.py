#1) a) algorytm sprawdzający, czy graf jest dwudzielny (BFS) v
#   b) Liczba skladowych w grafie (DFS)     v
#reprezentacja: macierz sąsiedztwa
#2) Staje nadawcze - chcemy je wylaczac tak, by miec ciagle spojny graf -> z uzyciem BFS -> po kolei zapisujemy elementy w liście, na koniec odwracamy v
#3)Dany jest graf jako macierz sąsiedztwa. Czy istnieje cykl o długości 4?
#   a)O(v^4) -> sprawdzamy wszystkie czwórki wierchołków czy są połączone v 
#   b)O(v^3) -> 1) Rozważamy wszystkie pary wierzcholkow -> jesli x i y maja wspolnych dwoch sasiadow -> przechodzimy po macierzy sąsiedztwa/BFS dla każdego wierzchołka v
#4) (Graf skierowany w postaci maxierzy sasiedztwa) Znależć uniwersalne ujście t- z każdego w istnieją krawedzie do ujscia, z samego ujscia nie wychodza krawedzie 
#   a) znalezc wiersz o samych zerach i kolumne o jedynkach O(n^2)
#   b) chodzimy w prawo i w lewo po macierzy sasiedztwa O(n) -> wystarczy jedno przejście v
#5) Znaleźć najkrótszą ścieżkę miedzy s i k w grafie nieskierowanym (BFS), def spath(G,s,k) v
#6) Dana jest szachownica n x n, każde pole ma koszt {1...5}, król w lewym górnym rogu, ma przejść w prawy dolny z jak najmniejszym kosztem -> return min koszt
# -> do kolejki BFS wrzucamy pare wiezcholek, wartosc/zmniejszamy wart v
#7)Malejące krawędzie - G=(V,E) nieskierowany, koszty krawędzi {1...|E|} s->t po krawędziach o coraz mniejszych wagach -> DFS -> nie sprawdzamy visited, sprawdzamy czy koszt mniejszy v
#8)Graf G=(V,E) reprezentuje mapę drogową krajów -> koszty przejazdów 0 lub 1 najmniejszy koszt między s i t-> zwijać krawędzie z 0, BFS -nieprzyjemne/wchodzimy do wszystkich możliwych zer, potem do jedynek, do zer itd
#w kolejce priorytetyzujemy zera tak, by zostały obsłużone przed jedynkami v

#1) a)
from collections import deque

def bipartite(G):
    n=len(G)
    colors=[-1 for v in range(n)]
    Q=deque()
    s=0
    Q.append(s)
    colors[s]=1
    while (len(Q))>0:
        v=Q.popleft()
        for i in G[v]:
            if colors[i]==(-1):
                colors[i]=(colors[v]+1)%2
                Q.append(i)
            elif colors[i]==colors[v]:
                    return False
    return True

#1) b)
def consistent(G):
    n=len(G)
    visited=[0 for _ in range(n)]
    #parent=[None for _ in range(n)]
    def DFSvisit(G,u):
        #nonlocal time
        visited[u]=True
        for v in G[v]:
            if visited[x]:
                continue
            DFS(G,x)
    for i in range(n):
        if not visited[i]:
          l+=1
          DFS(i)
    return l
#2) b)
def cycle(G):
    n=len(G)
    for i in range(n):
        for j in range(n):
            c=0
            for k in range(n):
                if G[i][k] and G[j][k]:
                    c+=1
                if c==2:
                    return True
    return False
#5)
def spath(G,s,k):
    n=len(G)
    visited=[-1 for v in range(n)]
    parent=[None for v in range(n)]
    Q=deque()
    Q.append(s)
    colors[s]=1
    while (len(Q))>0:
        v=Q.popleft()
        for i in G[v]:
            if visited[i]==(-1):
                visited[i]=1
                parent[i]=v
                Q.append(i)

    t=[k]
    while parent[k]!=None:
        t.append(parent[k])
        k=parent[k]
    
    return reverse(t)

#6)
def king(G,s):
    n=len(G)
    visited=[-1 for v in range(n)]
    parent=[None for v in range(n)]
    D=[0 for _ in range(n)]
    Q=deque()
    Q.append((s,0))
    while (len(Q))>0:
        v,c=Q.popleft()
        for x in G[v]:

            if visited[x]==(-1):
                if c==1:
                    visited[x]=1
                    parent[x]=v
                    Q.append(x)
                else:
                    Q.append((x,c-1))
                    D[x]+=1
 
    return min(D)
G=[[1,2,4],[9,3,5],[8,7,6]]
print(king(G,0))
