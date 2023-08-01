
def countVowelStrings(n):
    if n==1:
        return 5

    F=[[0 for _ in range(5)]for _ in range(n+1)]

    for i in range(1,n+1):
        F[i][0]=1

    for i in range(1,5):
        F[1][i]=1
        #print(i)
        F[2][i]=F[2][i-1]+i+1
    
    
    
    for i in range(3,n+1):
        for j in range(1,5):
            F[i][j]=F[i-1][j]+F[i][j-1]

    return F[n][4]


n=2
print(countVowelStrings(n))