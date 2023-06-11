    G = [ set() for i in range(n) ]
    for i in range(r):
        u = MY_random() % n
        v = MY_random() % n
        G[u].add(v)
        G[v].add(u)
    
    for _ in range(k):
        u = 0
    for __ in range(l-1):
        v = MY_random() % (n-1)
        G[u].add(v)
        G[v].add(u)
        u = v
    v = n-1
    G[u].add(v)
    G[v].add(u)
    
    GG = [ list(G[i]) for i in range(n) ]
    print([GG, 0, n-1], hint) 

    exit()