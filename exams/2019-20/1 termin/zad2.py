""" O(V^3) """
from zad2testy import runtests


def opt_sum(A):
    n=len(A)
    F=[[float('inf')for _ in range(n)]for _ in range(n)]
    sum=[0 for _ in range(n)]
    sum[0]=A[0]

    F[0][0]=0
    for i in range(1,n):
        sum[i]=sum[i-1]+A[i]
        F[i-1][i]=abs(A[i-1]+A[i])
        F[i][i]=0

    def rec(i,j):
        if F[i][j]<float('inf'):
            return F[i][j] 
           
        if i==0:
            s=abs(sum[j])
        else:
            s=abs(sum[j]-sum[i-1])
        for k in range(i,j):
            F[i][j]=min(F[i][j],max(rec(i,k),rec(k+1,j),s))
        return F[i][j]
    
    rec(0,n-1)
   
    return F[0][n-1]
            

runtests(opt_sum)
A=[-999, -1000, 1001, 1000]
print(opt_sum(A))
