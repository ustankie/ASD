def maximum(S):
    return max_tab(S,len(S)-1)
def max_tab(T,l):
    if l==0:
        return T[0]
    a=max_tab(T,l-1)
    return max(a,T[l])

T=[0,120,4,3,90,20000]
print(maximum(T))