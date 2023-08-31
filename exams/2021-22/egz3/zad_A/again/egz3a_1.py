from egz3atesty import runtests
from math import log2
def map_snow(I):
    n=len(I)
    R=[]
    for i in range(n):
        R.append(I[i][0])
        R.append(I[i][1])
    
    R.sort()
    S=[R[0]]
    for i in range(1,2*n):
        if R[i]!=R[i-1]:
            S.append(R[i])
    return S

def binsearch(A,x):
    n=len(A)
    i=0
    j=n-1

    while i<=j:
        q=(i+j)//2
        if A[q]==x:
            return q
        if A[q]>x:
            j=q-1
        else:
            i=q+1
    return i


def snow( T,I ):
    n=len(I)
    

    S=map_snow(I)
    s=len(S)
    # print(S)
    _n=1<<(1+int(log2(s-1)))
    ST=[0 for _ in range(2*_n)]

    def update(a,b,c):
        # print(a,b,_n)
        a=binsearch(S,a)
        b=binsearch(S,b)
        a+=_n
        b+=_n
        while a<=b:
            if a%2==1:
                ST[a]+=c
                a+=1
            if b%2==0:
                # print(b)
                ST[b]+=c
                b-=1
            a//=2
            b//=2

    def query(a):
        sum=0
        a+=_n
        while a>0:
            sum+=ST[a]
            a//=2
        return sum
    
    for i in range(n):
        update(I[i][0],I[i][1],1)
    
    max_snow=0
    for i in range(s):
        max_snow=max(max_snow,query(i))
    return max_snow

    



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
T = 100
I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
print(snow(T,I))