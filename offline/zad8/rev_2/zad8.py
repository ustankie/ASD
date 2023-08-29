
from zad8testy import runtests
from collections import deque
def sum_stains(T):
    n=len(T)
    m=len(T[0])

    S=[0 for _ in range(m)]
    steps=[(-1,0),(0,-1),(1,0),(0,1)]
    suma=0

    def DFS(u1,u2):
        nonlocal suma
        T[u1][u2]=0
        for a,b in steps:
            v1=u1+a
            v2=u2+b
            if 0<=v1<n and 0<=v2<m and T[v1][v2]:
                suma+=T[v1][v2]               
                DFS(v1,v2)
    cnt=0
    for u2 in range(m):
        if  T[0][u2]:
            suma=0
            cnt+=1
            suma+=T[0][u2]
            DFS(0,u2)
            S[u2]=suma
    return S,cnt
                
    

def plan(T):
    # print(T)
    S,cnt_stains=sum_stains(T)
    m=len(T[0])
    max_stain=max(S)
    # print(S)

    F=[float('inf') for _ in range(m)]
    B=[0 for _ in range(m)]
    
    B[0]=S[0]
    F[0]=1
    S[0]=0

    for i in range(1,m):
        F[i]=F[i-1]
        if B[i-1]>1:
            B[i]=B[i-1]-1           
        elif i!=m-1:
            max_stain=0
            max_ind=1
            for j in range(1,i+1):
                if S[j]>max_stain:
                    max_stain=S[j]
                    max_ind=j
            B[i]=max_stain
            S[max_ind]=0
            F[i]=F[i-1]+1
    return F[m-1]
                





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
T=[[1, 0], 
   [0, 0]]
T=[[3, 0, 0, 1, 0], 
   [0, 1, 0, 0, 1], 
   [0, 1, 0, 0, 0], 
   [0, 1, 0, 0, 0], 
   [0, 1, 0, 0, 0]]
print(plan(T))

