'''
Urszula Stankiewicz, nr albumu: 415668
Algorytm sortuje punkty, a następnie sprawdza dla każdego punktu, od ilu punktów jest silniejszy, zapisując to w tablicy F.
Na koniec zwracamy max(F)
Złożoność: O(n^2)
'''
from egz2atesty import runtests


def dominance(P):
  n=len(P)
  P.sort()
  # print(P)
  F=[0 for _ in range(n)]

  for i in range(n):
    for j in range(i):
      x1,y1=P[i]
      x2,y2=P[j]
      if x1>x2 and y1>y2:
        F[i]+=1
    # print(F)
  return max(F)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

P=[(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]
P=[(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))
