from kol2btesty import runtests

def min_cost( O, C, T, L ):
    n=len(O)
    for i in range(n):
        O[i]=(O[i],C[i])

    O.append((0,0))
    O.sort(key=lambda x:x[0])
    O.append((L,0))

    #print(O)

    n+=2

    F=[[float('inf'),float('inf')] for _ in range(n)]
    
    F[0][0]=0

    i=0
    while i<n:
        min_ind=i+1
        min_c=float('inf')
        
        k=i+1
        
        while k<n and O[k][0]-O[i][0]<=T:
            F[k][0]=min(F[k][0],F[i][0]+O[k][1])
            F[k][1]=min(F[k][1],F[i][1]+O[k][1])
            #print(i,k)
            if min_c>F[k][0] or min_c>F[k][1]:
                min_c=min(F[k])
                min_ind=k
            k+=1
            
        while k<n and T<O[k][0]-O[i][0]<=2*T:
            F[k][1]=min(F[k][1],F[i][0]+O[k][1])
            k+=1
        
        i=min_ind
    
    #print(*F,sep="\n")

    return min(F[n-1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25
print(min_cost( O, C, T, L ))
