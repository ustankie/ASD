def get_solution(F,V,W,H):
    n=len(F)
    w=len(F[0])-1
    h=len(F[0][0])-1

    i=n-1
    j=w
    k=h

    R=[]
    while i>=0 and j>=0 and w>=0:
        if F[i][j][k]==F[i-1][j-W[i]][k-H[i]]+P[i]:
            #print(F[i][j][k],i,j,k)
            R.append(i)
            #i-=1
            j-=W[i]
            k-=H[i]
            #print(F[i][j][k],i,j,k)
        #else:
        i-=1
        
    return R[::-1]

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
    return F[n-1][w][h],get_solution(F,V,W,H)


def knapsack2(V,W,H,w,h):
    n=len(V)

    F=[[0 for _ in range(h+1)]for _ in range(w+1)]

    for j in range(W[0],w+1):
        for k in range(H[0],h+1):
            F[j][k]=P[0]

    for i in range(1,n):
        for j in range(w,-1,-1):
            for k in range(h,-1,-1):
                if j-W[i]>=0 and k-H[i]>=0:
                    F[j][k]=max(F[j][k],F[j-W[i]][k-H[i]]+V[i])
    return F[w][h]#,get_solution(F,V,W,H)

P = [4, 10, 2, 3, 8]
W = [10, 4, 1, 2, 6]
H = [3, 9, 12, 4, 2]

MaxW = 12
MaxH = 20



P = [4, 10, 2, 3, 8]
W = [10, 6, 1, 2, 6]
H = [3, 9, 12, 4, 9]

MaxW = 12
MaxH = 20

print(knapsack2(P, H, W, MaxH, MaxW))
