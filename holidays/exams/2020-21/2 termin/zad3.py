from zad3testy import runtests
from math import log2


def lamps( n,L ):
    m=len(L)

    color=[0 for _ in range(n)]
    blue=0
    max_blue=0

    for i in range(m):
        for j in range(L[i][0],L[i][1]+1):
            if color[j]==2:
                blue-=1
            color[j]=(color[j]+1)%3
            if color[j]==2:
                blue+=1
        max_blue=max(max_blue,blue)

    
    return max_blue

    
runtests( lamps )


