from queue import PriorityQueue


def towers(W0,W):
    n=len(W)
    my_sum=sum(W0)
    print(W)
    Q=PriorityQueue()
    all_sum=0
    for i in range(n):
        all_sum+=sum(W[i])
        print(i,": ",sum(W[i]))

    for i in range(n):
        Q_=PriorityQueue()
        maxi=max(W[i])
        for v in W[i]:
            Q_.put((maxi-v,v))
        a=sum(W[i])
        W[i]=(a,Q_)
        Q.put((all_sum-a,a,i,Q_))
    
    print(Q.queue)
    R=[]
    while my_sum<Q.queue[0][1]:
        a,sum_w,child,Q_=Q.get()
        b,brick=Q_.get()
        sum_w-=brick
        my_sum+=brick
        R.append((brick,child))
        Q.put((all_sum-sum_w,sum_w,child,Q_))
    
    print(Q.queue)
    while not Q.empty():
        a,sum_w,child,Q_=Q.get()
        print(child,": ",sum_w)
    return R,my_sum
        

    




W1 = [4] * 8
W2 = [10]
W3 = [10, 6]
W4 = [2.75] * 6
W5 = [4, 6, 2]
W = [W1, W2, W3, W4, W5]

W0 = [2.5, 3.5]

print(towers(W0,W))