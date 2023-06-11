def sub(A):
    n=len(A)
    F=[1 for _ in range(n)]
    par=[None for _ in range(n)]
    for i in range(2,n):
        for j in range(i):
            if A[j]<A[i] and F[j]+1>F[i]:
                par[i]=j
                F[i] = F[j]+1
    maxi=0
    max_ind=0
    for i in range(n):
        if maxi<F[i]:
            maxi=F[i]
            max_ind=i
    return maxi,max_ind,par

def print_res(par,A,i):
    if par[i]!=None:
        print_res(par,A,par[i])
    print(A[i],end=" ")


A=[2,1,4,3,1,5,2,7,8,3]
maxi,i,par=sub(A)
print(maxi)
print_res(par,A,i)
print()
