def closure(G):
    n=len(G)

    for t in range(n):
        for x in range(n):
            for y in range(n):
                G[x][y]=G[x][y]or(G[x][t] and G[t][y])
                #G[x][y]|=G[x][t]&G[t][y]
    return G

G=[
    [False, 1, False, False, False, False, 2, False, False], 
    [1, False, 3, False, 3, False, False, False, False], 
    [False, 3, False, False, False, 5, False, False, False], 
    [False, False, False, False, 3, False, False, 1, 8], 
    [False, 3, False, 3, False, 2, 1, False, False], 
    [False, False, 5, False, 2, False, False, False, 1], 
    [2, False, False, False, 1, False, False, 7, False], 
    [False, False, False, 1, False, False, 7, False, False], 
    [False, False, False, 8, False, 1, False, False, False]
 ]
G2=[
    [False, 1, 3, False, False, False], 
    [1, False, False, 5, 8, False], 
    [3, False, False, 4, False, 6], 
    [False, 5, 4, False, 7, 2], 
    [False, 8, False, 7, False, False], 
    [False, False, 6, 2, False, False]
 ]
G3=[
    [False,True,True,False,False,False,False,False,False],
    [True,False,False,False,False,False,False,False,False],
    [True,False,False,True,False,False,False,False,False],
    [False,False,True,False,False,False,False,False,False],
    [False,False,False,False,False,True,False,False,False],
    [False,False,False,False,True,False,True,False,False],
    [False,False,False,False,False,True,False,False,False],
    [False,False,False,False,False,False,False,False,True],
    [False,False,False,False,False,False,False,True,False],
 ]

print(*closure(G3),sep="\n")