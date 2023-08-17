def get_solution(F,V,W,H):
    n=len(F)
    w=len(F[0])-1
    h=len(F[0][0])-1

    i=n-1
    j=w
    k=h

    R=[]

    

def knapsack(V,W,H,w,h):
    n=len(V)

    F=[[[0 for _ in range(h+1)]for _ in range(w+1)]for _ in range(n)]

    for j in range(W[0],w+1):
        for k in range(H[0],h+1):
            F[0][j][k]=P[0]

    for i in range(1,n):
        for j in range(w+1):
            for k in range(h+1):
                F[i][j][k]=F[i-1][j][k]
                if j-W[i]>=0 and k-H[i]>=0:
                    F[i][j][k]=max(F[i][j][k],F[i-1][j-W[i]][k-H[i]]+V[i])
    return F[n-1][w][h]


P = [4, 10, 2, 3, 8]
W = [10, 4, 1, 2, 6]
H = [3, 9, 12, 4, 2]

MaxW = 12
MaxH = 20

print(knapsack(P, H, W, MaxH, MaxW))
