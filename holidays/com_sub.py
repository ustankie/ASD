def print_solution(F,A,B):
    n=len(A)
    m=len(B)

    i=n-1
    j=m-1

    R=[]

    while i>=0 and j>=0:
        if A[i]==B[j]:
            R.append(A[i])
            i-=1
            j-=1
        elif F[i-1][j]==F[i][j]:
            i-=1
        else:
            j-=1



    return (R[::-1])
def com_sub(A,B):
    n=len(A)
    m=len(B)

    F=[[0 for _ in range(m)]for _ in range(n)]

    if A[0]==B[0]:
        F[0][0]=1
    
    for i in range(1,n):
        if F[i-1][0] or B[0]==A[i]:
            F[i][0]=1

    for j in range(1,m):
        if F[0][j-1] or A[0]==B[j]:
            F[0][j]=1

    for i in range(1,n):
        for j in range(1,m):
            if A[i]==B[j]:
                F[i][j]=max(F[i-1][j-1]+1,F[i][j])
            else:
                F[i][j]=max(F[i][j],F[i-1][j],F[i][j-1])
    return F[n-1][m-1],print_solution(F,A,B)

def filter(B):
    n=len(B)
    R=[B[0]]

    for i in range(1,n):
        if B[i]!=B[i-1]:
            R.append(B[i])
    return R

def lis(A):
    n=len(A)
    if n==0:
        return 0,[]
    B=sorted(A)
    B=filter(B)
    print(A,B)
    return com_sub(A,B)

a = "ababaaabsbininm"
b = "jmjkbkjkv"

print(com_sub(a, b))  

a = [67, 42, 61, 2, 77, 9, 45, 96, 32, 27, 47, 20]
print(lis(a))