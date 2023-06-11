def radix_sort(T):
    n=len(T)
    S=[0 for i in range(n)]
    R=[0 for i in range(n)]

    for i in range(n):
        S[T[i]%n]+=1
    for i in range(1,n):
        S[i]+=S[i-1]
    for i in range(n-1,-1,-1):
        R[S[T[i]%n]-1]=T[i]
        S[T[i]%n]-=1
    print(R)
    S=[0 for i in range(n)]
    for i in range(n):
        S[R[i]//n]+=1
    for i in range(1,n):
        S[i]+=S[i-1]
    for i in range(n-1,-1,-1):
        T[S[R[i]//n]-1]=R[i]
        S[R[i]//n]-=1

T=[24,1,2,6,14]
radix_sort(T)
print(T)