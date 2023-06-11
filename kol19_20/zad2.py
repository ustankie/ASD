
def partition(T,p,r):
    x=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<T[r]:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[i],T[r]=T[r],T[i]
    return i

def quick_sort(T,p,r):
    if p<r:
        q=partition(T,p,r)
        if q>=r:
            quick_sort(T,p,q-1)
        elif q<=p:
            quick_sort(T,q+1,r)

T=[455,1266,2344,67333,123,43,114577]
p=2
q=5
quick_sort(T,0,len(T)-1)
R=[T[i]for i in range(p,q+1)]
print(R)