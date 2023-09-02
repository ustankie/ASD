from zad1ktesty import runtests

def roznica( S ):
    n=len(S)
    # print(S)
    prefix=[0 for _ in range(n)]

    if S[0]=='1':
        prefix[0]=1
    
   

    for i in range(1,n):
        prefix[i]=prefix[i-1]
        if S[i]=='1':
            prefix[i]+=1
    # print(prefix)
    if prefix[n-1]==n:
        return -1
    
    max_diff=-1

    for i in range(n):
        for j in range(i+1,n):
            
            if i==0:
                diff=(j-i+1-2*(prefix[j]))
                # if diff==j-i+1:
                #     diff=-1
            else:
                diff=(j-i+1-2*(prefix[j]-prefix[i-1]))
                # if diff==j-i+1:
                #     diff=-1
            max_diff=max(max_diff,diff)
            # if (i,j)==(1,5):
            #     print(diff,i,j)

    return max_diff



    

runtests ( roznica )
S='10111110000111101110100101101010111010011110100010'
print(roznica(S))