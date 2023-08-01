from zad3testy import runtests
from math import log10

def selection_sort(T):
    n=len(T)
    for i in range(n-1):
        nm=i
        for j in range(i+1,n):
            if T[j]<T[nm]:
                nm=j
        T[i],T[nm]=T[nm],T[i]

                 
    
def fast_sort(tab, a):
    n=len(tab)
    R=[[]for _ in range(n)]

    for i in range(n):
        x=log10(tab[i])/log10(a)
        ind=int(x*n)
        R[ind].append(tab[i])
    
    for i in range(n):
        selection_sort(R[i])
    
    j=0
    for i in range(n):
        for x in R[i]:
            tab[j]=x
            j+=1


    return tab



runtests( fast_sort )
