#Urszula Stankiewicz, nr_albumu: 415668
#Algorytm na początku tworzy tablicę S, gdzie S[i] zawiera informację o ilości ropy w plamie, której częścią jest pole [0][i] w tablicy T,
#przy czym jeżeli dana plama obejmuje jakieś dwa pola [0][i],[0][j], to S[i] będzie zawierało wielkość plamy, a S[j]=0. Jest to poprawne, ponieważ
#jeżeli raz zbierzemy ropę z danej plamy, to nie możemy tego zrobić po raz drugi. Ponadto zależy nam, by mieć ewentualny dostęp do ropy jak najwcześniej w czasie
#drogi, by w razie braków móc uzupełnić zapas paliwa. W następnym kroku tworzymy tablicę B, gdzie B[i] oznacza ilość paliwa w baku na pozycji [0][i] tablicy T
#oraz tablicę F, gdzie F[i] to minimalna ilość tankowań, by dojechać do pola [0][i] tablicy T. B[0]=S[0],B[i]=B[i-1]-1 (jeżeli B[i-1]-1>=0) v (wpp)max(S[j]) gdzie j={1,...,i} 
#i S[j] nie była jeszcze tankowana. F[0]=1 (tankujemy na polu (0,0)),F[i]=F[i-1] (jeżeli B[i-1]-1>=0) v F[i]=F[i-1]+1 (wpp).
#W pętli for (0...len(T[0])) wyliczamy poszczególne wartości obu funkcji i zwracamy F[len(T[0])-1].
#Algorytm jest poprawny, ponieważ dla każdego pola oblicza minimalną ilość tankowań, więc w szczególności robi to dla pola (0,m-1)
#Złożoność: O(m*n+m)=O(m*n)
from zad8testy import runtests
from collections import deque
def sum_stains(T):
    n=len(T)
    m=len(T[0])
    S=[0 for _ in range(m)]
    move=[(-1,0),(1,0),(0,1),(0,-1)]
    Q=deque()
    for i in range(m):
        if T[0][i]:
            Q.append((0,i))
            S[i]+=T[0][i]
            T[0][i]=0
            while len(Q)>0:
                u,v=Q.popleft()                
                for um,vm in move:
                    a=u+um
                    b=v+vm
                    if a>=0 and a<n and b>=0 and b<m and T[a][b]:
                        S[i]+=T[a][b]
                        T[a][b]=0
                        Q.append((a,b))
    return S
                
    

def plan(T):
    S=sum_stains(T)
    m=len(T[0])
    B=[0 for _ in range(m)]
    F=[0 for _ in range(m)]

    B[0]=S[0]
    F[0]=1
    S[0]=0

    for i in range(1,m):
        if B[i-1]-1>=0:
            B[i]=B[i-1]-1
            F[i]=F[i-1]
        else:
            max_stain=0
            max_ind=1
            for j in range(1,i):
                if S[j]>max_stain:
                    max_ind=j
                    max_stain=S[j]
            B[i]=max_stain
            S[max_ind]=0
            F[i]=F[i-1]+1

    return F[m-1]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

T0 = [
    [1, 0],
    [0, 0],
]
T1 = [
    [3, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]
T2 = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
T3 = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

r0_T4 = [6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1]
T4 = [
         r0_T4
     ] + (
             [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (len(r0_T4) - 1)
     )

T5 = [
    [1, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

T6 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T7 = [
    [5, 0, 1, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
]

T8 = [
    [3, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

T9 = [[2,0,2,0,5],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
        ]
T=T1
# print(*T,sep="\n")
# print(plan(T))

