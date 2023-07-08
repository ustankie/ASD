from kolutesty import runtests

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

def find(T,i,j,d):
    n=len(T)
    if i==j:
        # print(i)
        # k=i
        # a=select(T,k,0,n-1)
        # print(a)
        # if a==k:
        #     return a,k
        # if a-k<0:
        #     a=select(T,k-1,0,n-1)
        #     if a-k+1>=0:
        #         return a,k
        # if k+1<n:
        #     a=select(T,k+1,0,n-1)
        #     print(a)
        #     if a-k-1>=0:
        #         return a,k
        return -1,i

    
    k=(i+j)//2
    a=select(T,0,n-1,k)
    print(a,k)
    if a-k==0:
        return a,k
    if a-k<0:
        if d!=0:
            a=select(T,0,n-1,k-1)
            print(a,k-1)
            if a-k+1>=0:
                return a,k-1
        return find(T,i,k-1,0)
    if d!=1 and k+1<n:
        a=select(T,0,n-1,k+1)
        print(a,k+1)
        if a-k-1>=0:
            return a,k+1
    return find(T,k+1,j,1)
def ice_cream( T ):
    n=len(T)

    a,k=find(T,0,n-1,-1)
    print(a,k)
    #print(T)
    sum=0
    cnt=0
    for i in range(n):
        if T[i]>=a:
            #print(T[i],sum,cnt)
            sum+=(T[i]-cnt)
            cnt+=1
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( ice_cream, all_tests = True )
T=[11, 16, 5, 6, 15, 12, 9, 18, 11, 16]
#print(select(T,0,0,len(T)-1))
print(ice_cream(T))
