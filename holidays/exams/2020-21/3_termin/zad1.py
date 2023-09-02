from zad1testy import runtests

def binsearch(A,x):
    i=0
    j=len(A)-1

    while i<=j:
        q=(i+j)//2
        if A[q][0]==x:
            return q

        if A[q][0]<x:
            j=q-1
        else:
            i=q+1
    return i

def find_lis_num(par,F,X,i,R):
    a=binsearch(R,X[i])
    if a==len(R):
        R.append((X[i],i))
        F[i]=len(R)
    else:
        R[a]=(X[i],i)
        F[i]=a+1
        
    if a>0:
        par[i]=R[a-1][1]

def give_result(ind,par,X,res):
    p=ind
    while p!=None:
        res.append(X[p])
        p=par[p]    
    
def mr( X ):
    n=len(X)
    X1=X[::-1]
    F_r=[0 for _ in range(n)]
    F_m=[0 for _ in range(n)]

    par_r=[None for _ in range(n)]
    par_m=[None for _ in range(n)]
    R=[]
    M=[]

    for i in range(n):
        find_lis_num(par_r,F_r,X1,i,R)
        find_lis_num(par_m,F_m,X,i,M)

    res=[]
    MR=0
    if F_r[n-1]>F_m[n-1]:
        MR=F_r[n-1]
        ind=0
    else:
        MR=F_m[n-1]
        ind=n-1
    
    for i in range(1,n-1):
        curr_MR=F_m[i]+F_r[n-i-1]-1
        if curr_MR>MR:
            MR=curr_MR
            ind=i

    if ind==0:
        give_result(n-1,par_r,X1,res)
        return res
    elif ind==n-1:
        give_result(n-1,par_m,X,res)
        return res[::-1]
    
    p=ind
    p=par_m[p]
    give_result(p,par_m,X,res)
    res=res[::-1]

    give_result(n-ind-1,par_r,X1,res)

    return res


runtests( mr )

X=[4,10,5,1,2,3,4]
# X=[1,10,5]
print(mr(X))


