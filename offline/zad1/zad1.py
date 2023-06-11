#Urszula Stankiewicz, nr albumu: 415668
#Program wyszukuje dwa środkowe elementy ciągu znaków s - prawy i lewy (mid_r,mid_l) 
#i traktuje każdy z nich jako środek potencjalnego palindromu. Dopóki środek prawy jest odległy od końca s 
#o  więcej niż znalezioną największą połowę długości najdłuższego palindromu (half_max, początkowo równe 0) 
#lub środek lewy odległy o więcej niż ta wartość od początku s, znaczy to, że wciąż jesteśmy w stanie znaleźć dłuższy palindrom niż ten, którego długość zapamiętaliśmy w half_max.
#Sprawdzamy więc długości maksymalnych palindromów (a raczej ich połowy) o tych środkach (funkcja pal_count),
#zaczynając od mid_l, ponieważ dla n=len(s) nieparzystych będzie miał on większą wartość niż mid_r (potencjał na znalezienie od razu dłuższego palindromu).
#Następnie porównujemy te długości z half_max i w razie potrzeby zapamiętujemy nową, większą wartość half_max - sprawdzamy przy tym, czy jest to palindrom maksymalny dla tego środka
#(taki, że jego powiększenie spowodowałoby wykroczenie poza zakres danych). Jeśli tak, zwracamy odpowiednią długość maksymalną (half_max*2+1 -> half_max jest połową długości nieparzystej).
#Następnie przesuwamy odpowiednio mid_l i mid_r w lewo lub w prawo o jedną pozycję i powtarzamy operację do momentu, kiedy dalsze przesunięcie będzie oznaczało, że palindrom maksymalny
#będzie mniejszej długości niż 2*half_max+1. Na koniec zwracamy 2*half_max+1
#Algorytm ma złożoność O(nlogn), ponieważ z każdą iteracją zmniejszamy ilość porównań dzięki sprawdzaniu, czy dalsze przesuwanie mid_l i mid_r ma szansę nam dostarczyć lepszego rozwiązania


from zad1testy import runtests

def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    def pal_count(s,mid): #zwraca połowę długości najdłuższego z palindromów o środku mid
        i=1
        n=len(s)
        while (i+mid)<n and i<=mid and s[mid+i]==s[mid-i]:
            i+=1
        return i-1
    
    n=len(s) #mierzymy długość danych wejściowych
    half_max=0 #half_max przechowuje odległość środka najdłuższego palindromu od jego początku/końca, na początku najdłuższy palindrom ma długość 1, zatem half_max=0
    mid_r=n//2 #prawy element środkowy s (dla n parzystych) lub środek s (dla n nieparzystych)
    mid_l=n//2-1 # lewy element środkowy s (dla n parzystych) lub pierwszy element na lewo od środka s (dla n nieparzystych)

    while mid_l>half_max or (n-mid_r)>half_max: #sprawdza, czy dalsze palindromy o środkach mid_r, mid_l mają szansę być dłuższe od już znalezionego najdłuższego
 
        b=pal_count(s,mid_r)

        if b>half_max:
            half_max=b
            if half_max==(n-mid_r): #sprawdzamy, czy kolejne przesunięcie mid_r w prawo nie spowoduje sprawdzania niepotrzebnie palindromu, który nie ma szansy być dluższy od już znalezionego
                return (2*half_max+1) #warunek ten pozwala ominąć porównania analogiczne dla mid_l (które zawsze będzie mogło dać palindrom co najwyżej taki jak maksymalny mid_r, ale nie dluższy)
        
        a=pal_count(s,mid_l)

        if a>half_max:
            half_max=a
        
        mid_l-=1
        mid_r+=1

    return 2*half_max+1
        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True)