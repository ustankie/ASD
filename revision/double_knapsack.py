def knapsack(P,W,H):
    n=len(P)

    F=[[[0 for _ in range(H+1)]for _ in range(W+1)]for _ in range(n)]

    for w in range(P[0][1],W+1):
        for h in range(P[0][1],H+1):
            F[0][w][h]=P[0][0]
    
    for i in range(1,n):
        for w in range(W+1):
            for h in range(H+1):
                F[i][w][h]=F[i-1][w][h]
                if w-P[i][1]>=0 and h-P[i][2]>=0:
                    F[i][w][h]=max(F[i][w][h],F[i][w-P[i][1]][h-P[i][2]]+P[i][0])
    return F[n-1][W][H]


P = [4, 10, 2, 3, 8]
W = [10, 4, 1, 2, 6]
H = [3, 9, 12, 4, 2]
A=[]
for i in range(len(P)):
    A.append((P[i],W[i],H[i]))
MaxW = 12
MaxH = 20
print(A)

print(knapsack(A ,MaxW, MaxH))