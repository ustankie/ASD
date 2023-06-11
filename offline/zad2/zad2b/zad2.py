from zad2testy import runtests
sum=0
def merge(T1,T2,step):
    n1=len(T1)
    n2=len(T2)
    r=[0 for _ in range(n1+n2)]
    i=0
    for j in range(n1):
        if T1[j]>step:
            r[i]=T1[j]-step
            i+=1
    for j in range(n2):
        if T2[j]>step:
            r[i]=T2[j]-step
            i+=1
    return r

def snow2(S,step=0):
    global sum
    n=len(S)
    # print(S)
    # print(step,sum)

    if n==1:
        sum+=S[0]
        return S

    mid=n//2
    L=S[:mid]
    R=S[mid:]
    return merge(snow2(L,step),  snow2(R,step+1),step)
    
def snow( S ):
    global sum
    a=snow2(S)
    print(a)
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
S = [1, 7, 3, 4, 1]
#print(snow(S))