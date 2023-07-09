def ranges(A):
    n=len(A)
    A.sort()
    F=[0 for _ in range(n)]

    F[0]=1
    min_range=A[0]

    for i in range(1,n):
        if A[i]<=min_range+1:
            F[i]=F[i-1]
        else:
            min_range=A[i]
            F[i]=F[i-1]+1
    return F[n-1]

A =[-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]
print(ranges(A))