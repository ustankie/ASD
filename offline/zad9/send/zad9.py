#Urszula Stankiewicz, nr albumu: 415668
#Algorytm posługuje się tablicą F[i][2], gdzie F[i][0] - minimalny koszt dotarcia do pola i niewykorzystawszy jeszcze skoku 2*T
#F[i][1] - minimalny koszt dotarcia do pola i wykorzystawszy skok 2*T
#F[i][0]=min(F[j][0])+C[i], 0<=j<i, 0<=O[i]-O[j]<=T
#F[i][1]=min(F[j][0])+C[i], 0<=j<i, 0<=O[i]-O[j]<=2*T
#Najpierw sortujemy tablice O,C wg rosnących odległości parkingów, a potem w podwójnej pętli for uzupełniamy tablicę.
#Algorytm ma złożoność O(n^2)

from zad9testy import runtests
def merge(T1,T2,C1,C2,L):
    n1=len(T1)
    n2=len(T2)

    i=0
    j=0

    T=[]
    C=[]
    while i<n1 and j<n2:
        if T1[i]<T2[j]:
            if T1[i]<L:
                T.append(T1[i])
                C.append(C1[i])
            i+=1
        else:
            if T2[j]<L:
                T.append(T2[j])
                C.append(C2[j])
            j+=1
    while i<n1:
        if T1[i]<L:
            T.append(T1[i])
            C.append(C1[i])
        i+=1
    
    while j<n2:
        if T2[j]<L:
            T.append(T2[j])
            C.append(C2[j])
        j+=1  
    return T,C   

def merge_sort(T,C,L):
    n=len(T)
    if n==1:
        return T,C
    q=n//2
    LE=T[:q]
    R=T[q:]
    C1=C[:q]
    C2=C[q:]
    T1,C1=merge_sort(LE,C1,L)
    T2,C2=merge_sort(R,C2,L)
    return merge(T1,T2,C1,C2,L)

def min_cost( O, C, T, L ): 
    O,C=(merge_sort(O,C,L))
    O.append(L)
    C.append(0)
    O=[0]+O
    C=[0]+C

    n=len(O)

    F=[[float('inf'),float('inf')]for _ in range(n)]
    F[0][0]=0
    F[0][1]=0

    for i in range(1,n):
        j=i-1
        while j>=0 and O[i]-O[j]<=T:
            F[i][0]=min(F[i][0],F[j][0])
            F[i][1]=min(F[i][1],F[j][1])
            j-=1
        while j>=0 and O[i]-O[j]<=(2*T):
            F[i][1]=min(F[i][1],F[j][0])
            j-=1
        F[i][0]+=C[i]
        F[i][1]+=C[i]

    return min(F[n-1])

        

runtests( min_cost, all_tests = True )

