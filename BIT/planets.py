def bin(T,n):
    i=1
    B=[0 for _ in range(n)]
    j=0
    while i<n:
        B[j]=i
        i*=2
        j+=1
        f=[[0 for _ in range(n)] for i in range(n)]
        for v in range(n):
            f[0][v]=v
            f[1][v]=T[v]
    for k in B:
        for v in range(2,n-k):
            f[k][v]=f[k//2][f[k//2][v]]
            print(f[k][v])



n,q=list(map(int, input().split(' ')))

T = list(map(int, input().split(' ')))
Q=[[0,0]for _ in range(q)]
for i in range(q):
    Q[i]=list(map(int, input().split(' ')))
