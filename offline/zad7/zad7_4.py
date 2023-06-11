from zad7testy import runtests

def r_maze(F,i,j,sum,dir,vis,L):
    n=len(F)    
    if i==n-1 and j==n-1:
        return 0
        
    if i<0 or j<0 or i>=n or j>=n or vis [i][j] or L[i][j]=="#":
        return -1
  
    a=-1
    
    call_right=True

    if dir!=1:
        if F[i][j][0]>=0:
            up=F[i][j][0]        
        else:
            vis[i][j]=True
            up=r_maze(F,i+1,j,sum+1,0,vis,L)       
            right=r_maze(F,i,j+1,sum+1,2,vis,L)
            call_right=False
            if right>=0:
                right+=1
            if up>=0:
                up+=1        
            if up!=-1:
                F[i][j][0]=up
            F[i][j][0]=max(F[i][j][0],right)
        a=F[i][j][0]

    
    if dir!=0:
        if F[i][j][1]>=0:
            down=F[i][j][1]
        else:
            vis[i][j]=True
            down=r_maze(F,i-1,j,sum+1,1,vis,L)            
            if down>=0:
                down+=1        
            if down>=0:
                F[i][j][1]=down
            if call_right:
                right=r_maze(F,i,j+1,sum+1,2,vis,L)

                if right>=0:
                    right+=1            
                F[i][j][1]=max(F[i][j][1],right)


        a=max(a,F[i][j][1])

    vis[i][j]=False
    return a

def maze(L):
    n=len(L)
    F=[[[-1,-1] for _ in range(n)]for _ in range(n)]
    vis=[[False for _ in range(n)]for _ in range(n)]

    return r_maze(F,0,0,0,0,vis,L)






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