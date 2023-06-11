#Urszula Stankiewicz, nr albumu: 415668
#Algorytm na początek odwraca słowa w tablicy w taki sposób, by były każde było jak najwcześniej położone w porządku leksykograficznym - np. słowo "tok" zostanie zamienione
#na słowo "kot", słowo "tsokt" na "tkost", ale słowo "pies" nie zostanie zamienione. Następnie sortujemy tablicę alfabetycznie (merge sort) i zliczamy występujące teraz już
#obok siebie słowa równoważne. Po każdym bloku słów porównujemy uzyskaną sumę z sumą maksymalną i, w razie potrzeby, aktualizujemy ją.
#Algorytm ma złożoność O(N+nlogn)
from zad3testy import runtests

def strong_string(T):
    def merge(T1,T2):
        n1=len(T1)
        n2=len(T2)

        i=0
        j=0

        T=["" for _ in range(n1+n2)]
        while i<n1 and j<n2:
            if T1[i]>T2[j]:
                T[i+j]=T2[j]
                j+=1         
            else:
                T[i+j]=T1[i]
                i+=1
        while j<n2:
            T[i+j]=T2[j]
            j+=1
            
        while i<n1:
            T[i+j]=T1[i]
            i+=1

        return T

    def MergeSort(T):
        n=len(T)
        if n==1:
            return T
        mid=n//2
        L=T[:mid]
        R=T[mid:]

        return merge(MergeSort(L),MergeSort(R))
    def reverse(T): #odwraca słowa tak, by były jak najwcześniejsze leksykograficznie
        n=len(T)
        for i in range(n):
            k=len(T[i])
            x=T[i][::-1]
            if x<T[i]:
                T[i]=x        
            
    def strongest(T):
        n=len(T)
        #układamy słowa i sortujemy tablicę
        reverse(T)
        T=MergeSort(T)

        max_strength=0
        i=1
        while i<(n): #zliczamy poszczególne słowa równoważne
            s=1
            while i<(n) and (T[i-1]==T[i] ):
                s+=1
                i+=1
            max_strength=max(max_strength,s) #aktualizujemy siłę maksymalną
            i+=1
        return max_strength
    return strongest(T)



# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
