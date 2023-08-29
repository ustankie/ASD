from zad7testy import runtests


def maze(L):
    # 0-ostatni w dół,1-góre,2-prawo
    n = len(L)
    F = [[[-1, -1, -1] for _ in range(n)]for _ in range(n)]
    F[0][0][0] = F[0][0][1] = F[0][0][2] = 0
    for i in range(1, n):
        if L[i][0] != "#" and F[i-1][0][0] >= 0:
            F[i][0][0] = F[i-1][0][0]+1

    for j in range(1, n):
        for i in range(n):
            if L[i][j] != "#":
                F[i][j][2] = max(F[i][j-1])
                if F[i][j][2] >= 0:
                    F[i][j][2] += 1
                if i > 0:
                    F[i][j][0] = max(F[i-1][j][0], F[i-1][j][2])
                    if F[i][j][0] >= 0:
                        F[i][j][0] += 1
            if i > 0 and i < n//2 and L[n-i][j] != "#":
                F[n-i][j][2] = max(F[n-i][j-1])
                if F[n-i][j][2] >= 0:
                    F[n-i][j][2] += 1
            if L[n-i-1][j] != "#" and i > 0:
                F[n-i-1][j][1] = max(F[n-i][j][1], F[n-i][j][2])
                if F[n-i-1][j][1] >= 0:
                    F[n-i-1][j][1] += 1

    if len(L) == 4:
        print(*F, sep="\n")

    return max(F[n-1][n-1])


# runtests(maze, all_tests=True)
L = [
    '....#...##',
    '...#....##',
    '#.........',
    '.......#..',
    '.......##.',
    '...#....#.',
    '#....#....',
    '##.....#.#',
    '..........',
    '......#...'
]
L = [ '....','..#.','..#.','....']
# L = ['......',
#      '#..#..',
#      '.#..#.',
#      '##..#.',
#      '......',
#      '......']


print(maze(L))
