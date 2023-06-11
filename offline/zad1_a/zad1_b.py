#Urszula Stankiewicz, nr albumu: 415668
#Program wykorzystuje symetrię palindromu. Iterując i od 0 do n, sprawdzamy długość promienia maksymalnego palindromu o środku i, zapisując tę wartość w tablicy promieni r.
#Następnie w każdym kroku sprawdzamy długości już obliczonych promieni palindromów o środkach leżących na lewym promieniu naszego palindromu.
#jeśli palindrom o środku i-j (dla j od 0 do r[i]) ma promień 
#1)wykraczający poza granice naszego r[i] (r[i-j]>(r[i]-j)), to znaczy, że palindrom symetryczny względem i do palindromu
#o środku i-j ma promień r[i+j]=r[i]-j, gdyż gdyby był większy, to palindrom o środku i dałoby się powiększyć. Możemy więc nie sprawdzać już palindromu o środku i+j, 
#gdyż nie będzie on miał największego promienia. 
#2)niewykraczający poza granice r[i] (r[i-j]<(r[i]-j)), to na pewno nie jest on promieniem maksymalnym, gdyż jest mniejszy od r[i]. 
#Z symetrii podobna sytuacja ma miejsce dla palindromu o środku i+j, którego również nie musimy już sprawdzać. 
#3)r[i-j]=(r[i]-j) prawdopodobne jest, że palindrom o środku i+j da się powiększyć, dlatego musimy go sprawdzić.
#Za każdym razem, kiedy mierzymy długość promienia jakiegoś palindromu sprawdzamy czy nie jest on dłuższy od r_max.
#Algorytm ma złożoność O(n).


from zad1testy import runtests

def ceasar( s ):

    def pal_count(s,mid): #zwraca promien najdluzszego z palindromow o srodku mid
        R=2
        n=len(s)
        while (R+mid)<n and R<=mid and s[mid+R]==s[mid-R]:
            R+=1
        return R-1
    
    n=len(s)
    max_r=0
    r=[-1 for _ in range(n)] #tworzymy tablice promieni palindromow o danym srodku
    r[0]=0 
    r[n-1]=0
    #pierwszy i ostatni promien sa rowne 0 - zapisujac je w tablicy od razu oszczedzamy czas procesora, 
    #gdyz wywolanie funkcji pal_count (CALL) jest bardziej czasochlonne niz reczne wpisanie do tablicy
    #i=1
    for i in range(1,n):
        if r[i]==(-1): #sprawdzamy, czy dany palindrom byl juz symetria innego palindromu (wtedy nie musimy sprawdzac dlugosci jego promienia)

            if s[i-1]==s[i+1]: #sprawdzamy, czy w danym miejscu istnieje palindrom
                r[i]=pal_count(s,i) #mierzymy jego promien
                max_r=max(max_r,r[i]) #zapisujemy maksymalny promien w max_r
            else:
                r[i]=0

            j=1
            while j<=r[i]: #sprawdzamy dlugosci promieni palindromow o srodkach lezacych na promieniu palindromu o srodku i

                if r[i-j]>(r[i]-j):
                    r[i+j]=r[i]-j

                elif r[i-j]<(r[i]-j):
                    r[i+j]=r[i-j]

                j+=1

        #i+=1
    return max_r*2+1 #zwracamy dlugosc calego palindromu, czyli podwojona dlugosc promienia + srodek

        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True)
#print(ceasar("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))