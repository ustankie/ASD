from zad9ktesty import runtests
from math import inf
def get_solution(F,l1,l2,A,a):
    n=len(F)
    m=len(F[0])
    i=0
    r=l2
    l=l1
    left=[]
    right=[]
    while i<=a and (r-A[i]>=0 or l-A[i]>=0):
        if F[i][r][0]>F[i][r][1]:
            right.append(i)
            r-=A[i]
        else:
            left.append(i)
            l-=A[i]
        i+=1
    if left[-1]==a:
        return left
    return right

def prom(A,l,r):
    n=len(A)

    S=[0 for i in range(n+2)]
    F=[[[None,None] for _ in range(r+1)]for _ in range(n+1)]
    S[0]=A[0]

    for i in range(1,n):
        S[i]=S[i-1]+A[i]

    def rec(i,R):
        if i==0:
            L=l
        else:
            L=l-((S[i-1])-(r-R))
        if L<0 or R<0:
            return i-1
        if i==n:
            return i

        if F[i][R][0] is None:           
            F[i][R][0]=rec(i+1,R-A[i])

        if F[i][R][1] is None: 
            F[i][R][1]= rec(i+1,R)

        return max(F[i][R])
    

    a=rec(0,r)-1

    R=get_solution(F,l,r,A,a)
    return R

runtests ( prom )
T = [6, 6, 10, 11, 0, 2, 9, 8, 11, 1]
l1 = 10
l2 = 15

T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10

l1=50 
l2=80 
T=[11, 2, 29, 24, 9, 10, 1, 2, 13, 12, 9, 6, 23, 6, 13, 12, 9, 18, 25, 24, 27, 12, 27, 4, 5, 22, 17, 12, 1, 12, 3, 22, 19, 8, 21, 28, 13, 8, 13, 8, 5, 6, 27, 24, 11, 20, 7, 6, 21, 20]
print(prom(T,l1,l2))