from random import uniform
class Node():
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def create(n):
    p=Node(uniform(0.0,10.0))
    q=p
    for i in range(n):
        a=Node(uniform(0.0,10.0))
        p.next=a
        p=a
    return q

def wypisz(p):
    while p!=None:
        print(p.val)
        p=p.next

def find_num(p):
    n=0
    p=p.next
    while p!=None:
        n+=1
        p=p.next
    return n

def bucket_sort(p):
    n=find_num(p)
    q=p
    T=[[[None,None] for i in range(n)]for i in range(n)]
    p=p.next
    while p!=None:
        z=int(p.val*n//10)
        j=0
        while T[z][j][0]!=None:
            j+=1
        T[z][j][0]=p.val
        T[z][j][1]=p
        p=p.next
    #print(T)

    R=[0]
    r=q
    for i in range(n):
        j=0
        while T[i][j][0]!=None:
            j+=1
        if j>0:
            R=merge_sort(T[i][:j])
            #print()
            for k in range(j):
                q.next=R[k][1]
                #wypisz(a)
                q=q.next
                
    q.next=None
    return r
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    R=[[0 ,0]for i in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][0]<T2[j][0]:
            R[i+j][0]=T1[i][0]
            R[i+j][1]=T1[i][1]
            i+=1
        else:
            R[i+j][0]=T2[j][0]
            R[i+j][1]=T2[j][1]
            j+=1
    while i<n1:
        R[i+j][0]=T1[i][0]
        R[i+j][1]=T1[i][1]
        i+=1
    while j<n2:
        R[i+j][0]=T2[j][0]
        R[i+j][1]=T2[j][1]
        j+=1
    return R

def merge_sort(T):
    n=len(T)
    #print(T)
    if n==1:
        return T
    q=n//2
    L=T[:q]
    R=T[q:n]
    return merge(merge_sort(L),merge_sort(R))
    

p=create(10)
wypisz(p)
print("\n",find_num(p))
p=bucket_sort(p)
wypisz(p)
#A=[0,34,6,2,46]
#print(merge_sort(A))