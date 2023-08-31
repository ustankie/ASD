def deadlines(A):
    n = len(A)

    for i in range(n):
        A[i] = (A[i][0], A[i][1], i)

    A.sort(key=lambda x: x[0])
    A.sort(key=lambda x: x[1], reverse=True)

    R=[]
    gain=0
    day=0
    for i in range(n):
        if A[i][0]>day:
            gain+=A[i][1]
            day+=1
            R.append(A[i][2])
    
    return gain,R



A = [[2, 50],
     [1, 21],
     [2, 27],
     [3, 25],
     [2, 15],
     #  [2,21],
     #  [1,15]
     ]
print(deadlines(A))
