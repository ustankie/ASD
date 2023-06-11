#1) znaleźć ścieżkę Hamiltona w DAG w grafie acyklicznym skierowanym -> sortujemy topologicznie, 
#   sprawdzamy czy po posortowaniu istnieją krawędzie między każdymi dwoma kolejnymi wierzchołkami (sortowanie topologiczne -> porządek częściowy) v
#2) dobry początek -> czy w grafie acyklicznym istnieje wierzcholek v, z ktorego istnieje sciezka do kazdego innego w(może ich być więcej)  v
#   szukamy wszystkich spójnych składowych, sortujemy topologicznie graf z odwróconymi krawędziami -> ostatni wierzchołek to dobry początek
#   b)na kazdym wierzcholku DFS
#   c)DFS, kolejność postorder, w tablicy zapisujemy czas przetworzenia -> jako potencjalny dobry poczatek sprawdzamy przetworzony jako ostatni -> inaczej nie ma dobrego początku
#   lub oznaczanie w visited fal DFS
#3) Problem przewodnika turystycznego: dzielenie grupy turystów na kilka autobusów (chcemy przejechac miedzy dwoma punktami), w miescie duzo ulic(graf nieskierowany),
#  kazda ma wage, jak duze autobusy tam jezdza -> na ile min grup podzielic n osob zeby przejechac z a do b -> BFS z tablica visited na krawedzie -> w wierzcholki 
# -> wszystkie grupy ta sama trasa
#   
#   wpisujemy min koszt wejscia do kazdego w ->(V weight, E weight)
#   b)sortujemy krawedzie po wagach malejaco, scalamy w, ktore polaczone juz tymi samymi krawedziami(spojne skladowe), 
#   sety, jesli nagle da sie przejechac miedzy s i t (są razem w secie)-> uczynila to nowododana krawedz,
#   dzielimy na grupy -> struktura find union
#   c) wyszukiwanie binarne n//2 BFS/DFS , n//4,n//8
#4) Cykl Eulera -> czy istnieje, wypisac v
#5) Czy mosty w grafie? v
#6) państwo - każde miasto ma dwie bramy - płn i płd -> jesli weszlismy pld, to musimy wyjsc pln i na odwrot
#   oazy, istnieja drogi, przechodzace przez 0 lub wiecej oaz -> z kazdego miasta wychodzi dokladnie jedna droga, oazy polaczone jakkolwiek
#   Bajtocja, król Bajtocji wysyła gońca, do kazdego miasta dokladnie raz, oazy jakkolwiek -> wyznaczamy trase gonca (tylko w jakiej kolejnosci miasta)-> transpozycja grafu, 
#   wierzcholki jako kr, kr jako w
#   Łączymy oazy w jeden w (DFS?), potem miasta zamieniamy w krawedzie, krawedzie laczace miasta zamieniamy w wierzcholki -> cykl eulera/koszty autostrad 0/1 z poprzednich lab
#ociepka@agh.edu.pl

#1) 
def DFS(G,s,vis,A):
    vis[s]=True
    for v in G[s]:
        if not vis[v]:
            DFS(G,v,vis,A)
    A.append(s)
def Hamilton(G):
    A=[]
    n=len(G)
    vis=[False for _ in range(n)]
    for i in range(n):
        if not vis[i]:
            DFS(G,i,vis,A)
    A.reverse()
    for i in range(n-1):
        u=A[i]
        v=A[i+1]
        if not v in G[u]:
            return False
    return True

#2)
def DFS2(G,s,vis,time):
    vis[s]=time
    for v in G[s]:
        if not vis[v]:
            DFS2(G,v,vis,time)
        
def good_beginning(G):
    #A=[]
    n=len(G)
    vis=[0 for _ in range(n)]
    time=1
    last=1
    for i in range(n):
        if not vis[i]:
            DFS2(G,i,vis,time)
            time+=1
            last=i
    max_ind=0
    max_w=i
    vis=[0 for _ in range(n)]
    DFS2(G,last,vis,time)
    # for v in range(n):
    #     if vis[v]>max_ind:
    #         max_ind=vis[v]
    #         max_w=v
    for i in vis:
        if not i:
            return False
    return True

G=[[1,2],[2,4],[],[],[3,6,5],[],[]]
G2=[[]]
print(good_beginning(G))


    
