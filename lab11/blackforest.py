def blackf(C):
    n=len(C)
    F=[[0,0]for _ in range(n)]
    for i in range(n):
        F[i][1]=C[i]
    for i in range(1,n):
        F[i][0]=max(F[i-1][0],F[i-1][1])
        F[i][1]=F[i-1][0]+C[i]
    return max(F[n-1]),solution(F,C)
def solution(F,C):
    A=[]
    if F[n-1][0]<F[n-1][1]:
        A.append(n-1)
    def recur(i):
        if F[i][0]
    



T = [1, 8, 3, 4, 5, 1, 2]
T = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
T = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
print(blackf(T))