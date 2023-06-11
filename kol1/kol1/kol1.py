#Urszula Stankiewicz, nr albumu 415668
#Algorytm wykorzystuje kolejkę priorytetową PriorityQueue, wrzucając do niej wszystkie wartości z danego
#przedziału od i do i+p-1 (czynność tę powtarzamy dla każdego przedziału). 
#Następnie wyciągamy z kolejki p-k-1 wartości (tyle będzie elementów mniejszych od k-tego największego)
#i p-k-ty element będzie zarazem k-tym największym, więc dodajemy go do sumy. Algorytm działa poprawnie, ponieważ 
#dla każdego z przedziałów od i do i+p-1(dla każdej iteracji zewnętrznej pętli for) znajdujemy k-ty największy element w tym przedziale
#dodając go do sumy.
#Algorytm ma złożoność czasową O(n*p), zaś pamięciową O(n^2)
from kol1testy import runtests
from queue import PriorityQueue

def ksum(T, k, p):
    n=len(T)
    sum=0
    for i in range(0,n-p+1):
        a=PriorityQueue(n)
        for j in range(i,i+p):
            a.put(T[j]) 

        for j in range(p-k):
            s=a.get()
        sum+=a.get()

    return sum







# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
