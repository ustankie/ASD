def partition(T,l,r,a):
    x=T[a]
    T[a],T[r]=T[r],T[a]
    i=l-1
    for j in range(l,r):
        if T[j]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    #print(T)
    return i

def partition2(T,l,r,a):
    x=T[a][0]
    i=l-1
    for j in range(l,r):
        if T[j][0]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[a],T[i]=T[i],T[a]
    return i


def quick_sort2(T,l,r):
    while l<r:
        q=partition2(T,l,r,r)
        if (q-l)<(r-q):
            quick_sort2(T,l,q-1)
            l=q+1
        else:
            quick_sort2(T,q+1,r)
            r=q-1
def quick_sort(T,l,r):
    while l<r:
        q=partition(T,l,r,r)
        if (q-l)<(r-q):
            quick_sort(T,l,q-1)
            l=q+1
        else:
            quick_sort(T,q+1,r)
            r=q-1


def median_of_medians(T,a=True):
    n=len(T)
    if n==1:
        return T[0]
    
    fives=[T[i:i+5]for i in range(0,n,5)]

    if a:
        for i in range(n):
            fives[i//5][i%5]=T[i],i
    

    m=len(fives)
    for i in range(m):
        quick_sort2(fives[i],0,len(fives[i])-1)

    medians=[fives[i][len(fives[i])//2] for i in range(m)]

    return median_of_medians(medians,False)

def select(T,p,r,k):
    if p==r and p==k:
        return T[p]
    if p<r:
        m=median_of_medians(T[p:r+1])
        q=partition(T,p,r,m[1]+p)
        if q==k:
            return T[q]
        if k>q:
            return select(T,q+1,r,k)
        else:
            return select(T,p,q-1,k)

    

T=[1,24,5,41,0,4,90,67,90,78,57,3,0,1]
n=len(T)
for i in range(n):
    T[i]=(T[i],i)

print(select(T,0,len(T)-1,5))
quick_sort(T,0,len(T)-1)
print(T)