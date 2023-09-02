from time import time
def ferry(A,l):
    n=len(A)
    l=int(l*100+0.5)
    r=int(r*100+0.5)
    for i in range(n):
        A[i]=int(A[i]*100+.5)
    S=[0 for i in range(n)]
    P=[0 for i in range(n)]
    S[0]=A[0]

    for i in range(1,n):
        S[i]=S[i-1]+A[i]

    def rec(i,R,L):
        if i==n or (R>=l and  L>=l ):
            return i+1
        a=i+1
        b=i+1
        #if R+A[i]<=l and S[i]-A[i]-R<=l:
        if R+A[i]<=l and L<=l:
            a=rec(i+1,R+A[i],L)
        #if S[i]-R<=l and R<=l:
        if L+A[i]<=l and R<=l:
            b=rec(i+1,R,L+A[i])
        if a>=b:
            P[i]='R'
        else:
            P[i]='L'
        return max(a,b)
    
    print(rec(0,0,0))

    #P[0]='R'
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
    return R,suma1,suma2


L = 18.24

cars = [15.16, 7.23, 4.98, 2.11, 3.08, 3.92, 6.34, 4.39, 2.63, 1234.88]
L = 18.24

cars = [3.16, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]
# L=10
# cars=[3,5,6,6]
start = time()
print(ferry(cars, L))
end = time()
print(end-start)