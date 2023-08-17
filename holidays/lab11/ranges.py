def min_max(A):
    n=len(A)
    mini=float('inf')
    maxi=-float('inf')

    for i in range(n):
        mini=min(mini,min(A[i]))
        maxi=max(maxi,max(A[i]))
    if mini<0:
        for i in range(n):
            A[i][0]-=mini
            A[i][1]-=mini
        maxi-=mini
    return maxi

def k_ranges(A,k):
    n=len(A)
    m=min_max(A)
    F=[[0 for _ in range(k+1)]for _ in range(m+1)]
    A.sort(key=lambda x: x[1])
    print(A)
    for i in range(n):
        for j in range(k+1):
            F[A[i][1]][j]=max(F[A[i][1]][j],F[A[i][0]][j-1]+(A[i][1]-A[i][0]),F[A[i][1]][j-1])
        print(*F,sep="\n")
        print()
    return F[m][k]

A = [[4, 5], [2, 4], [1, 3], [3, 6], [5, 7], [1, 5], [-5, 2]]
A = [[4.1, 5.2], [2.15, 4.4], [1.5, 3.2], [3.2, 6.83], [5.2, 7.1], [1.2, 5.2], [-5.75, 2.15]]
for i in range(len(A)):
    A[i][0]=int(A[i][0]*100+.5)
    A[i][1]=int(A[i][1]*100+.5)
print(k_ranges(A,2))