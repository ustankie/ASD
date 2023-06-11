def counting_sort(T,j):
    n=len(T)
    #print(T)
    B=[0 for i in range(27)]
    R=[0 for i in range(n)]
    #print(T[0][j])
    for i in range(n):
        t=len(T[i])-1
        if t<j:
            B[0]+=1
        else:
            B[ord(T[i][j])-ord('a')+1]+=1
    #print(B)
    for i in range(26):
        B[i]+=B[i-1]
    #print(B)
    for i in range(n-1,-1,-1):
        t=len(T[i])-1
        if t<j:
            R[B[0]-1]=T[i]
            B[0]-=1
        else:
            R[B[ord(T[i][j])-ord('a')+1]-1]=T[i]
            B[ord(T[i][j])-ord('a')+1]-=1
    for i in range(n):
        T[i]=R[i]
def radix_sort(T):
    n=len(T)
    t=0
    for i in range(n):
        x=len(T[i])
        if t<x:
            t=x
    
    for i in range(t-1,-1,-1):
        counting_sort(T,i)
        #print(T)

T=["kra","art","kot","kitt","ati","kil","kit","gitara","pies","owca","ola","ogrod","poziomkaaa"]
radix_sort(T)
print(T)