from kolutesty import runtests
from queue import PriorityQueue


def process(depends, disk,u,vis,d):
    for v in depends[u]:
        if not vis[v]:
            # vis[u]=True
            process(depends,disk,v,vis,d)

    if depends[u]:
        maxi=0
        ind=u
        for v in depends[u]:
            if d[v]>maxi or (disk[u]!=disk[v] and d[v]>=maxi):
                maxi=d[v]
                ind=v
        d[u]=d[ind]+(disk[ind]!=disk[u])
        vis[u]=True
                




def swaps( disk, depends):
    # tu prosze wpisac wlasna implementacje

    n = len(depends)
    vis=[False for _ in  range(n)]
    d=[0 for _ in range(n)]


    for u in range(n):
        if depends[u]==None:
            vis[u]=True

    for u in range(n):
        if not vis[u]:
            process(depends,disk,u,vis,d)
    return max(d)

def swap():
    return None


runtests( swaps, all_tests = True )
disks=['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A']
depends=[[1], [], [1, 4, 7], [1, 7], [1], [1, 2, 4], [2, 4, 5], [1], [1, 2], [3, 4]]
# disks=['A', 'A', 'B', 'B']
# depends=[[2, 3], [], [1, 3], [1]]
print(swaps(disks,depends))