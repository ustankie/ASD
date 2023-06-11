from copy import deepcopy
def partition(T,a,b):
    x=T[b]
    i=a-1
    j=b
    for j in range(a,b):
        if T[j]<x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[i],T[b]=T[b],T[i]
    return i

def quick_sort(T,i,j):
    while i<j:
        q=partition(T,i,j)
        if j-q>q-i:
            quick_sort(T,i,q-1)
            i=q+1
        else:
            quick_sort(T,q+1,j)
            j=q-1
def filter(A):
    n=len(A)

    B=[]
    B.append(A[0])
    for i in range(1,n):
        if A[i-1]!=A[i]:
            B.append(A[i])
    return B

def ascend(A):
    n=len(A)    
    if n==0:
        return 0,[]
    B=deepcopy(A)
    quick_sort(B,0,n-1)
    B=filter(B)
    print(B)
    return com_sub(A,B)
    
def print_sub2(F,A,B):
    a=len(A)
    b=len(B)
    i=a-1
    j=b-1
    W=[]

    while i>0 and j>0:
        if F[i-1][j]==F[i][j]:
            i-=1
        if j>0 and F[i][j-1]==F[i][j]:
            j-=1
        if i>0 and j>0 and F[i-1][j]!=F[i][j] and F[i][j-1]!=F[i][j]:
            W.append(A[i])
            i-=1
            j-=1

    for i in range(a):
        if F[i][0]:
            W.append(A[i])
            break
    else:
        for j in range(b):
            if F[0][j]:
                W.append(B[j])
                break
    return W[::-1]

    

def com_sub(A,B):
    if len(A)==0 or len(B)==0:
        return 0,[]
    a=len(A)
    b=len(B)
    F=[[0 for _ in range(b)]for _ in range(a)]

    F[0][0]=int(A[0]==B[0])
    for i in range(1,a):
        if F[i-1][0] or B[0]==A[i]:
            F[i][0]=1
    for j in range(1,b):
        if F[0][j-1] or A[0]==B[j]:
            F[0][j]=1

    
    for i in range(1,a):
        for j in range(1,b):
            if A[i]==B[j]:
                F[i][j]=F[i-1][j-1]+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
                
    return F[a-1][b-1],print_sub2(F,A,B)


a = [67, 42, 61, 2, 77, 9, 45, 96, 32, 27, 47, 20]
print(ascend(a))

