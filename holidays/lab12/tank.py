def tank_a(L,S):
    n=len(S)
    
    fuel_refill=0

    i=0
    while i<n:
        j=i+L
        while j>=i and S[j]==False:
            j-=1
        fuel_refill+=1
        i=j

def tank_b(L,S):
    n=len(S)
    cheapest=[(S[i],i)for i in range(n)]
    cheapest.sort()
    cost=0
    access=0
    i=0
    while i<n:           
        while len(cheapest)>0 and cheapest[0][1]<i:
            print(cheapest,i)
            cheapest=cheapest[1:]
        if len(cheapest)==0:
            return cost
        print(cheapest,i,cost)
        if cheapest[0][1]==i:
            cost+=cheapest[0][0]*min(L,n-i)
            cheapest=cheapest[1:]
            i=min(i+L,n-1)
        else:
            lacks=cheapest[0][1]-i
            cost+=lacks*S[i]
            i=cheapest[0][1]
            cheapest=cheapest[1:]
    return cost

S=[7,4,1,23,4]
L=2
print(tank_b(L,S))



