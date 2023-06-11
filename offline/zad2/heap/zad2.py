#Urszula Stankiewicz, nr albumu 415668
#Algorytm sortuje tablicę S (heap sortem) i wstawiając największe elementy z kopców na koniec tablicy, sumuje je, za każdym razem odejmując liczbe dni, która upłynęła 
#(w heap sorcie iterujemy od końca tablicy, dlatego liczba, którą odejmujemy wynosi days=n-step-1). Robimy to dopóki wartość danego elementu tablicy pomniejszona 
#o liczbę dni jest większa od 0 - wtedy możemy przerwać sortowanie tablicy, gdyż znamy już poprawny wynik.
#Wyjaśnienie:
#Chcemy zebrać jak najwięcej śniegu, dlatego bierzemy go z miejsc, gdzie jest 
#go najwięcej, kolejność nie jest ważna poza tym, żeby zebrać jak najwięcej największych porcji - algorytm ma podać tylko największą wartość, a nie kolejność, dlatego
#możemy założyć, że jeśli chcemy zebrać śnieg z danych obszarów, to zrobimy to w takiej kolejności, żeby nie odśnieżyć ich wcześniej, zbierając śnieg z innych obszarów 
#(zawsze da się to zrobić).
#Sniegu z kazdego obszaru ubywa tak samo, dopoki dany obszar nie jest pusty, dlatego to, czy najpierw zbierzemy wieksze wartosci, czy mniejsze z tych ktore chcemy zebrac, nie ma znaczenia.
#Algorytm ma zlozonosc O(nlogn)


from zad2testy import runtests

def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and T[l]>T[max_ind]:
        max_ind =l
    if r<n and T[r]>T[max_ind]:
        max_ind =r
    if max_ind!=i:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify(T,max_ind,n)

def build_heap(T):
    n=len(T)
    for i in range(n-1,-1,-1):
        heapify(T,i,n)


def snow( S ):
    n=len(S)
    build_heap(S)
    sum=0 #suma zebranego sniegu po (n-step-1) dniach
    for step in range(n-1,0,-1):
        x=S[0]-n+step+1
        if x<=0:
            return sum
        sum+=x
        S[0],S[step]=S[step],S[0]
        heapify(S,0,step)

    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
