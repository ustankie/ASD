#1)QS w pamięci O(logn) v
#2)QS bez rekurencji, z własnym stosem v
#3) Wstawianie do kopca binarnego v
#4)k posortowanych list odsylaczowych -> scalić w jedno O(nlogk) -> scalamy parami po 2 listy ze soba /kopiec v
#5)struktura danych z operacjami -> wszystkie w O(logn) #kopiec - na poziomach parzystych dzieci wieksze od parentow, na nieparzystych na odwrot
#kopec minimum i maksimum o tych smych danych, odsyłacze miedzy kopcami
#   -insert
#   -extract min
#   -extraxt max
#6) struktura danych
# #dwa kopce - wieksze od x i mniejsze od x -> jesli kopce tego samego rozmiaru -> mediana, z jendego wyjmujemy element -> mediana, z drugiego wstawiamy do kółeczka

#   -insert
#   -extract median
#7) tablica k-chaotyczna - kazdy el pod swoim miejscu +-k -> algorytn sortujacy nlogk v?
from collections import deque

def partition(T,p,r):
    x=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i

#1) liczymy dlugosci przedzialow, robimy jako pierwszy ten ktory jest krotszy
def QuickSort_logn(T,p,r):
    while p<r:
        q=partition(T,p,r)
        if (q-p)<(r-q):
            QuickSort(T,p,q-1)
            p=q+1
        else:
            QuickSort(T,q+1,r)
            r=q-1
def QuickSort_stos(A,p,r): #najpierw dłuższy push
    s=stack()
    s.push(p,r)
    while not s.isempty():
        p,r=s.pop()
        if (p<r):
            q=partition(A,p,r)
            if (q-p)>(r-q):
                s.push(p,q-1)
                s.push(q+1,r)
            else:
                s.push(q+1,r)
                s.push(p,q-1)

#3)
class Heap:
    def __init__(self,n):
        self.T=[0]*n
        self.size=0

def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2

def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and T[max_ind]<T[l]:
        max_ind=l
    if r<n and T[max_ind]<T[r]:
        max_ind=r
    if i!=max_ind:
        T[max_ind],T[i]=T[i],T[max_ind]
        heapify(T,max_ind,n)

def insert(H,x):
    p=parent(H.size) 
    H.T[H.size]=x
    i=H.size
    H.size+=1
    
    while p>=0:
        if H.T[p]<H.T[i]:
            H.T[p],H.T[i]=H.T[i],H.T[p]
        else:
            break
        i=p
        p=parent(p)

def


H=Heap(10)
insert(H,1)
insert(H,4)
insert(H,0)
insert(H,9)
T=[1,2,53,2,0,6,7,22,54,67]
QuickSort_stos(T,0,len(T)-1)
print(T,0,len(T)-1)