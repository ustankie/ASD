#1) zad5 z png - mamy ciąg a0,..,a_(n-1) - mamy podzielić na k przedziałów tak, by najmniejsza suma przedziału była największa
#   F(i,j,l)-minimalna suma podprzedziału w optymalnym podziale przedziału i,j na l przedziałów
#   F(i,j,1)=suma od A[i] do A[j]
#   F(i,j,l)=max(min(f(m,j,l-1),suma od A[i] do A[m] po m od i+1 do j) #F(i,j,l)=max(min(f(i,m,1),suma od A[i] do A[m] po m od i+1 do j)
#   F(i,j,l)=-inf dla i>j
#   rekurencja ze spamiętywaniem, słowniki
#2) n domków, włamywacz włamuje się, każdy dom ma wartość c[i], nie może się włamać do dwóch domków pod rząd / drzewa
#   F[i][True] - maksymalny zysk z domów od 1 do i, pod warunkiem, że okradamy i-ty dom
#   F[i][False] - maksymalny zysk z domów od 1 do i, pod warunkiem, że nie okradamy i-tego domu
#   F[0,_]=0
#   F[i,True]=F[i-1,False] + C[i]
#   F[i,False]=max(F[i-1,True],F[i-1,False])
#3) głodna żaba - Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
#   wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
#   jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
#   niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
#   dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
#   skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
#   każdej z liczb. - F[i,k]-minimalna liczba skoków, by dotrzeć z pola i do końca, jeśli żaba ,a na polu i k energii (przed zjedzeniem przekąski z pola i)
#   F[n,k]=0 k>=0
#   F[j,k]=inf, k<0, 1<=j<=n
#   F[i,k]=min(F[j,k-(j-i)+A[i]]) +1 dla i<j<=k+A[i]
#   O(n^2) -> jeśli algorytm zachłanny jest poprawny, to O(nlogn)
#4) Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można
#   skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
#   1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków. - koniec przedziałów wierzchołkiem, krawędzią przedział,DFS
#   2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b] - dijkstra
#   3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków:
#       początki i końce są naturalne
#   F[l,x] - długość najdłuższego przedziału złożonego z l odcinków zaczynającego się w x
#   F[0,_]=0
#   F[l,x]=0 jeśli x nie jest początkiem żadnego przedziału
#   F[l,x]=max(F(l-1,b)+(b-x)) dla przedziałów (x,b) w zbiorze wszystkich przedziałów
#   rozwiązanie: max(F[k,_])

#1)
f=dict()
def recur(A,i,j,k):
    if (i,j,k) in f.keys():
        return f[(i,j,k)]
    sum=0
    maxi=-float('inf')
    for m in range(i,j):
        sum+=A[i]
        maxi=max(maxi,f(tab,m,j,k-1))