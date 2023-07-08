from kolutesty import runtests


def process(point, depends, disk, setted, changes):

    for neighbour in depends[point]:
        if not setted[neighbour]:
            process(neighbour, depends, disk, setted, changes)

    if depends[point]:
        # find max
        Max = 0
        Max_point = point
        for i in depends[point]:
            if changes[i]>Max or (changes[i]>=Max and disk[i]!=disk[point]):
                Max = changes[i]
                Max_point = i

        changes[point] = changes[Max_point] + (disk[Max_point] != disk[point])
        setted[point] = True


def swaps( disk, depends):
    # tu prosze wpisac wlasna implementacje

    n = len(disk)
    changes = [0 for _ in range(n)]
    setted = [False for _ in range(n)]

    for point in range(n):
        if depends[point] == None:
            setted[point] = True

    for point in range(n):
        if not setted[point]:
            process(point, depends, disk, setted, changes)

    return max(changes)
runtests( swaps, all_tests = True )