#Urszula Stankiewicz, nr albumu: 415668
#Program wykorzystuje symetrię palindromu. Iterując i od 0 do n, sprawdzamy długość promienia maksymalnego palindromu o środku i, zapisując tę wartość w tablicy promieni r.
#Następnie w każdym kroku sprawdzamy długości już obliczonych promieni palindromów o środkach leżących na lewym promieniu naszego palindromu.
#jeśli palindrom o środku i-j (dla j od 0 do r[i]) ma promień 
#1)wykraczający poza granice naszego r[i] (r[i-j]>(r[i]-j)), to znaczy, że palindrom symetryczny względem i do palindromu
#o środku i-j ma promień r[i+j]=r[i]-j, gdyż gdyby był większy, to palindrom o środku i dałoby się powiększyć. Możemy więc nie sprawdzać już palindromu o środku i+j, 
#gdyż nie będzie on miał największego promienia. 
#2)niewykraczający poza granice r[i] (r[i-j]<(r[i]-j)), to na pewno nie jest on promieniem maksymalnym, gdyż jest mniejszy od r[i]. 
#Z symetrii podobna sytuacja ma miejsce dla palindromu o środku i+j, którego również nie musimy już sprawdzać. 
#3)r[i-j]=(r[i]-j) prawdopodobne jest, że palindrom o środku i+j da się powiększyć, dlatego musimy go sprawdzić. W
#Za każdym razem, kiedy mierzymy długość promienia jakiegoś palindromu sprawdzamy czy nie jest on dłuższy od r_max.
#Algorytm ma złożoność O(n).


from zad1testy import runtests

def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    def pal_count(s,mid): #zwraca promien najdluzszego z palindromow o srodku mid
        R=1
        n=len(s)
        while (R+mid)<n and R<=mid and s[mid+R]==s[mid-R]:
            R+=1
        return R-1
    
    n=len(s)
    max_r=0
    r=[-1 for _ in range(n)]
    r[0]=0
    r[n-1]=0
    #print(r[0])
    i=1
    while i<n:
        if r[i]==(-1):
            #print("i: ",i,"\n")
            r[i]=pal_count(s,i)
            max_r=max(max_r,r[i])
            j=1
            while j<=r[i]:
                #print(i-j)
                if r[i-j]>(r[i]-j):
                    r[i+j]=r[i]-j
                    #max_r=max(max_r,r[i-j])
                elif r[i-j]<(r[i]-j):
                    r[i+j]=r[i-j]
                j+=1
            #print("\n")
        i+=1
    return max_r*2+1

        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True)
#print(ceasar("akontnoknonabcddcba"))