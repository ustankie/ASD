from zad3testy import runtests
def common(A,B):
    a=(max(A[0],B[0]),min(A[1],B[1]))
    if a[0]<=a[1]:
        return a
    return (0,0)
def length(A):
    return A[1]-A[0]

def find_max(A,n):
    max_len=0
    max_interval=(0,0)
    max_ind=0

    for i in range(n):
        if A[i][1]-A[i][0]>max_len:
            max_len=A[i][1]-A[i][0]
            max_interval=A[i]
            max_ind=i
    return max_interval,max_ind
def kintersect(A, k):
    n=len(A)
    F=[[[[(0,0),[]]]for _ in range(k+1)]for _ in range(n)]


    
    # for i in range(n):
    #     #max_interval,max_ind=find_max(A,i)
    #     F[i][0][0]=(-float('inf'),float('inf'))

    for i in range(n):
        F[i][1][0][0]=A[i]
        F[i][1][0][1]=[i]
    #print(*F,sep="\n")
    
    for i in range(1,n):
        for j in range(2,k+1):
            for p in range(i):
                for s in range(len(F[p][j])):
                    #print(F[p][j])
                    c=common(F[p][j-1][s][0],A[i])
                    if length(c)==length(F[i][j][0][0]):
                        F[i][j][0].append([c,F[p][j-1][s][1]+[i]])
                    elif length(c)>length(F[i][j][0][0]):
                        F[i][j][0][0]=c
                        F[i][j][0][1]=F[p][j-1][s][1]+[i]
                    if length(F[p][j][s][0])==length(F[i][j][0][0]):
                        F[i][j][0].append([F[p][j][s]])
                    elif length(F[p][j][s][0])>length(F[i][j][0][0]):
                        F[i][j][0][0]=F[p][j][s][0]
                        F[i][j][0][1]=F[p][j][s][1]
    #print(*F,sep="\n")
    return F[n-1][k][0][1]
            


    



runtests(kintersect)
A=[(0, 4), (1, 10), (6, 7), (2, 8)]
k=3
print(kintersect(A,k))