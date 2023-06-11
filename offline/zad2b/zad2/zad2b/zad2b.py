#Urszula Stankiewicz, nr albumu 415668
#Algorytm sortuje malejąco tablicę S (merge sortem), a następnie sumuje elementy od największego, za każdym razem odejmując liczbe dni, która upłynęła 
#(czyli od kazdego S[i+1] argumentu tablicy odejmujemy step+1, gdzie step odjelismy od S[i]) dopóki wartość danego elementu tablicy pomniejszona o liczbę dni jest większa od 0. 
#Chcemy zebrać jak najwięcej śniegu, dlatego bierzemy go z miejsc, gdzie jest 
#go najwięcej, kolejność nie jest ważna poza tym, żeby zebrać jak najwięcej największych porcji - algorytm ma podać tylko największą wartość, a nie kolejność, dlatego
#możemy założyć, że jeśli chcemy zebrać śnieg z danych obszarów, to zrobimy to w takiej kolejności, żeby nie odśnieżyć ich wcześniej, zbierając śnieg z innych obszarów 
#(zawsze da się to zrobić).
#Sniegu z kazdego obszaru ubywa tak samo, dopoki dany obszar nie jest pusty, dlatego to, czy najpierw zbierzemy wieksze wartosci, czy mniejsze z tych ktore chcemy zebrac, nie ma znaczenia.
#Algorytm ma zlozonosc O(nlogn)


from zad2testy import runtests
sum=0
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=0
    j=0
    T=[0 for _ in range(n1+n2)]
    while i<n1 and j<n2:
        if T1[i]>T2[j]:
            T[i+j]=T1[i]
            i+=1
        else:
            T[i+j]=T2[j]
            j+=1
    
    while i<n1:
            T[i+j]=T1[i]
            i+=1
    
    while j<n2:
            T[i+j]=T2[j]
            j+=1
    return T


def MergeSort(T):
    n=len(T)
    if (n==1):
        return T
    mid=n//2
    L=T[:mid]
    R=T[mid:n]

    return merge(MergeSort(L),MergeSort(R))

def snow( S ):
    S=MergeSort(S)
    n=len(S)
    step=0
    sum=0
    while S[step]-step>0 and step<n:
         sum+=S[step]-step
         step+=1
         
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
