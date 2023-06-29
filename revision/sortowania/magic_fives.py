def selection_sort(T):
    n=len(T)
    for i in range(n-1):
        nm=i
        for j in range(i+1,n):
            if T[nm]>T[j]:
                nm=j
        T[nm],T[i]=T[i],T[nm]
    
def magic_fives(T):
    n=len(T)
    if n==1:
        return T[0]
    B=[T[i:i+5]for i in range(0,n,5)]
    b=len(B)
    M=[0 for i in range(b)]
    for i in range(b):
        selection_sort(B[i])
        M[i]=B[i][len(B[i])//2]

    return magic_fives(M)

def find_position(T,x):
    n=len(T)
    for i in range(n):
        if T[i]==x:
            return i

def partition(T,p,k,y):
    T[k],T[y]=T[y],T[k]
    x=T[k]
    i=p-1
    for j in range(p,k):
        if T[j]<x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[k],T[i]=T[i],T[k]
    return i

def select(T,i,j,k):
    if i==j and i==k:
        return T[k]
    if i<j:
        p=find_position(T,magic_fives(T[i:j+1]))
        q=partition(T,i,j,p)
        if q==k:
            return T[k]
        if q<k:
            return select(T,q+1,j,k)
        else:
            return select(T,i,q-1,k)
    
T=[1,24,5,41,0,4,90,67,90,78,57,3,0,1]

print(select(T,0,len(T)-1,0))
selection_sort(T)
print(T)





