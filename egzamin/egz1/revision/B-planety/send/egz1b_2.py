#Urszula Stankiewicz, nr albumu: 415668
#Algorytm dynamiczny, wyznaczamy wartości tablicy F[i][j] - minimalna cena dotarcia od 0 do i mając jeszcze j paliwa w baku
#F[0][0]=0
#Dla danego pola i rozpatruję wszystkie możliwości dotarcia z i  mając j paliwa do pól k>i (posiadając na polu k jeszcze l paliwa).
# i jeśli koszt dotarcia tam jest mniejszy, to aktualizuje wartość F[k][l]
#Jeśli T[i][0]!=i oraz nie mamy paliwa w baku, to sprawdzamy, czy zmniejszy to koszt dotarcia do pola T[i][0]
#Złożoność: O(n^2*E^2)
from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)

    F=[[float('inf') for _ in range(E+1)]for _ in range(n)]
    
    F[0][0]=0

    def rec(i,j):
        if F[i][j]<float('inf'):
            return F[i][j]
        for k in range(i):
            dist=D[i]-D[k]
            if j-dist<0:
                F[i][j]=min(F[i][j],rec(k,0)+(dist-j)*C[k])
            for l in range(j-dist):
                F[i][j]=min(F[i][j],F[k][l])
        return F[i][j]
            

    # for i in range(1,n):
    #     if  T[i][0]>i:
    #         F[T[i][0]][0]=min(F[T[i][0]][0],F[i][0]+T[i][1])  
    #     for j in range(E+1):
    #         dist=D[i]-D[i-1]
    #         if j-dist>=0:
    #             F[i][j]=min(F[i][j],F[i-1][j-dist])
    #         else:
    #             to_tank=dist-j
    #             F[i][j]=min(F[i][j],F[i-1][0]+C[i-1]*to_tank)
                
            # for k in range(i+1,n):
                
            #     l=0
            #     to_tank=dist-j+l
            #     while l<=E:
            #         if to_tank>=0:

            #             F[k][l]=min(F[k][l],F[i][j]+to_tank*C[i])
            #         l+=1
            #         to_tank+=1


    rec(n-1,E)
                

    return min(F[n-1])


            

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = False )

