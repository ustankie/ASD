#Jan Masternak 415200

#Algorytm zaklada, ze rozwiazanie istnieje.
#Rozwazamy funkcje f(i,j) - w implementacji nazwana the_best_scenario
#f(i,j) - najlepsze mozliwe dopasowanie parkingow do biurowcow, pod warunkiem, ze dla biurowcow o numerach i,i+1,...,n-1
#mamy do dyspozycji jedynie parkingi o numerach j,j+1,...-m-1
#Edge casy:
#a) musimy przypasowac jeszcze jakies biurowce do parkingow, ale juz nie mamy parkingow do dyspozycji -> inf (i != n and j == m)
#b) juz nie musimy przypasowac zadnych parkingow -> 0 (i == n)
#W przeciwnym razie:
#f(i,j) = min (p,r), gdzie:
#p = f(i+1,j+1) + abs(X[i]-Y[j]) - i-temu biurowcowi przydzielamy j-ty parking; a co za tym idzie dalszym biurowcom mozemy przydzielic tylko parkingi j+1,j+2,...,m-1
#r = f(i,j+1) - i-temu biurwocowi nie przydzielamy j-tego parkingu, tylko taki, ktory lezy dalej (dalej od poczatku osi liczbowej, niekoniecznie dalej od i-tego biurowca)
#Zloznosc obliczeniowa: O(n*m) (koszt obliczenia f(i,j) ma czas staly, a kazde f(i,j) obliczamy tylko raz)
#Zloznosc pamieciowa: O(n*m)


from egz2btesty import runtests


def parking(X,Y):
    n = len(X)
    m = len(Y)
    the_best_scenario = [[None for _ in range (0,m)] for _ in range (0,n)]

    def determine_the_best_scenario (i,j):
        if i != n and j == m: return float ("inf")
        elif i == n: return 0
        elif the_best_scenario[i][j] != None: return the_best_scenario[i][j]
        else:
            the_best_scenario[i][j] = min (determine_the_best_scenario (i,j+1), determine_the_best_scenario (i+1,j+1) + abs(X[i]-Y[j]))
            return the_best_scenario[i][j]

    return determine_the_best_scenario (0,0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
