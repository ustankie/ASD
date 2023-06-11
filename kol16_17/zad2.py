def partition(T,p,r,a):
    x=T[a]
    T[a],T[r]=T[r],T[a]
    i=p-1
    for j in range(p,r):
        if T[j]<x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i

def quicksort(T,p,r):
    while p<r:
        q=partition(T,p,r,r)
        if (r-q)<(q-p):
            quicksort(T,q+1,r)
            r=q-1
        else:
            quicksort(T,p,q-1)
            p=q+1
def median_of_medians(T):
    n=len(T)
    if n==1:
        return T[0]
    B=[T[i:i+5]for i in range(0,n,5)]
    #print(B)

    m=len(B)
    for i in range(m):
        quicksort(B[i],0,len(B[i])-1)
    Medians=[B[i][len(B[i])//2]for i in range(m)]
    return median_of_medians(Medians)
def find_x(T,x):
    n=len(T)
    for i in range(n):
        if T[i]==x:
            return i
def select(T,p,r,k):
    if p==r and k==p:
        return T[k]
    if p<r:
        x=median_of_medians(T[p:r+1])
        median=find_x(T,x)
        q=partition(T,p,r,median)
        #print(x,median,q)

        if q==k:
            return T[q]
        if k<q:
            return select(T,p,q-1,k)
        else:
            return select(T,q+1,r,k)

def sum_between(T,a,b):
    n=len(T)
    select(T,0,n-1,a)
    select(T,a+1,n-1,b)
    sum=0
    for i in range(a,b+1):
        sum+=T[i]
    return sum


T=[34,5,65,0,3,6,3,7,56,345,76,9,78,6,5,34]
S=[34,5,65,0,3,6,3,7,56,345,76,9,78,6,5,34]

#quicksort(T,0,len(T)-1)
print(sum_between(S,9,15))
quicksort(T,0,len(T)-1)

print(sum_between(T,9,15))

