from zad7testy import runtests
from collections import deque
from queue import PriorityQueue
from copy import deepcopy
def r_maze(F,i,j,sum,dir,vis):
    n=len(F)    
    if i==n-1 and j==n-1:
        #print(sum)
        #print(i,j,n,"a: ",0)
        return 0
    #print(*vis,sep="\n")
    if i<0 or j<0 or i>=n or j>=n or vis [i][j]:
        #print(i,j,"a: ",-1)
        return -1
    # a=-1
    # if dir==0:
    #     a=max(F[i][j][2],F[i][j][0])

    # elif dir==1:
    #     a=max(F[i][j][1],F[i][j][2])
    # elif dir==2:
    #     a=max(F[i][j][1],F[i][j][0],F[i][j][2])
    # if a>=0:
    #     print(a)
    #     return a
 

  
    a=-1
    vis[i][j]=True
    # up=0
    # down=0
    # right=0
    #if dir!=1:
    if dir!=1:
        if F[i][j][0]>=0:
            up=F[i][j][0]
        else:
            up=r_maze(F,i+1,j,sum+1,0,vis)
        a=max(a,up)
        if F[i][j][0]!=up and up!=-1:
            F[i][j][0]=up+1
    
        # a=max(a,up)
    if dir!=0:
        if F[i][j][1]>=0:
            down=F[i][j][1]
        else:
            down=r_maze(F,i-1,j,sum+1,1,vis)
        a=max(a,down)
        if F[i][j][1]!=down and down!=-1:
            F[i][j][1]=down+1
        #a=max(a,down)
    #if j+1<n and not vis[i][j+1]:
    if F[i][j][2]>=0:
        right=F[i][j][2]
    else:
        right=r_maze(F,i,j+1,sum+1,2,vis)
    #a=max(a,right)
    
    a=max(a,right)
    if F[i][j][2]!=right and right!=-1:
        F[i][j][2]=right+1
    

    vis[i][j]=False
    if a>=0:
        return a+1
    return a
def rec1(L,F,i,j):
    while i>0 and L[i][j]==".":
        i-=1
        F[i][j]=F[i+1][j]+1
    if j<(n-1):
        j+=1
        F[i][j]=F[i][j-1]
    return i,j
def rec2(L,F,i,j):
    while i<(n-1) and L[i][j]==".":
        i+=1
        F[i][j]=F[i-1][j]+1
    if j<(n-1):
        j+=1
        F[i][j]=F[i][j-1]
    else:
        return False
    return i,j

def maze(L):
    n=len(L)
    F=[[[-1,-1,-1] for _ in range(n)]for _ in range(n)]
    vis=[[False for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if L[i][j]=="#":
                vis[i][j]=True

    return r_maze(F,0,0,0,0,vis)






#runtests( maze, all_tests = False )
L = [
     '....#...##',
     '...#....##', 
     '#.........', 
     '.......#..', 
     '.......##.', 
     '...#....#.', 
     '#....#....', 
     '##.....#.#', 
     '..........', 
     '......#...'
     ]
# L = [ '....','..#.','..#.','....']
# L = ['......', 
#      '#..#..', 
#      '.#..#.', 
#      '##..#.', 
#      '......', 
#      '......']


print(maze(L))