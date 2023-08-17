from zad8ktesty import runtests 

def napraw ( s, t ):
    n=len(s)
    m=len(t)
    print(s)
    print(t)

    F=[[0 for _ in range(m)]for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if s[i]==t[j]:
                F[i][j]=max(F[i-1][j],F[i][j-1])+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
    diff=m-F[n-1][m-1]
    print(diff)
    count=0
    i=n-1
    j=m-1

    print(*F,sep="\n")
    while i>0 and j>0:
        up=0
        while i>0 and F[i-1][j]==F[i][j]:
            i-=1
            up+=1
        left=0
        while j>0 and F[i][j-1]==F[i][j]:
            j-=1
            left+=1
        # elif F[i][j-1]+1==F[i][j]:
        #     j-=1
        #     #count-=1

        i-=1
        j-=1

            #count+=1
            #count-=1
        count+=abs(up-left)
        if abs(up-left)>0 and up>0 and left>0:
            count+=1

        print(count,up,left,i,j)

    return count
#runtests ( napraw )

s='mbsnotkdivadwngditcv'
t='bsaotkdimafdwcithyv'

print(napraw(s,t))