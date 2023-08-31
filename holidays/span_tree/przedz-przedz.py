from math import log2
#suma na przedziale
def seg_tree(T,assigns,queries):
    n=len(T)
    _n=1<<(1+int(log2(n-1)))

    ST=[0 for i in range(2*_n)]
    lazy=[0 for i in range(2*_n)]

    for i in range(n):
        ST[i+_n]=T[i]

    for i in range(_n-1,0,-1):
        ST[i]=ST[2*i]+ST[2*i+1]
    
    def push(i,mult):
        if not lazy[i]:
            return
        ST[2*i]+=lazy[i]*mult
        ST[2*i+1]+=lazy[i]*mult
        
        lazy[2*i]+=lazy[i]
        lazy[2*i+1]+=lazy[i]
        lazy[i]=0
        

    def range_assign(a,b,k,ka,kb,x):
        if b<ka or a>kb:
            return
        if a<=ka and b>=kb:
            ST[k]+=x*(kb-ka+1)
            lazy[k]+=x
            return
        push(k,(kb-ka+1)//2)
        mid=(ka+kb)//2
        range_assign(a,b,2*k,ka,mid,x)
        range_assign(a,b,2*k+1,mid+1,kb,x)
        ST[k]=(ST[2*k]+ST[2*k+1])
    
    def query(a,b,k,ka,kb):
        if b<ka or a>kb: 
            return 0
        if a<=ka and b>=kb:
            return ST[k]
        push(k,(kb-ka+1)//2)
        mid=(ka+kb)//2
        a1=query(a,b,2*k,ka,mid)
        a2=query(a,b,2*k+1,mid+1,kb)

        return a1+a2
    

    q=len(queries)
    ass=len(assigns)
    for i in range(q):
        a,b=queries[i]
        print(query(a,b,1,0,_n-1))

    for i in range(ass):
        a,b=assigns[i][0]
        x=assigns[i][1]
        range_assign(a,b,1,0,_n-1,x)
    
    print(ST)
    
    for i in range(q):
        a,b=queries[i]
        print(query(a,b,1,0,_n-1))

T=[0,7,5,3,1,8,6,12,3]
assigns=[[(2,5),6],[(7,8),2]]
queries=[(0,2),(6,8)]

seg_tree(T,assigns,queries)
