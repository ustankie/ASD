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
    #P.append((B,True))
    for i in range(n):
        P[i]=(P[i][0],P[i][1],i)

    P2=sorted(P,key=lambda x:x[0])
    
    stops=sorted(P,key=lambda x:x[1],reverse=True)
    n=len(P)
    par=[[None,None] for _ in range(n)]
    
    stop_num=0
    j=0
    while j<n and stops[j][1]:
        stop_num+=1
        j+=1
    
    stops=stops[:stop_num]
    sub_sums=[0 for _ in range(stop_num)]

    s1=0
    all_sum=0
    for i in range(1,n):
        if P2[i][1]:
            sub_sums[s1]=all_sum
            s1+=1
        else:
            all_sum+=1


    F=[[float('inf'),float('inf')] for _ in range(stop_num)]
    par=[[None,None] for _ in range(stop_num)]

    F[0][0]=0
    F[1][0]=0
    F[2][0]=0
    
    F[1][1]=sub_sums[1]-sub_sums[0]    
    F[2][1]=sub_sums[2]-sub_sums[1]

    par[1][1]=0
    par[2][1]=1

  
    
    for i in range(3,stop_num):
        for j in range(1,4): 
            #F[i][0]=float('inf')
            if F[i][1]>F[i-j][0]+sub_sums[i]-sub_sums[i-j]:
                par[i][1]=i-j
                F[i][1]=F[i-j][0]+sub_sums[i]-sub_sums[i-j]
            
            if F[i][0]>F[i-j][1]:
                par[i][0]=i-j
                F[i][0]=F[i-j][1]

    
    goes=True
    if F[stop_num-1][0]<=F[stop_num-1][1]:
        goes=False
    R=[]
    p=stop_num-1
    while p!=None:
        R.append(stops[p][2])
        p=par[p][goes]
        goes=1-goes
    R=R[1:]
    return R[::-1]



    


        

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )

p = True
c = False

P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
(2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]

B = 20

print(drivers(P,B))