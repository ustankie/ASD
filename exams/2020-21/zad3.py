from zad3testy import runtests
def find_max(A):
    n=len(A)
    max_ind=0
    for i in range(n):
        max_ind=max(max_ind,A[i][1])
    return max_ind
def compare(A,B):
    
def kintersect(A, k):
    n=len(A)
    m=find_max(A)
    #print(m)
    P=[[0,[]] for _ in range(m+1)]
    for i in range(n):
        for j in range(A[i][0],A[i][1]):
            P[j][0]+=1
            P[j][1].append(i)
    i=0
    max_cnt=0
    max_ind=0
    while i<(m+1):
        beginning=i
        count=1
        i+=1
        while i<(m+1) and P[i][0]>=k:
            i+=1
            count+=1
        if count>max_cnt:
            max_cnt=count
            max_ind=beginning
        i+=1
    return P[max_ind][1]

    



runtests(kintersect)
A=[(0, 4), (1, 10), (6, 7), (2, 8)]
k=3
print(kintersect(A,k))