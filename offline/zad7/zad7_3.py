from zad7testy import runtests
from collections import deque
from queue import PriorityQueue
from copy import deepcopy
def r_maze(F,i,j,sum,dir,vis):
    n=len(F)    
    if i==n-1 and j==n-1:
        return 0
    if i<0 or j<0 or i>=n or j>=n or vis [i][j]:
        return -1
  
    a=-1
    vis[i][j]=True

    if dir!=1:
        if F[i][j][0]>=0:
            up=F[i][j][0]
            
        else:
            up=r_maze(F,i+1,j,sum+1,0,vis)
            if up>=0:
                up+=1        
            if up!=-1:
                F[i][j][0]=up
        a=up

    
    if dir!=0:
        if F[i][j][1]>=0:
            down=F[i][j][1]
        else:
            down=r_maze(F,i-1,j,sum+1,1,vis)
            if down>=0:
                down+=1        
            if down>=0:
                F[i][j][1]=down
        a=max(a,down)


    if F[i][j][2]>=0:
        right=F[i][j][2]
    else:
        right=r_maze(F,i,j+1,sum+1,2,vis)
        if right>=0:
            right+=1
        if right>=0:
            F[i][j][2]=right
    a=max(a,right)    

    vis[i][j]=False
    return a

def maze(L):
    n=len(L)
    F=[[[-1,-1,-1] for _ in range(n)]for _ in range(n)]
    vis=[[False for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if L[i][j]=="#":
                vis[i][j]=True

    return r_maze(F,0,0,0,0,vis)






runtests( maze, all_tests = True )
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