from kolutesty import runtests
from queue import PriorityQueue

def swaps( disk, depends ):
    n=len(depends)

    def DFS(u):
        nonlocal changes
        
        Q=PriorityQueue()
        Q.put((0,u))
        while not Q.empty():
            p,u=Q.get()
            for v in depends[u]:
                if not vis[v]:
                    vis[v]=True
                    #DFS(v)
                    if disk[v]==disk[u]:
                        Q.put((0,v))
                    else:
                        Q.put((1,v))

            A.append(u)



    vis=[False for _ in range(n)]
    changes=0
    A=[]
    F=[float('inf')for _ in range(n)]
    F[0]=0

    for v in range(n):
        if not vis[v]:
            vis[v]=True
            DFS(v)
    # for i in range(n-2):
    #     if not A[i+2] in depends[A[i+1]] and disk[A[i]]!=disk[A[i+1]] and disk[A[i]]==disk[A[i+2]]:
    #         A[i+1],A[i+2]=A[i+2],A[i+1]
    # for i in range(1,n):
    #     if disk[A[i-1]]!=disk[A[i]]:
    #         F[i]=min(F[i-1]+1,F[i])
    #     else:
    #         F[i]=min(F[i],F[i-1])
    for i in range(1,n):
        if disk[A[i-1]]!=disk[A[i]]:
            changes+=1
    print(A)
    return changes




# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( swaps, all_tests = False )
disks=['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A']
depends=[[1], [], [1, 4, 7], [1, 7], [1], [1, 2, 4], [2, 4, 5], [1], [1, 2], [3, 4]]
print(swaps(disks,depends))

