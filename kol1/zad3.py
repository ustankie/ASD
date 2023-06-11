#from zad3testy import runtests
from queue import PriorityQueue

def strong_string(T,k,p):
    n=len(T)
    sum=0
    for i in range(0,n-p):
        a=PriorityQueue()
        for j in range(i,i+p):
            a.put(T[j])
        for j in range(k):
            a.get()
            sum+=a.get()
        print(sum)
    return -1


# # zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( strong_string, all_tests=False )
T=[7,9,1,5,8,6,2,12]
strong_string(T,4,5)
