#1) Dana jest tablica n liczb ze zbioru {0...n^2-1}
#Chcemy ją posortować -> radixsort 1)%n 2)//n -> O(n)                                                                                       1) v
#2)Sortowanie tablicy n liczb, w której występuje O(logn)różnych wartości -> tablica jak w counting sorcie -> para: wartość, ilość          2) v
#3)Dana jest tablica n liczb. Szukamy takich dwóch liczb, które po posortowaniu 
#byłyby koło siebie, i których różnica jest maksymalna -> bucket sort: znajdujemy min i max, na podstawie tego buckety, wrzucamy
#elementy do kubełków o równej szerokości ((max-min)//n) - jeśli któryś kubełek zawiera dwie liczby, to któryś jest pusty
#Wtedy odległość między kubełkami to co najmniej rozmiar kubełka. (min z prawej - max z lewej).                                             3) v chyba
# Jeśli w każdym kubełku jest wartość, to posortowaliśmy liczby, wystarczy porównać kolejne wartości.
#4) Dane są dwa napisy. Proszę zaimplementować funkcję, sprawdzającą czy są anagramami (słowa zbudowane z tych samych liter) 
#-np. "kot","kto" ->O(n) -> counting sort każde słowo                                                                                       4) v
#5)Mamy tablicę kolorów T rozmiaru n, T[i] należy do {0,..,k-1}
#Chcemy znaleźć najmniejszy spójny podprzedział, który zawiera wszystkie kolory -> rozszerzamy się od początku tablicy,
#potem zmniejszamy z lewej - bo dla każdego początku znajdujemy najmniejszy przedział                                                       5) v
#6) eksperyment fizyczny - generujemy liczby z zakresu 0...10^9-1 w czasie stałym mamy odp, ile różnych wart się pojawiło,
#znamy rozmiar najdłuższego ciągu, jest on rzędu n -> stos L: duża tablica liczników, każde pole zawiera licznik i wskaźnik na stos 
# jesli wskaźnik wskazuje poza stos, to licznik=1, wstawiamy liczbe na stos (kiedy element wskazuje na stos, ale stos twiedzi inaczej,
#  to znaczy ze elementu na stosie nie ma), by zresetowac liczniki, wystarczy powiedziec ze stos ma wartosc 0
#7)problem otoczki wypukłej - mamy zbiór punktów na płaszcyźnie - znaleźć najmniejszy wielokąt wypukły zawierający wszystkie pkt
#na podstawie tego, że nie można sortować szybciej niz logn, nie mozna napisac otoczki szybciej niz logn
#->mamy ciąg danych x0...xn -> mozemy je podzielic na pary (x0,x0^2),(x1,x1^2).... -> na wykresie parabola, 
# musimy posortowac je w kolejnosci
#8) szybkie przesuwanie indeksow o k pozycji - odwrócenie,odwrócenie,zamiana, odwrócenie                                                    8) v???




#4)
def anagram(w1,w2):
    n1=len(w1)
    n2=len(w2)
    if n1!=n2:
        return False
    R=[None for i in range(26)]  
    #wpisywanie zer trwa najdluzej kiedy duzy alfabet a krotkie slowa - > zerujemy tylko te elementy, ktore uzyte
    for c in w1:
        R[ord(c)-ord('a')]=0
    for c in w2:
        R[ord(c)-ord('a')]=0
    for i in range(n1):
        R[ord(w1[i])-ord('a')]+=1
    for i in range(n2):
        R[ord(w2[i])-ord('a')]-=1
        if R[ord(w2[i])-ord('a')]<0:
            return False
    return True
print(anagram("ktoo","ktto"))