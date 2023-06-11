# def counting_sort(T,n):
#     B=[0 for _ in range(n)]
#     R=[None for _ in range(n)]
    
#     for i in range(n):
#         B[T[i]]+=1
#     for i in range(1,n):
#         B[i]+=B[i-1]
#     for i in range(n-1,-1,-1):
#         R[B[T[i]]-1]=T[i][0]
#         B[T[i]]-=1

def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    R=[[0 ,0]for i in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][0]<=T2[j][0]:
            R[i+j]=T1[i]
            i+=1
        else:
            R[i+j]=T2[j]
            j+=1
    while i<n1:
        R[i+j]=T1[i]
        i+=1
    while j<n2:
        R[i+j]=T2[j]
        j+=1
    return R

def merge_sort(T):
    n=len(T)
    if n==1:
        return T
    q=n//2
    L=T[:q]
    R=T[q:]

    return merge(merge_sort(L),merge_sort(R))
def chaos_index(T):
    n=len(T)
    R=[(T[i],i)for i in range(n)]
    R=merge_sort(R)
    print(R)
    k=0
    for i in range(n):
        if abs(R[i][1]-i)>k:
            k=abs(R[i][1]-i)
    return k

T=[0,2,1.1,2,0,5]
# T=merge_sort(T)
# print(T)
print(chaos_index(T))