from zad4testy import runtests

def get_solution(included,T1,par,p):
    n=len(T1)
    R=[]
    i=n-1
    j=p
    while i!=None and i>=0:
        if included[i][j]:
            R.append(T1[i][4])
        i,j=par[i][j]
    return R


def select_buildings(T,p):
    n=len(T)


    F1=[[0 for _ in range(p+1)]for _ in range(n)]
    par=[[[None,None] for _ in range(p+1)]for _ in range(n)]
    included=[[False for _ in range(p+1)]for _ in range(n)]

    for i in range(n):
        h,a,b,w=T[i]
        T[i]=(h,a,b,w,i)

    T1=sorted(T,key=lambda x: x[1])
    T1.sort(key=lambda x: x[2])

    for i in range(n):
        h,a,b,w,ind=T1[i]
        c=h*(b-a)
        for j in range(p+1):
            if w<=j:
                F1[i][j]=c
                included[i][j]=True

                
    for i in range(1,n):
        h,a,b,w,ind=T1[i]  
        c=h*(b-a)
 
        for k in range(i-1,-1,-1):
            if T1[k][2]<a or k==i-1:
               for j in range(p+1):
                    if F1[i][j]<F1[i-1][j]:
                        F1[i][j]=max(F1[i-1][j],F1[i][j]) 
                        included[i][j]=False

                    if T1[k][2]<a and j-w>=0 and F1[i][j]<F1[k][j-w]+c:

                        F1[i][j]=max(F1[i][j],F1[k][j-w]+c)
                        included[i][j]=True
                        par[i][j]=[k,j-w]

            if T1[k][2]<a:
                break



        for j in range(p+1):
            if not included[i][j]:
                par[i][j]=[i-1,j]


    return get_solution(included,T1,par,p)
 
    



runtests( select_buildings )
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

# T=[(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# p=40 #27

# T=[(3, 3, 4, 19),
# (3, 11, 17, 7),
# (4, 8, 15, 15),
# (3, 1, 7, 15),
# (4, 12, 17, 7),
# (3, 1, 7, 3),
# (4, 8, 9, 7),
# (3, 11, 18, 15),
# (4, 20, 31, 19),
# (3, 17, 26, 7)]
# p=20
print(select_buildings(T,p))