from math import log2
def przedz_pkt(T,queries):
    n=len(T)
    _n=1<<(1+int(log2(n-1)))
    print(n,_n)

    ST=[0 for _ in range(2*_n)]

    for i in range(n):
        ST[i+_n]=T[i]
    
    # for i in range(_n-1,0,-1):
    #     ST[i]=ST[2*i]+ST[2*i+1]
    
    def query(a):
        sum=0
        a+=_n
        while a>0:
            sum+=ST[a]
            a//=2
        return sum
    
    def update(a,b,c):
        a+=_n
        b+=_n

        while a<=b:
            if a%2==1:
                ST[a]+=c
                a+=1
            if b%2==0:
                ST[b]+=c
                b-=1
            a//=2
            b//=2
    
    q=len(queries)
    for i in range(q):
        if queries[i][0]=='u':
            u,a,b,c=queries[i]
            update(a,b,c)
        else:
            u,a=queries[i]
            print(query(a))


T=[5,3,4,8]
queries=[('q',2),('q',1),('u',0,2,3),('q',2),('q',3),('u',1,3,6),('q',2)]

przedz_pkt(T,queries)