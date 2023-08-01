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

# def binsearch2(T,x):
#     i=0
#     j=len(T)-1
#     #print(*T,sep="\n")
#     while i<=j:
#         q=(i+j)//2
#         if T[q][4]==x:
#             #print(T[q],q)
#             #print(T)
#             return q
#         if T[q][4]<x:
#             i=q+1
#         else:
#             j=q-1
#     #print(i,x)
#     return i
# def binsearch1(T,x):
#     i=0
#     j=len(T)-1
#     while i<=j:
#         q=(i+j)//2
#         if T[q][4]==x:
#             #print(T[q],q)
#             #print(T)
#             return q
#         if T[q][4]>x:
#             i=q+1
#         else:
#             j=q-1
#     #print(i,x)
#     return i
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
    F1=[[0 for _ in range(p+1)]for _ in range(n)]
    F2=[[0 for _ in range(p+1)]for _ in range(n)]
    F=[[0 for _ in range(p+1)]for _ in range(n)]


    maxi=0
    for i in range(n):
        h,a,b,w=T[i]
        T[i]=(h,a,b,w,i)

    T1=sorted(T,key=lambda x: x[2])
    T2=sorted(T,key=lambda x: x[1])
    T1.sort(key=lambda x: x[1],reverse=True)
    T2.sort(key=lambda x: x[2])

    h,a,b,w,ind=T1[0]
    c=h*(b-a)
    for i in range(p+1):
        if w<=i:
            F1[0][i]=c

    
    h,a,b,w,ind=T2[0]
    c=h*(b-a)
    for i in range(p+1):
        if w<=i:
            F2[0][i]=c
    
    for i in range(1,n):
        h,a,b,w,ind=T1[i]
        c=h*(b-a)
        #print(c,h,a,b,w)
        k=1
        
        while k<=i and T1[i-k][1]<T1[i][2]:
            k+=1
        if k<=i:
            for j in range(p+1):
                F1[i][j]=F1[i-k][j]
                if j-w>=0:
                    F1[i][j]=max(F1[i][j],F1[i-k][j-w]+c)
        else:
            for j in range(p+1):
                if j-w>=0:
                    F1[i][j]=max(F1[i][j],c)
    
    for i in range(1,n):
        h,a,b,w,ind=T2[i]
        c=h*(b-a)
        k=1

        while k<=i and T2[i-k][2]>T2[i][1]:
                k+=1
        if k<=i:
            for j in range(p+1):
                F2[i][j]=F2[i-k][j]
                if j-w>=0:
                    F2[i][j]=max(F2[i][j],F2[i-k][j-w]+c)
        else:
            for j in range(p+1):
                if j-w>=0:
                    F2[i][j]=max(F2[i][j],c)
    print(*T1,sep="\n")
    print()
    print(*F1,sep="\n")
    print("\n\n")
    print(*T2,sep="\n")
    print()
    print(*F2,sep="\n")

    for i in range(n):
        h,a,b,w,ind=T[i]
        ind1=binsearch1(T1,a,ind)
        #print(ind1)
        ind2=binsearch2(T2,b,ind)
        print(ind,ind1,ind2)
        minus=0
        # for k in range(ind1):
        #     ind_int=binsearch2(T2,T1[k][4])
        #     if ind_int<ind2:
        #         minus+=T[ind_int][0]*(T[ind_int][2]-T[ind_int][1])
        
        # print(T2)
        for j in range(p+1):
            #F[i][j]-=minus
            if ind1>0 and ind2>0:
                for k in range(j):
                    F[i][j]=max(F[i][j],F1[ind1][k]+F2[ind2][j-k])
            elif ind1>0:
                F[i][j]=F1[ind1][j]
            elif ind2>0:
                F[i][j]=F2[ind2][j]
            F[i][j]=max(F[i][j],F[i-1][j])
        # curr_sum=h*(b-a)
        # curr_sol=[ind]
        # j=0
        # while j<n and T2[j][2]<a:
        #     h1,a1,b1,w1,ind1=T1[j]
        #     curr_sum+=h1*(b1-a1)
        #     curr_sol.append(ind1)
        #     j+=1
        # j=n-1
        # while j>=0 and T1[j][1]>b:
        #     h1,a1,b1,w1,ind1=T1[j]
        #     curr_sum+=h1*(b1-a1)
        #     curr_sol.append(ind1)
        #     j-=1
        
        # if curr_sum>maxi:
        #     maxi=curr_sum
        #     R=curr_sol
    print()
    print(*F,sep="\n")
    return F[n-1][p]
    #T.sort(key=lambda x:x[2])
    # F=[[0 for _ in range(p+1)]for _ in range(n)]

    # h,a,b,w=T[0]
    # c=h*(b-a)
    # for i in range(p+1):
    #     if w<=i:
    #         F[0][i]=c

    # for i in range(1,n):
    #     h,a,b,w=T[i]
    #     c=h*(b-a)  
    #     print(c)
    #     changed=False      
    #     for k in range(i):
    #         h1,a1,b1,w1=T[k]
    #         if b1<=a or b<=a1:
    #             changed=True
    #             for j in range(w):
    #                 F[i][j]=max(F[i][j],F[k][j])
    #             for j in range(w,p+1):
    #                 F[i][j]=max(F[i][j],F[k][j],F[k][j-w]+c)
    #     if not changed:
    #         for j in range(w,p+1):
    #             print("a")
    #             F[i][j]=c
    # print(*F,sep="\n")
    # return get_solution(F,T,p),F[n-1][p]

    



#runtests( select_buildings )
T = [(2, 1, 5, 3),
(3, 7, 9, 2), 
(2, 8, 11, 1) ]
p = 5 #14


T=[(7, 3, 4, 7),
(7, 1, 3, 19),
(2, 14, 15, 3),
(3, 3, 5, 3),
(3, 6, 7, 3),
(3, 5, 7, 19),
(3, 1, 17, 19),
(4, 7, 8, 7),
(3, 10, 14, 11),
(2, 9, 10, 11)]
p=20 #48

T=[(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
p=40 #27

print(select_buildings(T,p))