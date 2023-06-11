# 1)v A - tablica liczb naturalnych o długości n
#    czy da się wybrać podciąg B taki że suma elementów wynosi T 
#   a)v tablica sum, bool czy jesteśmy w stanie uzyskać daną sumę
#      -> iterujemy A z przodu, sumy od tyłu
#   b)v f(i,v)=True, f(i+1,v) or f(i+1,v-A[i]);False wpp
#       f(i,0)=True
#       f(i,v)=False, v<0
# 2)v dwie tablice liczb naturalnych A,B, równej długości - znaleźć najdłuższy wspólny (nie musi być spójny) podciąg O(n^2) 
#   ->f(i,j) - najdłuższy  podciąg i-elementów z A i j elementów z B
#   f(i,j)=max(f(i-j,j),f(i,j-1),f(i-1,j-1)+1 jeśli A[i]==B[i])
#   f(-1,j)=0
#   f(i,-1)=0
#
#   if A[i]==B[j]: f(i,j)=f(i-1,j-1)+1
#   else: f(i,j)=max(f(i-1,j),f(i,j-1))
#   wypisywanie chodzeniem po tablicy O(n) -> wiki
# 3) tablica liczb naturalnych A - najdłuższy niekoniecznie spójny rosnący podciąg O(nlogn)
#   -> wewnętrznego fora zamieniamy na binsearch, w F nie trzymamy długości, tylko wartość ostatniego elementu tworzącego ciąg rosnący
# 4) A1A2...An - ciąg macierzy, chcemy je wymnożyć tak by koszt (liczba operacji) był jak najmniejszy, znamy ich rozmiary -> w jakiej kolejności
#   a) szukamy największych wymiarów po posortowaniu, mnożymy, znowu szukamy najw itd -> źle
#   b) f(i,j)-koszt przemnożenia macierzy od Ai do Aj -> wyliczamy wartości "odchodząc" od przekątnej
# 5) szachownica A (n x n), zawiera liczby wymierne -> przejść z 0,0 na n,n -> nie można dijsktrą, można iśc tylko w prawo albo w dół o 1
#   -> dla każdego pola sprawdzamy czy lepiej przyjść z lewej czy z góry
# 6) tablica (szuflada z pieniędzmi kasjerki) - nieskończony zasób nominałów, 
#   ograniczone wartości, znaleźć minimalną ilość monet do wydania kwoty (zachłanny działa tylko dla optymalnych nominałów)


#1) b)
def f(A,m):
    n=len(A)
    DP=[[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(n+1):
        DP[i][0]=1
    for i in range(1,n+1):
        for j in range(m,-1+A[i-1],-1)
            DP[i][j]=DP[i][j] /#or DP[i-1][j]
            or DP[i-1][j-A[i]]
    return DP[n][m]