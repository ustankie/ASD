from zad9ktesty import runtests
from math import inf

def prom(A,l,r):
    n=len(A)
    #print(l,r)
    # l=int(l*100+0.5)
    # r=int(r*100+0.5)
    # for i in range(n):
    #     A[i]=int(A[i]*100+.5)
    S=[0 for i in range(n+2)]
    F=[[None for _ in range(r+1)]for _ in range(n+1)]
    P=[0 for i in range(n)]
    S[0]=A[0]

    for i in range(1,n):
        S[i]=S[i-1]+A[i]

    end_idx=0
    def rec(i,R):
        L=l-((S[end_idx]-S[i])-(r-R))
        if L<0 or R<0:
            return False
        if i==0:
            if L-A[0]>=0:
                P[0]='L'
                return True 
            if R-A[0]>=0:
                P[0]='R'
                return True
            return False
        #print(i,R,r,n)
        if F[i][R] is None:           
            F[i][R]=rec(i-1,R-A[i])
            if F[i][R]:
                P[i]='R'
            else: 
                F[i][R]= rec(i-1,R)
                if F[i][R]:
                    P[i]='L'
                else:
                    F[i][R]=None

        return F[i][R]
    
    for i in range(n-1,-1,-1):
        end_idx=i
        P=[0 for i in range(n)]
        if rec(i,r): 
            #print(P)
            letter='L'
            if P[i]=='R':
                letter='R'   
            R=[]
            for i in range(n):
                if P[i]==letter:
                    R.append(i)

            return R

    return []
runtests ( prom )
T = [6, 6, 10, 11, 0, 2, 9, 8, 11, 1]
l1 = 10
l2 = 15

T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10
print(prom(T,l1,l2))