""" O(V^3) """
from zad2testy import runtests


def opt_sum(A):
    n=len(A)
    inf = float('inf')

    F=[[inf for _ in range(n)]for _ in range(n)]
    sum=[0 for _ in range(n)]
    sum[0]=A[0]

    for i in range(n-1):
        F[i][i+1]=abs(A[i]+A[i+1])
        F[i][i]=0
        sum[i+1]=sum[i]+A[i+1]

    F[n-1][n-1]=0

    #version 1
    def rec(i,j):
        if F[i][j]<inf:
            return F[i][j]

        if i==0:
            s=abs(sum[j])
        else:
            s=abs(sum[j]-sum[i-1])
        for k in range(i,j):
            F[i][j]=min(F[i][j],max(rec(i,k),rec(k+1,j),s))
        return F[i][j]
    ###################
    #version 2 (similar to matrices)
    for j in range(2,n):
        for i in range(n-j):
            for k in range(i,i+j):
                if i==0:
                    s=abs(sum[j])
                else:
                    s=abs(sum[i+j]-sum[i-1])
                    
                a=(F[i][k])
                b=(F[k+1][i+j])
                F[i][i+j]=min(F[i][i+j],max(a,b,s))

    #uncomment next line for version 1
    #rec(0,n-1)

    return (F[0][n-1])

runtests(opt_sum)
A=[-999, -1000, 1001, 1000]
print(opt_sum(A))
