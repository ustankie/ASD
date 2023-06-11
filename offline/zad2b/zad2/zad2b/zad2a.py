from zad2testy import runtests
sum=0
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    T=[0 for _ in range(n1+n2)]
    while i<n1 and j<n2:
        if T1[i]<T2[j]:
            T[i+j]=T1[i]
            i+=1
        else:
            T[i+j]=T2[j]
            j+=1
    
    while i<n1:
            T[i+j]=T1[i]
            i+=1
    
    while j<n2:
            T[i+j]=T2[j]
            j+=1
    return T


def MergeSort(T):
    n=len(T)
    if (n==1):
        return T
    mid=n//2
    L=T[:mid]
    R=T[mid:n]

    return merge(MergeSort(L),MergeSort(R))
def minimalize(T):
    n=len(T)
    r=[0 for _ in range(n)]
    i=0
    for j in range(n):
        if T[j]>1:
            r[i]=T[j]-1
            i+=1

    return r[0:i]

def snow2(S,k,r=0):
    # global sum
    # for i in range(r):
    #     print("     |",end="")
    # print(S)
    # for i in range(r):
    #     print("     |",end="")

    n=len(S)

    if n==0:
        #print("\n")
        return 0
    if n==1:
        #print("\n")
        return S[0]

    a=S[k]
    if k==0:
        S=S[1:]
    else:
        S=S[:n-1]
    S=minimalize(S)
    #print(S,a)
    n=len(S)
    Ln=S[1:]
    Rn=S[:n-1]
    
    b=max(snow2(S,0,r+1),snow2(S,n-1,r+1),snow2(Ln,0,r+1),snow2(Rn,n-2,r+1))+a
    # for i in range(r):
    #     print("     |",end="")
    # print(S," b: ",b,r)
    return b
    
def snow( S ):
    global sum
    n=len(S)
    print(n)
    Ln=S[1:]
    Rn=S[:n-1]
    a=max(snow2(S,0),snow2(S,n-1),snow2(Ln,0),snow2(Rn,n-2,))

    return a

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
#S = [ 3,1,1,5,1,1,3]
#print(snow(S))