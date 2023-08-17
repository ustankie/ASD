def tree_path(G,C,s):
    n=len(G)
    par=[None for _ in range(n)]
    maximum=0
    max_path1=-float('inf')
    max_path2=-float('inf')

    def rec(u):
        a=-float('inf')
        nonlocal maximum
        max_path1=-float('inf')
        max_path2=-float('inf')
        for v in G[u]:
            par[v]=u
            if v!=par[u]:
                b=rec(v)
                a=max(a,b)
            if a>max_path1:
                max_path2=max_path1
                max_path1=b
            elif a>max_path2:
                max_path2=b

        maximum=max(maximum,max_path1+max_path2+C[u])
        if a==-float('inf'):
            a=0
        #print(max(0,a+C[u]),u,maximum,max_path1,max_path2)
        return max(0,a+C[u])

    for u in G[s]:
        par[u]=s
        a=rec(u)
        #print(a,u)
        if a>max_path1:
            max_path2=max_path1
            max_path1=a
        elif a>max_path2:
            max_path2=a
        maximum=max(maximum,max_path1+max_path2+C[s])
    return maximum

G=[[1,2,3,4],
   [0,5,6],
   [0,7],
   [0],
   [0,8,9,10,11],
   [1],
   [1],
   [2,12,13,14],
   [4],
   [4],
   [4,15],
   [4],
   [7],
   [7],
   [7],
   [10]
    
]

C=[20,5,-20,15,-10,30,-20,1,18,23,-20,-15,30,22,-15,100]

G=[[1,2,13],
   [0,3],
   [0,4,5],
   [1,6,7],
   [2],
   [2,8,9],
   [3,10],
   [3,11],
   [5],
   [5],
   [6,12],
   [7],
   [10],
   [0,14],
   [13]

]
C=[10,7,-5,8,-100,2,1,-7,20,7,-5,1,-4,-4,-8]

print(tree_path(G,C,0))