from zad4testy import runtests

def get_solution(F,T,p):
    n=len(T)
    i=n-1
    j=p
    R=[]


    while i>0 and j>0:
        i-=1
        while j>0 and F[i][j]!=F[i-1][j]+T[i][0]*(T[i][2]-T[i][1]):
            j-=1
        R.append(i)
        #j-=1
    return R

def binsearch1(A,l,x):
    n=len(A)
    i=0
    j=n-1
    while i<=j:
        q=(j+i)//2
        #print(A[q][4])
        if A[q][1]>l or (A[q][1]==l and A[q][4]<x):
            i=q+1
        else:
            j=q-1

    return i
def binsearch2(A,r,x):
    n=len(A)
    i=0
    j=n-1
    while i<=j:
        q=(j+i)//2
        if A[q][2]<r or (A[q][2]==r and A[q][4]<x):
            i=q+1
        else:
            j=q-1

    return i

def select_buildings(T,p):
    n=len(T)
    # if p==20:
    #     print(*T,sep="\n")
    R=[]
    F1=[[[0,0] for _ in range(p+1)]for _ in range(n)]
    F=[[0 for _ in range(p+1)]for _ in range(n)]


    for i in range(n):
        h,a,b,w=T[i]
        T[i]=(h,a,b,w,i)

    T1=sorted(T,key=lambda x: x[1])
    T1.sort(key=lambda x: x[2])

    # h,a,b,w,ind=T1[0]
    # c=h*(b-a)
    # for i in range(p+1):
    #     if w<=i:
    #         F1[0][i]=c

    

    for i in range(n):
        h,a,b,w,ind=T1[i]
        c=h*(b-a)
        for j in range(p+1):
            if w<=j:
                F1[i][j][1]=c
    
    for i in range(1,n):
        h,a,b,w,ind=T1[i]
        c=h*(b-a)
        #print(c,h,a,b,w)
        #k=1
        
        for k in range(i):
            #if :

            for j in range(p+1):
                
                if T1[k][2]<=a:
                    F1[i][j][0]=max(max(F1[k][j]),F1[i][j][0])
                    if j-w>=0:
                        F1[i][j][1]=max(F1[i][j][1],max(F1[k][j-w])+c)
                else:
                    F1[i][j][0]=max(F1[i][j][0],max(F1[k][j]))
        # else:
            #     for j in range(p+1):
            #         if j-w>=0:
            #             F1[i][j]=max(F1[i][j],c)
    
    print(*T1,sep="\n")
    print(*F1,sep="\n")


    return max(F1[n-1][p])
 
    



#runtests( select_buildings )
T = [(2, 1, 5, 3),
(3, 7, 9, 2), 
(2, 8, 11, 1) ]
p = 5 #14


# T=[(7, 3, 4, 7),
# (7, 1, 3, 19),
# (2, 14, 15, 3),
# (3, 3, 5, 3),
# (3, 6, 7, 3),
# (3, 5, 7, 19),
# (3, 1, 17, 19),
# (4, 7, 8, 7),
# (3, 10, 14, 11),
# (2, 9, 10, 11)]
# p=20 #48

# T=[(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# p=40 #27

T=[(3, 3, 4, 19),
(3, 11, 17, 7),
(4, 8, 15, 15),
(3, 1, 7, 15),
(4, 12, 17, 7),
(3, 1, 7, 3),
(4, 8, 9, 7),
(3, 11, 18, 15),
(4, 20, 31, 19),
(3, 17, 26, 7)]
p=20
print(select_buildings(T,p))