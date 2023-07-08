from kolutesty import runtests

def swaps( disk, depends ):
    n = len(disk)
    to_do1 = [0]*n
    to_do2 = [0]*n
    roots1 = [[], []]
    roots2 = [[], []]
    G = [[] for _ in range(n)] # G to graf zależności, dla każdego pliku wpisane są pliki, które zależą od niego

    def DFSvisit(graph, to_do, roots, vert, case, flag): #flag to indeks przeciwnej dyskietki w roots
        for j in range(len(graph[vert])):
            neigh = graph[vert][j]
            to_do[neigh] -= 1
            if to_do[neigh] == 0:
                if disk[neigh] == case:
                    DFSvisit(graph, to_do, roots, neigh, case, flag)
                else:
                    roots[flag].append(neigh)

    for i in range(n):
        leng = len(depends[i])
        to_do1[i] = to_do2[i] = leng

        if leng == 0:
            if disk[i] == 'A':
                roots1[0].append(i)
                roots2[0].append(i)
            else:
                roots1[1].append(i)
                roots2[1].append(i)
        else:
            for j in range(leng):
                G[depends[i][j]].append(i)
    
    sum1 = -1
    while roots1[0] or roots1[1]:
        if roots1[0]:
            sum1 += 1
            for j in range(len(roots1[0])):
                root = roots1[0][j]
                DFSvisit(G, to_do1, roots1, root, 'A', 1)
            roots1[0] = []
        elif roots1[1]:
            sum1 += 1
            for j in range(len(roots1[1])):
                root = roots1[1][j]
                DFSvisit(G, to_do1, roots1, root, 'B', 0)
            roots1[1] = []
    
    sum2 = -1
    while roots2[0] or roots2[1]:
        if roots2[1]:
            sum2 += 1
            for j in range(len(roots2[1])):
                root = roots2[1][j]
                DFSvisit(G, to_do2, roots2, root, 'B', 0)
            roots2[1] = []
        elif roots2[0]:
            sum2 += 1
            for j in range(len(roots2[0])):
                root = roots2[0][j]
                DFSvisit(G, to_do2, roots2, root, 'A', 1)
            roots2[0] = []
    
    return (sum1 if sum1 < sum2 else sum2)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )