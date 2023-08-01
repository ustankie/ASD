def lis(A):
    n=len(A)
    F=[1 for _ in range(n)]
    par=[None for _ in range(n)]
    max_ind=0
    maxi=0

    for i in range(n):
        for j in range(i):
            if A[j]<A[i] and F[j]+1>F[i]:
                F[i]=F[j]+1
                par[i]=j
        if F[i]>maxi:
            max_ind=i
            maxi=F[i]
    print_res(par,max_ind,A)
    return par,maxi,max_ind

def print_res(par,i,A):
    if par[i]!=None:
        print_res(par,par[i],A)
    print(A[i],end=" ")

A= [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
print(lis(A))

