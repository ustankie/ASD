


def find(T,k):
    n=len(T)
    R=[0 for _ in range(n+1)]
    R[k]=1
    for j in range(n):
        R[T[j]]+=1
        if R[T[j]]>1:
            print(T[j])
            return

n=int(input())
# p=Node()
# q=p
# p.val=int(input())
# for i in range(n):
#     a=Node(int(input()))
#     p.next=a
#     p=a

# p.next=q

T = list(map(int, input().split(' ')))
print()
for i in range(1,n+1):
    find(T,i)