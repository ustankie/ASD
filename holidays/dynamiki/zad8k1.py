from zad8ktesty import runtests 

def napraw ( s, t ):
    n=len(s)
    m=len(t)


    F=[[0 for _ in range(m)]for _ in range(n)]
    F[0][0]=1-int(s[0]==t[0])
    for i in range(1,m):
        if t[i]==s[0]:
            F[0][i]=i
        else:
            F[0][i]=F[0][i-1]+1
    
    for i in range(1,n):
        if s[i]==t[0]:
            F[i][0]=i
        else:
            F[i][0]=F[i-1][0]+1       

    for i in range(1,n):
        for j in range(1,m):
            if s[i]==t[j]:
                F[i][j]=F[i-1][j-1]
            else:
                F[i][j]=min(F[i-1][j],F[i][j-1],F[i-1][j-1])+1

    #print(*F,sep="\n")
    return F[n-1][m-1]

runtests ( napraw )

s='mbsnotkdivadwngditcv'
t='bsaotkdimafdwcithyv'

s='swidry'
t='kawiory'
print(napraw(s,t))