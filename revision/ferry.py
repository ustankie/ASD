def map_cars(A, L):
    n = len(A)
    total = 0
    for i in range(n):
        A[i] = int(A[i]*100+0.5)
        total += A[i]
        if total > 2*L:
            return i
    return n


def ferry(A, L):
    m = len(A)
    L = int(L*100+0.5)
    n = map_cars(A, L)

    F = [[[False for _ in range(L+1)]for _ in range(L+1)]for _ in range(m)]
    C=[None for _ in range(m)]
    def recur(i,l,r):
        if i==0:
            if l>=A[0]:
                C[0]='L'
                return True
            if r>=A[0]:
                C[0]='R'
                return True
        if not F[i][l][r]:
            if l-A[i]>=0 and recur(i-1,l-A[i],r):
                F[i][l][r] = True
                C[i]='L'
            if r-A[i]>=0 and recur(i-1,l,r-A[i]):
                F[i][l][r] = True
                C[i]='R'
        return F[i][l][r]
    for i in range(min(m,n-1),-1,-1):
        if recur(i,L,L):
            return i+1,C
    
    return C
    
def ferry2(A, L):
    m = len(A)
    L = int(L*100+0.5)
    n = map_cars(A, L)

    F = [[False for _ in range(L+1)]for _ in range(m)]
    C=[None for _ in range(m)]
    S=[0 for _ in range(n+1)]
    S[n-1]=A[n-1]
    for i in range(n-2,-1,-1):
        S[i]=S[i+1]+A[i]
    endi=0

    def recur(i,l):
        r=L-(S[i+1]-S[endi+1]-(L-l))
        if i==0:
            #r=L-(-(L-l))
            if l>=A[0]:
                C[0]='L'
                return True
            if r>=A[0]:
                C[0]='R'
                return True
        
        #print(r,i,S[i-1])
        if not F[i][l]:
            if l-A[i]>=0 and recur(i-1,l-A[i]):
                F[i][l] = True
                C[i]='L'
            if r-A[i]>=0 and recur(i-1,l):
                F[i][l] = True
                C[i]='R'
        return F[i][l]
    for i in range(min(m,n-1),-1,-1):
        endi=i
        if recur(i,L):
            return i+1,C
    
    return C



L = 18.24

cars = [3.15, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]
# cars=[3,5,6,6]
# start=time()
print(ferry2(cars, L))
# end=time()
# print(end-start)
