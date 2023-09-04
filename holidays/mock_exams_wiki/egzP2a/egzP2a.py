from egzP2atesty import runtests

def partition(T,p,r,x):
    T[r],T[x]=T[x],T[r]
    x=T[r][1]
    i=p-1
    for j in range(p,r):
        # print(T[j],x)
        if T[j][1]>x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i

def selection_sort(T):
    n = len(T)
    for i in range(n-1):
        nm = i
        for j in range(i+1, n):
            if T[j][1] > T[nm][1]:
                nm = j
        T[nm], T[i] = T[i], T[nm]

def median_of_medians(T,a=True):
    n = len(T)
    if n == 1:
        return T[0]

    B = [T[i:i+5] for i in range(0, n, 5)]
    # if a:
    #     for i in range(n):
    #         B[i//5][i%5]=T[i],i

    m = len(B)
    for i in range(m):
        selection_sort(B[i])

    medians = [B[i][len(B[i])//2]for i in range(m)]

    return median_of_medians(medians,False)
def find_x(T,p,r,x):
    for i in range(p,r+1):
        if T[i]==x:
            return i
def qselect(T,p,r,k):
    if p==r and k==p:
        return T[k]
    if p<r:
        x=median_of_medians(T[p:r+1])
        median=find_x(T,p,r,x)
        q=partition(T,p,r,median)
        if q==k:
            return T[q]
        if q>k:
            return qselect(T,p,q-1,k)
        else:
            return qselect(T,q+1,r,k)
        
def zdjecie(T, m, k):
    n=len(T)
    if T[0][0]==458:
        print(T)
    # print(n)
    add=[0 for _ in range(m+1)]
    add[m-1]=0
    for i in range(m-2,-1,-1): 
        add[i]=add[i+1]+1
    for i in range(1,m):
        add[i]+=add[i-1]
    # print(add)
    A=sorted(T,key=lambda x: x[1],reverse=True)
    last_end=n-1
    for i in range(m):        
        if i==0:
            a=n-1
        else:
            a=n-i-k*i
        # print(a)
        print(qselect(T,0,n-1,a),A[a])
        last_end=a
        # print(T)
        # print()
    # print(T)
    
    # print(sorted(T,key=lambda x: x[1],reverse=True))
    A=T[:]
    s=0
    for j in range(k):
        for i in range(m):
            if i==0:
                a=j+i*k
            else:
                a=j+i*k+add[i-1]
            # print(a)
            T[s]=A[a]
            s+=1
    for j in range(m-1):
        for i in range(m-j-1):
            if i==0:
                a=k+j+i*k
            else:
                a=k+j+i*k+add[i-1]
            # print(a)
            T[s]=A[a]
            s+=1

    return None


# runtests(zdjecie, all_tests=False)
T=[(48, 26), (82, 42), (24, 65), (28, 17), (14, 62), (72, 74), (26, 55), (88, 7), (2, 41), (8, 45), (68, 36), (50, 14), (64, 79), (38, 33), (54, 48)]
T=[(458, 460), (826, 476), (340, 869), (1078, 860), (598, 828), (684, 488), (754, 497), (440, 52), (994, 928), (528, 1004), (92, 397), (1042, 548), (120, 237), (740, 113), (792, 209), (26, 84), (654, 337), (312, 17), (314, 809), (710, 69), (672, 173), (936, 784), (226, 749), (1010, 236), (300, 945), (382, 764), (954, 785), (878, 356), (884, 716), (772, 516), (836, 969), (8, 53), (694, 533), (512, 748), (268, 1017), (102, 153), (564, 89), (1020, 317), (326, 584), (1038, 792), (366, 444), (720, 116), (168, 653), (238, 373), (924, 257), (208, 45), (980, 220), (778, 172), (10, 96), (380, 872), (368, 849), (408, 229), (774, 461), (1116, 129), (44, 693), (758, 136), (166, 532), (194, 189), (496, 300), (764, 240), (618, 848), (1060, 388), (644, 737), (282, 400), (444, 789), (176, 457), (94, 636), (554, 668), (476, 769), (962, 204), (140, 589), (88, 736), (580, 413), (992, 293), (1016, 889), (256, 276), (350, 521), (922, 952), (632, 705), (206, 180), (1044, 892), (348, 429), (402, 677), (542, 324), (224, 985), (154, 788), (502, 873), (858, 841), (856, 876), (914, 36), (430, 909), (1104, 152), (900, 477), (70, 565), (54, 617), (814, 665), (658, 684), (498, 972), (286, 600), (428, 428), (796, 137), (1086, 704), (462, 660), (438, 68), (28, 725)]
zdjecie(T,3,4)
print(T)
print(sorted(T,key=lambda x: x[1],reverse=True))