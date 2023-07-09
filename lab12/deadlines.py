def deadlines(A):
    n=len(A)
    A.sort(key=lambda x: x[0])
    A.sort(key=lambda x: x[1],reverse=True)
    
    print(A)
    K=[]
    max_profit=0
    days=0
    for i in range(n):
        if A[i][0]>days:
            max_profit+=A[i][1]
            K.append(A[i])
            days+=1
    return max_profit,K
        

A = [[2, 50],
     [1, 21],
     [2, 27],
     [3, 25],
     [2, 15],
    #  [2,21],
    #  [1,15]
]

print(deadlines(A))