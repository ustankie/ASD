#O(n^2)
from egz2btesty import runtests
from collections import deque
def magic( C ):
    n=len(C)
    d=[-1 for _ in range(n)]
    d[0]=0
    Q=deque()
    Q.append(0)
    while len(Q)>0:
        i=Q.popleft()
        for j in range(1,4):
            if C[i][j][1]>=0:
                a=C[i][0]-C[i][j][0]
                if a<=10 and d[i]+a>d[C[i][j][1]]:
                    d[C[i][j][1]]=d[i]+a
                    Q.append(C[i][j][1])
    
    return d[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
C=[[2, [5, 1], [1, 6], [1, 8]],
[2, [7, 2], [1, 4], [1, 2]],
[89, [91, 3], [75, 8], [84, 6]],
[8, [6, 4], [10, 6], [7, 5]],
[4, [5, 5], [1, 7], [3, 5]],
[10, [11, 6], [0, 6], [4, 6]],
[1, [0, 7], [0, 7], [6, 7]],
[57, [51, 8], [45, 8], [50, 8]],
[2, [6, 9], [7, 9], [0, 9]],
[6, [3, -1], [8, -1], [1, -1]]]
print(magic(C))

