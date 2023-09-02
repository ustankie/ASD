from zad1testy import runtests


def read_solution (X,parent,i,reverse_it):
    sequence = []
    while i != None:
        sequence.append(X[i])
        i = parent[i]

    if reverse_it == True: return sequence[::-1]
    else: return sequence


def f_dec (a,b): return a < b


def f_inc (a,b): return b < a


def binary_search (s,x,F,f):
    a = 0
    b = len(s)-1

    while a <= b:
        m = int((a+b)//2)
        if x == F[s[m]]: break
        if f (x,F[s[m]]) == True: a = m+1
        else: b = m-1

    if f (x,F[s[m]]) == False: m -= 1
    return m

def find_the_sequence (X,F,parent,f,start,stop,increment):
    F[start] = 1
    s = [start]
    i = start+increment

    while i != stop:
        if f (X[i],X[s[-1]]): parent[i] = s[-1]; s.append(i); F[i] = len(s)
        elif f (X[s[0]],X[i]): s[0] = i; F[i] = 1; parent[i] = None
        else:
            j = binary_search (s,X[i],X,f)
            s[j+1] = i; parent[i] = s[j]; F[i] = j+2
        i += increment


def mr (X):
    n = len(X)

    decreasing_from_left_to_right = [None for _ in range (0,n)]
    parent_dec_from_l_to_r = [None for _ in range (0,n)]

    increasing_from_left_to_right = [None for _ in range (0,n)]
    parent_inc_from_l_to_r = [None for _ in range (0,n)]

    decreasing_from_right_to_left = [None for _ in range (0,n)]
    parent_dec_from_r_to_l = [None for _ in range (0,n)]

    find_the_sequence (X,decreasing_from_left_to_right,parent_dec_from_l_to_r,f_dec,0,n,1)
    find_the_sequence (X,increasing_from_left_to_right,parent_inc_from_l_to_r,f_inc,0,n,1)
    find_the_sequence (X,decreasing_from_right_to_left,parent_dec_from_r_to_l,f_dec,n-1,-1,-1)

    sought = 0
    type = "decreasing_from_left_to_right"

    def read (type,i):
        if type == "decreasing_from_left_to_right":
            return decreasing_from_left_to_right[i]
        elif type == "increasing_from_left_to_right":
            return increasing_from_left_to_right[i]
        elif type == "mixed":
            return decreasing_from_left_to_right[i]+decreasing_from_right_to_left[i] - 1

    for i in range(0, n):
        if decreasing_from_left_to_right[i] > read (type,sought):
            sought = i
            type = "decreasing_from_left_to_right"
        if increasing_from_left_to_right[i] > read (type,sought):
            sought = i
            type = "increasing_from_left_to_right"
        if decreasing_from_left_to_right[i]+decreasing_from_right_to_left[i]-1 > read (type,sought):
            sought = i
            type = "mixed"

    if type == "mixed":
        A = read_solution (X,parent_dec_from_l_to_r,sought,True)
        B = read_solution (X,parent_dec_from_r_to_l,sought,False)
        print(len(A),len(B))
        return A+B[1:]
    elif type == "decreasing_from_left_to_right":
        #print('a')
        return read_solution (X,parent_dec_from_l_to_r,sought,True)
    else:
        print('a')
        return read_solution( X,parent_inc_from_l_to_r,sought,False)


runtests (mr)