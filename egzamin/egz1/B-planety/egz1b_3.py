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
    
    #for i in range(E+1):
    F[0][0]=0
    # def rec(i,j):
    #     if F[i][j]<float('inf'):
    #         return F[i][j]

    for i in range(n):
        for j in range(E+1):  
            if j==0 and T[i][0]>i:
                F[T[i][0]][0]=min(F[T[i][0]][0],F[i][j]+T[i][1])  
                #print(F[i][j],i,j,T[i][1],F[T[i][0]][0])
            for k in range(i+1,n):
                dist=D[k]-D[i]
                l=0
                to_tank=dist-j+l
                while l<=E:
                    #print(l)
                    if to_tank>=0:
                        # if i==1:
                        #     print(to_tank,C[i],F[i][j])
                        #print(i)
                        F[k][l]=min(F[k][l],F[i][j]+to_tank*C[i])
                    l+=1
                    to_tank+=1

        # print(*F,sep="\n")
        # print()
            # k=i+1
            # if k<n:
            #     dist=D[i+1]-D[i]
            # while k<n and dist<=j:
            #     F[k][j-dist]=min(F[k][j-dist],F[i][j])
            #     k+=1
            #     if k<n:
            #         dist=D[k]-D[i]
            # k=i+1
            # if k<n:
            #     dist=D[i+1]-D[i]
            # for k in range(i+1,n):
            #     for l in range(E+1-(j-dist)):
            #         F[k][j-dist+l]=min(F[k][j-dist+l],F[i][j]+l*C[i])
            #         dist=D[k]-D[i]

                

    print(*F,sep="\n")
    return min(F[n-1])


            

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = False )
D= [0, 2, 5, 6, 7, 8, 9, 11, 14, 16, 19, 20, 23, 25, 26, 27, 28, 30, 31, 34, 37, 38, 39, 42, 43, 45, 47, 50, 52, 55, 57, 60, 62, 64, 65, 68, 71, 72, 74, 75, 78, 81, 83, 86, 87, 88, 90, 92, 94, 95, 96, 98, 100, 103, 104, 106, 107, 110, 113, 116, 118, 120, 122, 123, 126, 129, 131, 134, 137, 140, 143, 144, 
    145, 146, 147, 150, 153, 154, 157, 158, 159, 162, 164, 167, 169, 171, 174, 176, 179, 180, 182, 184, 187, 188, 191, 192, 195, 196, 198, 200, 202]
C=  [2, 1, 3, 8]
T = [(8, 2), (1, 0), (2, 0), (3, 0), (4, 0), 
     (5, 0), (10, 4), (19, 34), (8, 0), (21, 56), 
     (18, 51), (11, 0), (24, 46), (13, 0), (14, 0), (27, 10), 
     (24, 2), (25, 14), (18, 0), (27, 2), (20, 0), (21, 0), 
     (22, 0), (23, 0), (24, 0), (25, 0), (34, 17), (35, 0),
       (28, 0), (33, 10), (38, 32), (35, 5), (44, 48), (41, 45), 
       (38, 3), (43, 19), (40, 4), (41, 14), (46, 30), (39, 0), 
       (40, 0), (49, 2), (54, 28), (47, 0), (44, 0), (45, 0), (54, 2), 
       (47, 0), (60, 2), (61, 50), (50, 0), (51, 0), (64, 8), (53, 0),
         (66, 12), (67, 28), (64, 2), (61, 6), (70, 14), (63, 4), 
         (60, 0), (61, 0), (70, 3), (63, 0), (64, 0), (65, 0), (70, 21), (67, 0), (68, 0), (69, 0), 
         (74, 6), (83, 28), (80, 34), (77, 10), (86, 4), (79, 6), (76, 0), (85, 10), (82, 14), 
         (83, 2), (80, 0), (93, 6), (90, 26), (95, 30), (88, 1), (85, 0), (98, 2), (99, 4), 
         (92, 5), (89, 0), (98, 5), (91, 0), (96, 2), (97, 10), (100, 3), (100, 10), (96, 0), (100, 12), (98, 0), (99, 0), (100, 52)]

E= 5
#print(planets(D,C,T,E))
