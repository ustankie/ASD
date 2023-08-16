def blackforest(C):
    n = len(C)
    F = [[0, 0] for _ in range(n)]

    F[0][0] = 0
    F[0][1] = C[0]

    for i in range(1, n):
        F[i][0] = max(F[i-1])
        F[i][1] = F[i-1][0]+C[i]

    return max(F[n-1]),get_solution(F)


def get_solution(F):
    n = len(F)
    R=[]

    def rec(i):
        if i<0:
            return
        if F[i][1]>F[i][0]:
            R.append(i)
            rec(i-2)
        else:
            rec(i-1)
    
    rec(n-1)
    return R

T = [1, 8, 3, 4, 5, 1, 2]
T = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
T = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
T = [8, 12, 3, 4, 7, 1, 2, 10]
T = [8, 1, 3, 4, 5, 1, 2]
print(blackforest(T))
