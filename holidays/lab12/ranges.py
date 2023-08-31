def ranges(A):
    n=len(A)
    A.sort()

    count=1
    curr=A[0]
    for i in range(1,n):
        if A[i]>curr+1:
            curr=A[i]
            count+=1
    return count



A =[-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]
print(ranges(A))