#1) v implementacja: domknięcie przechodnie grafu (rep. macierzowa) - jeśli istnieje ścieżka z x do y, to istnieje krwędź z x do y -
# - Floyd Warshall v
#2) v Implementacja: Kruskal (sort,find/union dane) v
#3) v G=(V,E) - graf skierowany, ważony -> obliczyć wagę cyklu o min wadze (jeśli nie ma cyklu, zwraca inf) - 
#   nie wpisujemy odleglosci 0 dla pierwszego wierzchołka, algorytm Floyda-Warshalla v
#4) v czas budowy autostrad -> między dowolną parą miast ma się dać jechać, ale różnica między czasem budowy najwcześniejszej i najpóźniejszej ma być najmniejszy -
# - sortujemy krawedzie po dlugosci, próbujemy każdego ciągu krawędzi, DFS z każdego wierzchołka O(E^3)
# - sortujemy krawędzie, znajdujemy MST od każdego vi w kolejności i    sprawdzamy czy działa (znajdujemy dla danego vi najmniejsze spojne drzewo find/union) O(E^2log*E) v
# - O(E^2): budujemy MST, przesuwamy się oknem -> DFS czy spójne, jeśli tak -> rozw, nie -> szukamy polaczenia miedzy dwoma drzewami 
#5) v Przewodnik turystyczny - s,t, autobusy, przepustowość krawędzi, chcemy znaleźć trasę z s do t o przepustowości max (bez DFS/BFS) - odwrotny kruskal v
#6) v Transport atomowy - s,t, graf ważony - odleglosc miedzy wierzcholkami to najkrotsza trasa miedzy nimi, z s rusza 1 do t, z t 2 do s, robią kroki na zmiane o jedno pole, v
# nie mogą się znaleźć bliżej niż d od siebie
# 1. Floyd-Warshall
# 2. budujemy graf, w którym pary wierzchołków u,v, istnieje krawędź, jeśli się da przejść (u,v')/(u',v)
# 3. DFS - patrzymy czy jest ścieżka z s do t albo na odwrót
#7) formula logiczna w postaci koniunkcyjnej normalnej, kazda zmienna wystepuje dokladnie dwa razy -> sprawdzić czy spełnialna - algorytm wybiera wartosci

#1)
def closure(G):
    n=len(G)
    for t in range(n):
        for x in range(n):
            for y in range(n):
                G[x][y]=G[x][y]or(G[x][t] and G[t][y])
    return G

#2)
def kruskal(E,n):
    A=[]
    V=[Node(i) for i in range(n)]
    E.sort()
    for e in E:
        u,v,w=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A+=e
    return A