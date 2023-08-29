from kol2atesty import runtests
def binsearch(T,x):
    i=0
    j=len(T)-1

    while i<=j:
        q=(i+j)//2
        if T[q][0]==x:
            return q
        if T[q][0]<x:
            i=q+1
        else:
            j=q-1
    return i

def drivers( P, B ):
    n=len(P)
    P2=sorted(P,key=lambda x:x[0])
    stops=sorted(P,key=lambda x:x[1],reverse=True)
    par=[None for _ in range(n)]
    s=0

    print(stops)
    print(P,len(P))

    F=[[0,float('inf')] for _ in range(n)]

    curr_ind=0
    if P2[0][1]==False:
        F[0][0]=1
        F[0][1]=1
    else:
        s+=1
    
    # for i in range(1,3):
    #     if P[i][1]==False:
    #         F[i][0]=F[i-1][0]+1
    #         F[i][1]=F[i-1][1]+1
    #     else:
    #         s+=1
    #         F[i][0]=F[i-1][1]
    #         F[i][1]=F[i-1][0]
    #         if i==2:
    #             F[i][0]=max(F[i-1][1],F[0][1])
    #             F[i][1]=min(F[i-1][0],F[0][0])

    for i in range(1,n):
        if P2[i][1]:
            
            if s==0:
                F[i][0]=0
                F[i][1]=0
            if s>0:
                print(stops[s-1])
                if F[i][1]>F[stops[s-1][0]-2][1]:
                    par[i]=stops[s-1][0]-2
                F[i][0]=max(F[stops[s-1][0]-2][0],F[i][0])
                F[i][1]=min(F[stops[s-1][0]-2][1],F[i][1])
                print(par)
            if s>1:
                if F[i][1]>F[stops[s-2][0]-2][1]:
                    par[i]=stops[s-2][0]-2
                F[i][0]=max(F[stops[s-2][0]-2][0],F[i][0])
                F[i][1]=min(F[stops[s-2][0]-2][1],F[i][1])
            if s>2:
                if F[i][1]>F[stops[s-3][0]-2][1]:
                    par[i]=stops[s-3][0]-2
                F[i][0]=max(F[stops[s-3][0]-2][0],F[i][0])
                F[i][1]=min(F[stops[s-3][0]-2][1],F[i][1])
                
            s+=1
        else:
            if P2[i-1][1]:
                F[i][0]=F[i-1][0]+1
                F[i][1]=F[i-1][1]+1               
            else:
                F[i][0]=F[i-1][0]+1
                F[i][1]=F[i-1][1]+1
            par[i]=i-1
    
    R=[]
    print(*F,sep="\n")

    # p=n-1
    # s-=1
    # while p>0 and s>=0:
    #     if F[stops[s-1][0]][1]-2==F[p][1]:
    #         p=stops[s-1][0]-2
    #         s-=1
    #     elif p>1 and F[stops[s-2][0]][1]-2==F[p][1]:
    #         p=stops[s-2][0]-2
    #         s-=2
    #     else:
    #         p=stops[s-3][0]-2
    #         s-=3

    #     if p>0:# and P[p][1]:
    #         R.append(p+1)
        
    #     p-=1
    print(par)
    p=n-1
    while p!=None:
        print(p+1)
        if P2[p][1]:
            x=binsearch(P,p+1)
            R.append(x)
        p=par[p]
    return R[::-1]
    


        

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( drivers, all_tests = False )

p = True
c = False

P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
(2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]

B = 20

print(drivers(P,B))