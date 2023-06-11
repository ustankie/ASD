# #Urszula Stankiewicz, nr albumu 415668
# #Algorytm wykorzystuje kolejkę priorytetową PriorityQueue, wrzucając do niej wszystkie wartości z danego
# #przedziału od i do i+p-1 (czynność tę powtarzamy dla każdego przedziału). 
# #Następnie wyciągamy z kolejki p-k-1 wartości (tyle będzie elementów mniejszych od k-tego największego)
# #i p-k-ty element będzie zarazem k-tym największym, więc dodajemy go do sumy. Algorytm działa poprawnie, ponieważ 
# #dla każdego z przedziałów od i do i+p-1(dla każdej iteracji zewnętrznej pętli for) znajdujemy k-ty największy element w tym przedziale
# #dodając go do sumy.
# #Algorytm ma złożoność O(n*p)
from kol1testy import runtests
from queue import PriorityQueue
# def left(i):return 2*i+1
# def right(i):return 2*i+2
# def parent(i):return (i-1)//2
# def heapify(T,i,n):
#     l=left(i)
#     r=right(i)
#     max_ind=i
#     if l<n and T[l]>T[max_ind]: max_ind=l
#     if r<n and T[r]>T[max_ind]: max_ind=r
#     if max_ind!=i:
#         T[i],T[max_ind]=T[max_ind],T[i]
#         heapify(T,max_ind,n)
# def build_heap(T):
#     n=len(T)
#     for i in range(parent(n-1),-1,-1):
#         #print(i)
#         heapify2(T,i,n)

# def heapify2(T,i,n):
#     l=left(i)
#     r=right(i)
#     max_ind=i
#     if l<n and T[l]<T[max_ind]: max_ind=l
#     if r<n and T[r]<T[max_ind]: max_ind=r
#     if max_ind!=i:
#         T[i],T[max_ind]=T[max_ind],T[i]
#         heapify(T,max_ind,n)
# def heap_sort(T):
#     n=len(T)
#     build_heap(T)
#     for i in range(n-1,0,-1):
#         T[0],T[i]=T[i],T[0]
#         heapify2(T,0,i)
# def find_x(T,x):
#     n=len(T)
#     for i in range(n):
#         if T[i]==x:
#             return i
# def ksum(T, k, p):
#     n=len(T)
#     sum=0
#     A=T[:p]

#     heap_sort(A)
#     print(A)

#     sum+=A[k-1]
#     for i in range(1,n-p+1):
#         print(sum)
#         a=find_x(A,T[i-1])
#         A[a]=T[i+p-1]
#         print(A)
#         q=parent(a)

#         while q>=0:
#             heapify(A,q,p)
#             q=parent(q)
#         build_heap(A)

#         print(A)

#         sum+=A[k-1]

#     return sum







# # zmien all_tests na True zeby uruchomic wszystkie testy
# #runtests( ksum, all_tests=True )
# T=[7,9,1,5,8,6,2,12]
# # heap_sort(T)
# # print(T)
# print(ksum(T,4,5))
def median_of_medians(T):
    n=len(T)
    if n==1:
        return T[0]
    B=[T[i:i+5] for i in range(0,n,5)]
    m=len(B)
    for i in range(m):
        quicksort(B[i],0,len(B[i])-1)
    Medians=[B[i][len(B[i])//2]for i in range(m)]
    return median_of_medians(Medians)
def find_x(T,x):
    n=len(T)
    for i in range(n):
        if T[i]==x:
            return i
def select(T,p,r,k):
    if p==r and k==p:
        return T[k]
    if p<r:
        x=median_of_medians(T[p:r+1])
        median=find_x(T,x)
        q=partition(T,p,r,median)
        if q==k:
            return T[q]
        if k<q:
            return select(T,p,q-1,k)
        else:
            return select(T,q+1,r,k)
def partition(T,p,r,k):
    x=T[k]
    T[k],T[r]=T[r],T[k]
    i=p-1
    for j in range(p,r):
        if T[j]<=x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[i],T[r]=T[r],T[i]
    return i
def quicksort(T,p,r):
    if p<r:
        q=partition(T,p,r,r)
        quicksort(T,p,q-1)
        quicksort(T,q+1,r)

def ksum(T, k, p):
    n=len(T)
    sum=0
    for i in range(n-p+1):
        A=T[i:i+p]
        sum+=select(A,0,p-1,p-k)
    return sum
runtests( ksum, all_tests=True )
#T=[7,9,1,5,8,6,2,12]
# heap_sort(T)
# print(T)
#print(ksum(T,4,5))