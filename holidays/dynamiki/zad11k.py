from zad11ktesty import runtests

def kontenerowiec(T):
    n=len(T)
    #print(T)
    s=0
    for i in range(n):
        s+=T[i]

    F=[[None for _ in range(s)]for _ in range(n)]

    def rec(i,R):
        if i+1<n:
            if F[i][R]==None:
                F[i][R]=min(rec(i+1,R+T[i]),rec(i+1,R))
        else:
            F[i][R]= abs(R-(s-R))
        return F[i][R]

    return rec(0,0)

runtests ( kontenerowiec )
T = [1, 4]
#T = [1, 6, 5, 11]
#T=[20, 39, 57, 77, 93]
print(kontenerowiec(T))