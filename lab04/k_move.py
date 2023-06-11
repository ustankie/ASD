def k_move(T,k): #???? Czy można tych operacji uzywac?
    n=len(T)
    T=T[n-k:]+T[:n-k]
    print(T)


T=[0,1,2,3,4,5,6,7,8,9]
k_move(T,4)