from zad3testy import runtests
from queue import PriorityQueue

def strong_string(T,k,p):
    n=len(T)
    #print("a")
    sum=0
    for i in range(0,n-p+1):
        #print("a")
        a=PriorityQueue(n)
        # print(a.qsize())
        for j in range(i,i+p):
            a.put(T[j]) 
            #print(T[j])          
        #print("b")

        for j in range(p-k):
            s=a.get()
        sum+=a.get()
        # print()
        # print(sum)
    return sum


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=False )
# T=[7,9,1,5,8,6,2,12]
# print(strong_string(T,4,5))
