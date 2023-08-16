from time import time
def ferry(A,l,r):
    n=len(A)
    l=int(l*100+0.5)
    r=int(r*100+0.5)
    for i in range(n):
        A[i]=int(A[i]*100+.5)
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
        if rec(i,r):    
            print(P)
            R=[]
            suma1=0
            suma2=0
            for i in range(n):
                if P[i]=='L':
                    R.append(i)
                    suma1+=A[i]
                elif P[i]=='R':
                    suma2+=A[i]
            return R

    return []

L = 18.24

cars = [15.16, 7.23, 4.98, 2.11, 3.08, 3.92, 6.34, 4.39, 2.63, 1234.88]
# L = 18.24

# cars = [3.16, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]
# L=10
# cars=[3,5,6,6]
start = time()
print(ferry(cars, L,L))
end = time()
print(end-start)