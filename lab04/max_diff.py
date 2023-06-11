def min_max(T):
    n=len(T)
    min_val=float("inf")
    max_val=0
    
    for i in range(n):
        min_val=min(min_val,T[i])
        max_val=max(max_val,T[i])
    return max_val,min_val

def are_zeros(T):
    n=len(T)
    for i in range(n):
        if T[i][2]==0:
            return True
    return False
    
def max_diff(T):
    n=len(T)
    max_val,min_val=min_max(T)
    k=max_val-min_val
    print(k)
    B=[[None,None,0] for i in range(n)]
    b_size=k//n
    for i in range(n):
        x=int((T[i]-min_val)*(n-1)//k)
        print((T[i]),k,x)

        if B[x][0]==None:
            B[x][0]=T[i]
        if B[x][1]==None:
            B[x][1]=T[i]
        
        if B[x][0]>T[i]:
            B[x][0]=T[i]
        if B[x][1]<T[i]:
            B[x][1]=T[i]

        B[x][2]+=1
    max_diff=0
    num=(0,0)

    if not are_zeros(B):
        max_p=B[0][1]
        for i in range(1,n):
            x=B[i][0]-max_p
            if x>max_diff:
                max_diff=x
                num=max_p,B[i][0]
            max_p=B[i][1]
    else:
        i=0
        while i<n: 
            max_p=B[i][1]
            i+=1
            while i<n and B[i][2]!=0:
                max_p=B[i][1]
                i+=1

            while i<n and B[i][2]==0:
                i+=1
            if i<n:
                x=B[i][0]-max_p
                if x>max_diff:
                    max_diff=x
                    num=max_p,B[i][0]
            

    print(B)
    return max_diff,num

T1=[3,5,5.5,2,8,4,9]
T=[20,23,43,54,23]
T3=[7,1,2,3,4,5]
print(max_diff(T))
    