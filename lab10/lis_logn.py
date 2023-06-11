def binsearch(A,x):
    n=len(A)
    i=0
    j=n-1
    while i<=j:
        q=(j+i)//2
        if A[q]<x:
            i=q+1
        else:
            j=q-1

    return i
    

def lis(A):
    n=len(A)
    F=[]
    for i in range(n):
        a=binsearch(F,A[i])
        #print(F,a)
        if a==len(F):
            F.append(A[i])
        else:
            F[a]=A[i]
            
    return len(F),F



a = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
print(lis(a))


        