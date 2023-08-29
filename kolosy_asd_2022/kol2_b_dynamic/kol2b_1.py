from kol2btesty import runtests
from queue import PriorityQueue

def min_cost( O, C, T, L ):
    n=len(O)
    for i in range(n):
        O[i]=(O[i],C[i])

    O.append((0,0))
    O.sort(key=lambda x:x[0])
    O.append((L,0))

    # print(O)

    n+=2

    F=[[float('inf'),float('inf')] for _ in range(n)]
    
    F[0][0]=0
    F[n-1][1]=0
    Q_a=PriorityQueue()
    Q_b=PriorityQueue()


    for i in range(n):   
        if O[i][0]>T:
            break
        Q_a.put((O[i][1],O[i][0]))    
        F[i][0]=O[i][1]

    for i in range(n-1,-1,-1):
        if L-O[i][0]>T:
            break
        Q_b.put((O[i][1],O[i][0]))
        F[i][1]=O[i][1]  


    for i in range(n):
        while not Q_a.empty() and O[i][0]-Q_a.queue[0][1]>T:
            Q_a.get()
        if Q_a.empty():
            return None
        else:
            F[i][0]=Q_a.queue[0][0]+O[i][1]
            Q_a.put((F[i][0],O[i][0]))

    for i in range(n-1,-1,-1):
        while not Q_b.empty() and Q_b.queue[0][1]-O[i][0]>T:
            Q_b.get()
        if Q_b.empty():
            return None
        else:
            F[i][1]=Q_b.queue[0][0]+O[i][1]
            Q_b.put((F[i][1],O[i][0]))
    min_val=F[0][1]
    Q=PriorityQueue()
    Q.put((F[0][0],0))

    for i in range(1,n):
        while not Q.empty() and O[i][0]-Q.queue[0][1]>2*T:
            Q.get()
        if Q.empty():
            return None
        else:
            min_val=min(min_val,F[i][1]+Q.queue[0][0])
            Q.put((F[i][0],O[i][0]))
        
    # print(*F,sep="\n")

    return min_val
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25
print(min_cost( O, C, T, L ))
