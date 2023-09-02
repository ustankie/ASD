def ferry(A,r,l):
    n=len(A)
    l=int(l*100+0.5)
    r=int(r*100+0.5)
    for i in range(n):
        A[i]=int(A[i]*100+.5)
    res=[None for _ in range(n)]
    F=[[None for _ in range(r+1)]for _ in range(n+1)]
    prefix=[0 for _ in range(n+1)]
    prefix[0]=0

    for i in range(1,n+1):
        prefix[i]=prefix[i-1]+A[i-1]

    def rec(i,R):
        L=prefix[i]-R
        if (L>=l and R>=r):
            return i+1
        if i==n-1:
            if L+A[i]<=l:
                res[i]='L'
                return i+1
            if R+A[i]<=r:
                res[i]='R'
                return i+i
            return i

        if F[i][R]!=None:
            return F[i][R]
        if R+A[i]<=r:
            a=rec(i+1,R+A[i])
        else:
            a=0
        if L+A[i]<=l:
            b=rec(i+1,R)
        else:
            b=0
        if a==b==0:
            F[i][R]=0
            return i
        F[i][R]=max(a,b)
        
        if a>b:
            res[i]='R'
        else:
            res[i]='L'
        print(res,a,b,L,R)
        return F[i][R]
    
    a=rec(0,0)
    R=0
    L=0
    for i in range(n):
        if res[i]=='R':
            R+=A[i]
        else:
            L+=A[i]
    
    print(R)
    print(L)
    return a,res


L = 18.24

cars = [3.15, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]



L = 18.24

cars = [3.16, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]

L = 18.24

cars = [15.16, 7.23, 4.98, 2.11, 3.08, 3.92, 6.34, 4.39, 2.63, 1234.88]
res = ferry( cars,L,L)
print(res)
