def forest(A):
    n=len(A)
    F=[[0,0]for _ in range(n)]
    F[0][1]=A[0]

    for i in range(1,n):
        F[i][0]=max(F[i-1])
        F[i][1]=F[i-1][0]+A[i]
    return max(F[n-1]),solution(A,F)

def solution(A,F):
    n=len(A)
    R=[]
    
    def recur(i):
        if i<0:
            return
        if F[i][0]>F[i][1]:
            recur(i-1)
        else:
            R.append(i)
            recur(i-2)
    recur(n-1)
    return R



T = [1, 8, 3, 4, 5, 1, 2]
T = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
T = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
T = [8, 12, 3, 4, 7, 1, 2, 10]
T = [8, 1, 3, 4, 5, 1, 2]
print(forest(T))