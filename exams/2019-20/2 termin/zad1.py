from zad1testy import runtests


def zbigniew(A):
    n=len(A)
    F=[[float('inf')for _ in range(n)]for _ in range(n)]
    
    # for i in range(n):
    #     F[0][i]=0
    F[0][0]=0

    for i in range(n):
        for j in range(n):
            k=i+1
            ind=min(n-1,j-(k-i)+A[i])
            while k<n and ind>=0:               
                F[k][ind]=min(F[k][ind],F[i][j]+1)
                k+=1
                ind=min(n-1,j-(k-i)+A[i])
    #print(*F,sep="\n")
    return min(F[n-1])




runtests(zbigniew)
A = [2, 2, 1, 0, 0, 0]
print(zbigniew(A))