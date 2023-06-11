def print_sub(F,A,B,i,j):
    if i<0 or j<0:
        return ""
    if i==0:
        if F[i][j]:
            return A[i]
        return ""
    if j==0:
        if F[i][j]:
            return B[j]
        return ""
    if F[i][j]==F[i-1][j-1]+1 and A[i]==B[j]:
        return print_sub(F,A,B,i-1,j-1) + A[i]
    if F[i-1][j]>F[i][j-1]:
        return print_sub(F,A,B,i-1,j)
    else:
        return print_sub(F,A,B,i,j-1)

def print_sub2(F,A,B):
    a=len(A)
    b=len(B)
    i=a-1
    j=b-1
    W=""

    while i>0 and j>0:
        if F[i-1][j]==F[i][j]:
            i-=1
        if j>0 and F[i][j-1]==F[i][j]:
            j-=1
        if i>0 and j>0 and F[i-1][j]!=F[i][j] and F[i][j-1]!=F[i][j]:
            W+=(A[i])
            i-=1
            j-=1

    for i in range(a):
        if F[i][0]:
            W+=A[i]
            break
    else:
        for j in range(b):
            if F[0][j]:
                W+=B[j]
                break
    return W[::-1]

    

def com_sub(A,B):
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

a = "ababaaabsbininm"
b = "jmjkbkjkv"
print(com_sub(a, b))        