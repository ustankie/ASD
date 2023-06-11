    F=[[-1 for _ in range(n)]for _ in range(n)]
from zad7testy import runtests
from collections import deque
from queue import PriorityQueue
def par_in_path(par,old_i,old_j,new_i,new_j,F):
    if (new_i,new_j)==(0,0):
        return True
    n=len(par)
    i,j=old_i,old_j
    p,q=i,j
    if (i,j)!=(0,0) or (i,j)!=(new_i,new_j):
        return (i,j)==(new_i,new_j)
    i,j=par[i][j]
    while (i,j)!=(0,0) and (i,j)!=(new_i,new_j):
        p,q=i,j
        i,j=par[i][j]
    print(old_i,old_j,new_i,new_j,(i,j)==(new_i,new_j))
    if (i,j)!=(new_i,new_j):
        return False
    D=[(0,-1),(-1,0),(1,0)]
    cnt=0
    for a in range(3):
        if D[a][0]+p>=0 and D[a][0]+p<n and D[a][1]+q>=0 and D[a][1]+q<n and F[D[a][0]+q][D[a][0]+q]==F[p][q]:
            if cnt==1:
                par[p][q]=(D[a][0]+p,D[a][1]+q)
                return False
                
            cnt+=1
    
    return True

def relax(F,par,Q,i,j,k,l,L):
    if L[k][l]=="#":
        return
    if F[k][l]<0:
        F[k][l]=F[i][j]+1
        par[k][l]=(i,j)
        Q.put((F[k][l],(k,l)))
    elif F[k][l]<F[i][j]+1 and not par_in_path(par,i,j,k,l,F):
        F[k][l]=F[i][j]+1
        par[k][l]=(i,j)
        Q.put((F[k][l],(k,l)))

def maze(L):
    n=len(L)
    par=[[None for _ in range(n)]for _ in range(n)]
    F[0][0]=0
    Q=PriorityQueue()
    Q.put((0,(0,0)))
    #print(Q.queue)
    while not Q.empty():
        #print(Q.queue)
        d,v=Q.get()
        i,j=v
        if i<(n-1):
            relax(F,par,Q,i,j,i+1,j,L)

        if i>0:
            relax(F,par,Q,i,j,i-1,j,L)

        if j<(n-1):
            relax(F,par,Q,i,j,i,j+1,L)
        print(*F,sep="\n")
        print()
    return F[n-1][n-1]



            # if F[i-1][j]<0:
            #     F[i-1][j]=F[i][j]+1
            #     par[i-1][j]=(i,j)
            #     Q.put(F[i-1][j],(i-1,j))
            # elif not par_in_path(par,i,j,i-1,j) and F[i-1][j]<F[i][j]+1:
            #     F[i-1][j]=F[i][j]+1
            #     par[i-1][j]=(i,j)
            #     Q.put(F[i-1][j],(i-1,j))
            
            # if F[i+1][j]<0:
            #     F[i+1][j]=F[i][j]+1
            #     par[i+1][j]=(i,j)
            #     Q.put(F[i+1][j],(i+1,j))
            # elif not par_in_path(par,i,j,i+1,j) and F[i+1][j]<F[i][j]+1:
            #     F[i+1][j]=F[i][j]+1
            #     par[i+1][j]=(i,j)
            #     Q.put(F[i+1][j],(i+1,j))


#runtests( maze, all_tests = False )
L = [ "....",
"..#.",
"..#.",
"...." ]

print(maze(L))