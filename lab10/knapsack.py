def knapsack(W,P,B):
    n=len(W)
    F=[[0 for _ in range(B+1)]for _ in range(n)]

    for i in range(W[0],B+1):
        F[0][i]=P[0]
    
    for i in range(1,n):
        for j in range(B+1):
            F[i][j]=F[i-1][j]
            if j-W[i]>=0:
                F[i][j]=max(F[i][j],F[i-1][j-W[i]]+P[i])
    
    return F[n-1][B]
def filtr(W,P,B):
    W1=[]
    P1=[]
    n=len(W)
    for i in range(n):
        if W[i]<=B and P[i]>0:
            W1.append(W[i])
            P1.append(P[i])
    return W1,P1
def print_par(par,j,i,p,F,W):
    A=[]
    s=i*p+j
    while s!=None:
        i=s//p
        j=s%p
        if F[i][j]!=F[i-1][j] or par[i][j]==None or par[i][j]==(i-1)*(p+1)+j-P[i]:
            A.append(i)

        print(i,j,F[i][j])
        s=par[i][j]

    return A[::-1]
def get_knap(F,W,P,i,p):
    if i<0:
        return []
    if i==0:
        if p==P[0]:
            return [0]
        return []
    if F[i][p]!=F[i-1][p]:
        if p>=P[i] and F[i][p]==F[i-1][p-P[i]]+W[i]:
            return get_knap(F,W,P,i-1,p-P[i])+[i]
        return [i]
    return get_knap(F,W,P,i-1,p)

def knapsack2(W,P,B):
    W,P=filtr(W,P,B)
    if len(W)==0:
        return 0
    n=len(W)
    p=sum(P)
    F=[[B+1 for _ in range(p+1)]for _ in range(n)]
    par=[[None for _ in range(p+1)]for _ in range(n)]

    for i in range(P[0]+1):
        F[0][i]=W[0]
    
    for i in range(1,n):
        for j in range(p+1):
            F[i][j]=F[i-1][j]
            par[i][j]=(i-1)*(p+1)+j
            if P[i]>=j: 
                if F[i-1][j]>W[i]:
                    F[i][j]=W[i]
                    par[i][j]=None
            else:
                if F[i][j]>F[i-1][j-P[i]]+W[i]:
                    F[i][j]=F[i-1][j-P[i]]+W[i]
                    par[i][j]=(i-1)*(p+1)+j-P[i]
    print(*par,sep="\n")
    for i in range(p,-1,-1):
        if F[n-1][i]<=B:      
            return i,get_knap(F,W,P,n-1,i),print_par(par,i,n-1,p,F,W)
    return 0



W = [5, 3, 4, 2]
P = [60, 50, 70, 30]
MaxW = 5


print(knapsack2(W, P, MaxW))