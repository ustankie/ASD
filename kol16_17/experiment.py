from queue import PriorityQueue
from collections import deque

q=PriorityQueue([2,"aa"])
q.put([2,"a"])
q.put([1,"b"])
print(q.get())

d=deque([1,2,3,4,5])
print(d.popleft())
d[0]+=1
print(d[0])
