#zad_a
def min_max(A,inter):
    n=len(A)
    mini=inter[0]
    maxi=inter[1]

    for i in range(n):
        mini=min(mini,min(A[i]))
        maxi=max(maxi,max(A[i]))
    if mini<0:
        for i in range(n):
            A[i][0]-=mini
            A[i][1]-=mini
        maxi-=mini
        inter[0]-=mini
        inter[1]-=mini
    return inter

def filter_int(A, inter):
    n = len(A)
    R = []
    for i in range(n):
        if not (A[i][0] < inter[0] or A[i][1] > inter[1]):
            R.append(A[i])
    return R

def binsearch(A,x):
    n=len(A)
    i=0
    j=n-1

    while i<=j:
        q=(i+j)//2
        if A[q]==x:
            return q
        if A[q]<x:
            i=q+1
        else:
            j=q-1
    return i

def intervals(A, inter):
    A=filter_int(A,inter)
    A.sort()
    n=len(A)
    inter=min_max(A,inter)
    print(A,inter)

    a,b=inter
    c=b-a+1
    print(c)
    F=[[None for _ in range(c)]for _ in range(c)]

    def merge(i,j):
        if F[i-a][j-a]!=None:
            return F[i-a][j-a]
        q=binsearch(A,[i,j])
        if q<n and A[q]==[i,j]:
            F[i-a][j-a]=True
            return True
        for k in range(i,j):
            if merge(i,k) and merge(k,j):
                F[i-a][j-a]=True
                return True
        F[i-a][j-a]=False
        return False
    merge(a,b)
    #print(*F,sep="\n")
    return F[0][b-a]

#zad_b
def intervals_cost(A, inter):
    A=filter_int(A,inter)
    A.sort()
    A_bin=[]
    n=len(A)

    inter=min_max(A,inter)
    for i in range(n):
        A_bin.append([A[i][0],A[i][1]])
    # print(A,inter)
    # print(A_bin)

    a,b=inter
    #print(a,b)
    c=b-a+1
    #print(c)
    F=[[None for _ in range(c)]for _ in range(c)]

    def merge(i,j):
        nonlocal a
        if F[i-a][j-a]!=None:
            return F[i-a][j-a]
        
        q=binsearch(A_bin,[i,j])
        if q<n and A_bin[q]==[i,j]:
            F[i-a][j-a]=A[q][2]
            return F[i-a][j-a]
        F[i-a][j-a]=float('inf')
        for k in range(i+1,j):
            o=merge(i,k)
            p=merge(k,j)
            # if [i,j]==[a,b]:
            #     print(i,k,j,o,p)

            F[i-a][j-a]=min(F[i-a][j-a],o+p)
        return F[i-a][j-a]
    merge(a,b)
    #print(*F,sep="\n")
    return F[0][b-a]

#zad_c

def min_max2(A):
    n=len(A)
    mini=float('inf')
    maxi=-float('inf')

    for i in range(n):
        mini=min(mini,min(A[i]))
        maxi=max(maxi,max(A[i]))
    if mini<0:
        for i in range(n):
            A[i][0]-=mini
            A[i][1]-=mini
        maxi-=mini
        mini=0
    

    return mini,maxi,maxi-mini+1
def k_intervals(A):
    A.sort()
    n=len(A)

    a,b,c=min_max2(A)
    print(a,b,c)

    # print(A,inter)
    # print(A_bin)


    #print(c)
    F=[[None for _ in range(c)]for _ in range(c)]

    def merge(i,j):
        if F[i][j]!=None:
            return F[i][j]
        
        q=binsearch(A,[i,j])
        if q<n and A[q]==[i,j]:
            F[i][j]=A[q][1]-A[q][0]
            return F[i][j]
        F[i][j]=-float('inf')
        for k in range(i+1,j):
            o=merge(i,k)
            p=merge(k,j)
            # if [i,j]==[a,b]:
            #     print(i,k,j,o,p)

            F[i][j]=max(F[i][j],o+p)
        return F[i][j]
    merge(a,b)
    #print(*F,sep="\n")
    return F[0][b-a]


A = [[4, 5], [2, 4], [1, 3], [3, 6], [5, 7], [1, 5], [-5, 2]]
A = [[4.1, 5.2], [2.15, 4.4], [1.5, 3.2], [3.2, 6.83], [5.2, 7.1], [1.2, 5.2], [-5.75, 2.15]]
for i in range(len(A)):
    if A[i][0]>0:
        A[i][0] = int(A[i][0]*100+0.5)
    else:
        A[i][0] = int(A[i][0]*100-0.5)
    if A[i][1]>0:
        A[i][1] = int(A[i][1]*100+0.5)
    else:
        A[i][1] = int(A[i][1]*100-0.5)
print(A)
print(intervals(A,[120,710]))
A = [[7.1, 9.2, 1.3], 
     [9.2, 11, 0], 
     [5.2, 11, 7.3], 
     [-5.2, 5.2, 6.2], 
     [5.2, 7.1, 9], 
     [1.5, 5.2, 3], 
     [9.2, 11, 20]
]
for i in range(len(A)):
    if A[i][0]>0:
        A[i][0] = int(A[i][0]*10+0.5)
    else:
        A[i][0] = int(A[i][0]*10-0.5)
    if A[i][1]>0:
        A[i][1] = int(A[i][1]*10+0.5)
    else:
        A[i][1] = int(A[i][1]*10-0.5)
    if A[i][2]>0:
        A[i][2] = int(A[i][2]*10+0.5)
    else:
        A[i][2] = int(A[i][2]*10-0.5)

print(A)
print(intervals_cost(A, [15, 110]))
print(intervals_cost(A, [-52, 110]))



A = [[4.1, 5.2], [2.15, 4.4], [1.5, 3.2], [3.2, 6.83], [5.2, 7.1], [1.2, 5.2], [-5.75, 2.15]]
for i in range(len(A)):
    if A[i][0]>0:
        A[i][0] = int(A[i][0]*100+0.5)
    else:
        A[i][0] = int(A[i][0]*100-0.5)
    if A[i][1]>0:
        A[i][1] = int(A[i][1]*100+0.5)
    else:
        A[i][1] = int(A[i][1]*100-0.5)       
print(A)                                                                           
print(k_intervals(A))

