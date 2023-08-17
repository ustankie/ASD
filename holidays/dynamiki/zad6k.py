from zad6ktesty import runtests 

def haslo ( S ):
    n=len(S)
    if n==0:
        return 1
    for i in range(1,n):
        if S[i]==S[i-1]==0:
            return 0
    F=[0 for _ in range(n)]

    F[0]=1
    if S[1]==0:
        if S[0]<3:
            F[1]=1
        else:
            return 0
    elif int(S[:2])<27:
        F[1]=2
    else:
        F[1]=1

    for i in range(2,n):
        if int(S[i])!=0:
            F[i]+=F[i-1]
        if 9<int(S[i-1:i+1])<27:
            F[i]+=F[i-2]
    #print(F)
    return F[n-1]
runtests ( haslo )
S='18758'
print(haslo(S))