from zad1testy import runtests

def counting_sort(A,k):
    n=len(A)
    C=[0 for _ in range(k)]
    B=[0 for _ in range(n)]
    for i in range(n):
        #print(A[i][0],ord(A[i][0]))
        C[ord(A[i][0])-ord('a')]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    #print(C)
    for i in range(n-1,-1,-1):
        B[C[ord(A[i][0])-ord('a')]-1]=A[i]
        #print(B)
        C[ord(A[i][0])-ord('a')]-=1
    for i in range(n):
        A[i]=B[i]

def tanagram(x,y,t):
    n=len(x)
    m=len(y)
    if n!=m:
        return False
    a=[[x[i],i]for i in range(n)]
    b=[[y[i],i]for i in range(n)]

    counting_sort(a,26)
    counting_sort(b,26)
    for i in range(n):
        if a[i][0]!=b[i][0]:
            return False
        if abs(a[i][1]-b[i][1])>t:
            return False
    return True
runtests(tanagram)
x="egzamin"
y="gzemina"
t=3
print(tanagram(x,y,t))


    