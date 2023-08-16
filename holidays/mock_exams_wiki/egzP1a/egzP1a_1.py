from egzP1atesty import runtests


def binsearch(A, x):
    i = 0
    j = len(A)-1

    while i <= j:
        q = (i+j)//2
        if A[q] == x:
            return q
        if A[q] < x:
            i = q+1
        else:
            j = q-1
    return i


def alpha_search(M, x):
    for i in range(len(M)):
        if M[i] == x:
            return i
    return len(M)


def titanic(W, M, D):
    #D.sort()
    n = len(W)

    # for i in range(len(D)):
    #     print(M[D[i]])
    m = len(M)

    maxlen=0
    for i in range(m):
        maxlen=max(maxlen,len(M[i][1]))

    D1=[]
    for i in range(len(D)):
        D1.append(M[D[i]][1])
    #print(D1)
    D1.sort()
    W1 = ""

    for i in range(n):
        W1 += (M[ord(W[i])-ord('A')][1])
    #print(W1)
    n = len(W1)
    F = [float('inf') for _ in range(n)]
    F[0] = 1

    for i in range(1, n):
        for j in range(i-maxlen,i+1):
            sub = W1[j:i+1]

            b =binsearch(D1, sub)

            if b < len(D1) and D1[b] == sub:
                #print(D1[b],sub)
                F[i] = min(F[i], F[j-1]+1)
                if j == 0:
                    F[i] = 1

    return F[n-1]


runtests(titanic, recursion=False)

M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'),
     ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..')]
W = 'BGTILCLEXI'
D = [0, 2, 4, 13, 17, 19]

print(titanic(W, M, D))
