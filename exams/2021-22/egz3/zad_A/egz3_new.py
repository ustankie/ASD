from egz3atesty import runtests

def binsearch(T,x):
    i=0
    j=len(T)-1

    while i<j:
        q=(i+j)//2
        if T[q][0]==x:
            return q
        if T[q][0]<x:
            i=q+1
        else:
            j=q-1
    return i

def snow( I,T ):
    n=len(T)

    P=[]
    for i in range(n):
        P.append(T[i][0])
        P.append(T[i][1])

    P.sort()
    #print(P)

    A=[[-float('inf'),0],[P[0],0]]


    for i in range(1,2*n):
        if P[i]!=P[i-1]:
            A.append([P[i],0])

    m=len(A)
    for i in range(n):
        a=binsearch(A,T[i][0])
        b=binsearch(A,T[i][1])
        #print(a,b)
        for j in range(a,b+1):
            A[j][1]+=1
    maxi=0
    for i in range(m):
        maxi=max(maxi,A[i][1])
    #print(A)
    return maxi






# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
T = 100
I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
print(snow(T,I))