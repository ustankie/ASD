#O(n^2)
from egz2atesty import runtests
from queue import PriorityQueue
# def left(i):
#     return 2*i+1
# def right(i):
#     return 2*i+2
# def parent(i):
#     return (i-1)//2


# def heapify(T,i,n):
#     l=left(i)
#     r=right(i)
#     max_ind=i
#     if l<n and (T[max_ind][0]>T[l][0] or (T[max_ind][0]==T[l][0] and T[max_ind][1]>T[l][1])):
#         max_ind=l
#     if r<n and (T[max_ind][0]>T[r][0] or (T[max_ind][0]==T[r][0] and T[max_ind][1]>T[r][1])):
#         max_ind=r
#     if i!=max_ind:
#         T[max_ind],T[i]=T[i],T[max_ind]
#         heapify(T,max_ind,n)

# # def build_heap(T):
# #     n=len(T)
# #     for i in range(n-1,-1,-1):
# #         heapify(T,i,n)

# # def heap_sort(T):
# #     n=len(T)
# #     build_heap(T)
# #     for i in range(n-1,0,-1):
# #         T[0],T[i]=T[i],T[0]
# #         heapify(T,0,i)
# def repair(A,i):
#     a=parent(i)
#     #print(A,i)
#     while a>=0 and (A[a][0]>A[i][0] or (A[a][0]==A[i][0] and A[a][1]>A[i][1])):
#         #print(A)
#         A[a],A[i]=A[i],A[a]
#         i=a
#         a=parent(a)
   
# def binsearch(A,i,j,x,T):
#     A=A.queue()
#     if i<j:
#         q=(i+j)//2  
#         #print(q) 
#         #if q>len(A):
#             #print(q)     
#         if A[q][0]==T and  A[q][0]!=x:
#             return binsearch(A,i,q-1,x,T)
#         if A[q][0]>= x:
#             #print(A[q][0],x)
#             while q>=0 and A[q][0]>=x:
#                 q-=1
#             return q+1
#         else:
#             return binsearch(A,q+1,i,x,T)
#     if A[i][0]>= x:
#         return i
#     while A[i][0]<x:
#         i+=1
#     return i

# def coal( A, T ):
#     n=len(A)
#     F=[[T,i] for i in range(n)]
#     for i in range(n):
#         j=binsearch(F,0,n-1,A[i],T)
        
#         if i==n-1:       
#             if len(A) == 800:
#                 print(F)
#             return F[j][1]
#         #F[0],F[j]=F[j],F[0]
#         #L=F[i:j:-1]
        
#         #F=L[::-1]+F[j:]
#         F[j][0]-=A[i]
#         repair(F,j)
#         print(F)

# def coal2( A, T ):
#     n=len(A)
#     F=[[T,i] for i in range(n)]
#     Q=PriorityQueue()
#     for i in range(n):
#         Q.put([T,i])
#     P=PriorityQueue()
    
#     for i in range(n):
#         a=[0,0]
#         #j=binsearch(Q,0,n-1,A[i],T)
#         while not Q.empty() and a[0]<A[i]:
#             a=Q.get()
#             if a[0]>=A[i]:
#                 a[0]-=A[i]
#                 if i==n-1:
#                     return a[1]
#             P.put(a)

#         while not P.empty():
#             Q.put(P.get())

def coal( A, T ):
    n=len(A)
    F=[T for i in range(n)]
    for i in range(n):
        j=0
        while j<n and F[j]<A[i]:
            j+=1
        F[j]-=A[i]
        if i==n-1:
            return j

   

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
A      = [2, 7, 6, 7, 6, 3, 10, 9, 2, 7]
T      = 10
print(coal(A,T))
