from egz3atesty import runtests
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
    
    S=map_snow(I)
    n=len(I)
    s=len(S)
    # print(S)

    prefix_diff=[0 for _ in range(s+1)]
    
    for i in range(n):
        a=binsearch(S,I[i][0])
        b=binsearch(S,I[i][1])
        
        prefix_diff[a]+=1
        prefix_diff[b+1]-=1
    
    sums=[0 for _ in range(s+1)]
    sums[0]=prefix_diff[0]
    max_snow=sums[0]
    for i in range(1,s+1):
        sums[i]=sums[i-1]+prefix_diff[i]
        max_snow=max(max_snow,sums[i])
    return max_snow
    



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
T = 100
I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
print(snow(T,I))