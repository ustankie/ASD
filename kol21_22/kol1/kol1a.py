from kol1atesty import runtests

def g(T):


    def merge(T1,T2):
        n1=len(T1)
        n2=len(T2)
        #print(n1,n2)
        i=0
        j=0

        T=["" for _ in range(n1+n2)]
        while i<n1 and j<n2:
            #print(T1[i],T2[j])
            if T1[i]>T2[j]:
                T[i+j]=T2[j]
                j+=1
            # elif len(T1[i])==len(T2[j]):
            #     if T1[i]>T2[j]:
            #         T[i+j]=T2[j]
            #         j+=1
            #     else:
            #         T[i+j]=T1[i]
            #         i+=1           
            else:
                T[i+j]=T1[i]
                i+=1
        while j<n2:
            T[i+j]=T2[j]
            j+=1
            
        while i<n1:
            T[i+j]=T1[i]
            i+=1
        #print(T)
        return T

    def MergeSort(T):
        n=len(T)
        if n==1:
            return T
        mid=n//2
        L=T[:mid]
        R=T[mid:]
        #print(L,R)
        return merge(MergeSort(L),MergeSort(R))
    def reverse(T):
        n=len(T)
        R=[""for i in range(n)]
        n1=0
        for i in range(n):
            if len(T[i])>1:
                a=T[i][::-1]
                if a!=T[i]:
                    R[n1]=a
                    n1+=1
        return R[:n1],n1

    def strongest(T):
        n=len(T)
        
        R,n1=reverse(T)
        T=MergeSort(T+R)
        #print(T)
        max_strength=0
        i=1
        while i<(n1+n):
            s=1
            while i<(n1+n) and (T[i-1]==T[i] ):
                s+=1
                i+=1
            max_strength=max(max_strength,s)
            i+=1
        return max_strength
    return strongest(T)

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
