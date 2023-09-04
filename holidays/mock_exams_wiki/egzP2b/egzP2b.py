from egzP2btesty import runtests
from math import log10

def kryptograf( D, Q ):
    n=len(D)
    # for i in range(n):
    #     D[i]=D[i][::-1]
    
    m=len(Q)
    # for i in range(m):
    #     Q[i]=Q[i][::-1]
    
    count=1
    for i in range(m):
        a=len(Q[i])
        curr=0
        for j in range(n):
            b=len(D[j])-a
            is_=True
            if len(D[j])>=a:
                for k in range(a):
                    # print(k+b)
                    if D[j][k+b]!=Q[i][k]:
                        is_=False
                        break
                if is_:
                    curr+=1
        # print(curr)
        if curr:
            count*=curr
    # print(count)
    return log10(count)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 1)

D=  ['0', '100', '1100', '1101', '1111']
Q=  ['', '1', '11', '0', '1101']
print(kryptograf(D,Q))