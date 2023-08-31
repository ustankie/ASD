def przyczepa(W, K):
    n = len(W)

    W.sort(reverse=True)
    print(W)

    R=[]
    loaded=0
    things=0
    for i in range(n):
        if loaded+W[i]<=K:
            things+=1
            loaded+=W[i]
            R.append(W[i])
    return loaded,things,R


W = [2, 2, 4, 8, 1, 8, 16]
k = 27

print(przyczepa(W, k))