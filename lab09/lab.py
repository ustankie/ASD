#pytania: ociepka@agh.edu.pl
#1) implementacja forda-fulkersona v
#2) znaleźć maksymalny przepływ w grafie nieskierowanym -> przerobić na skierowany (obie nowe krawędzie mają wagę pierwotnej)
#   -> w reprezentacji macierzonwej od razu tak jest, listowej też v
#3) mamy gotowy algorytm forda-fulkersona, mamy wiele źródeł i wiele ujść -> dodajemy wspólne źródło i wspólne ujście -> implementacja redukcji,dana lista tupli v
#4) spójność krawędziowa - ile minimalnie krawędzi trzeba zniszczyć, żeby go rozspójnić -> graf o wagach 1,ff, wybieramy jedno źródło, musimy sprawdzić wszystkie ujścia
#   (w grafie skierowanym trzeba sprawdzić każdy z każdym)
#5) skojarzenie - dodajemy źródło do jednego ze zbiorów, ujście do drugiego,ff -> poprawne bo do każdego wierzchołka z A wchodzimy maksymalnie raz
#   i z każdego z B wychodzimy maksymalnie raz
#6) znaleźć skojarzenie w drzewie - graf dwudzielny - na każdym poziomie "zmienia się kolor" -> BFS: dzielimy na zbiory,ff
#7) dany graf skierowany, maksymalna liczba ścieżek, które nie dzielą między sobą wierzchołków -> każdy wierzchołek dzielimy na dwa, do jednego wchodzą, 
#   z drugiego tylko wychodzą krawędzie, pomiędzy nimi dwie krawędzie - jedna o wadze 1, druga o wadze 0, reszta krawędzi w grafie skierowanym ma wagę 1, s i t może zostać
#8) formuły logiczne (określić wartościowanie -> wart poszczególnych zmiennych - normalnie problem NP trudny)
#   -> postać normalna koniunkcyjna, każda zmienna występuje dokładnie dwa razy (raz z negacją, raz be) -> krawędź skierowana w grafie to implikacja
#   (mamy więcej zmiennych niż alternatyw), skojarzenie maksymalne pomiędzy A={a,~a,...} B=((a v b),(b v ~c),...) -> bierzemy te krawędzie, które są w maksymalnym skojarzeniu
#   lub: b) wierzchołkami klauzule, wagi - zmienne bez negacji, trzeba nadać skierowanie tak, by na każdy wierzchołek wskazywała przynajmniej jedna krawędź, 
#   jeśli mamy drzewo, to nie da się znaleźć takiego wartościowania, jeśli cykl, to łączymy w kółko, zamieniamy cykl w wierzchołek i uruchamiamy DFS

#by me: 4) lista krawędzi do usunięcia
#1) (reprezentacja macierzowa) -> warto skopiowac graf
from copy import deepcopy #copy kopiuje tylko na jednym poziomie zagnieżdżenia, deepcpy wszystko
from collections import deque
def BFS(G,s,t):
    Q=deque()
    path=[]

    return path

def capacity(G,path):
    min_cap=G[path[0][path[1]]]
    n=len(path)
    for i in range(1,n-1):
        min_cap=min(G[pacth[i],path[i+1],min_cap])
    return min_cap

def update(G,path):
    w=capacity(G,path)
    n=len(path)
    for i in range(n-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w

def ff(G,s,t):
    flow=0
    G2=deepcopy(G)
    path=BFS(G2,s,t)
    while path:
        flow+=capacity(G,path)
        update(G2,path)
        path=BFS(G2,s,t)
    return flow

#3) 
def multi_ff(G,sources,sinks):
    n=len(G)
    G=deepcopy(G) #też działa

    G.append([0 for _ in range(n+2)])
    G.append([0 for _ in range(n+2)])

    for i in range(n):
        G[i].append(0)
        G[i].append(0) #lub G[i].extend([0,0])
    for u,c in sources:
        G[n][u]=c
    for v,c in sinks:
        G[v][n+1]=c
    
    return ff(G,n,n+1)

