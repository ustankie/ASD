def truck(A,k):
    n=len(A)
    A.sort(reverse=True)
    #print(A)

    load_sum=0
    R=[]

    for i in range(n):
        if A[i]<=k:
            load_sum+=1
            R.append(A[i])
            k-=A[i]

    return load_sum,R



W = [2, 2, 4, 8, 1, 8, 16]
k = 27

print(truck(W, k))

