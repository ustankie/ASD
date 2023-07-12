# Dane są lampki o numerach od 0 do n-1. Każda z nich może świecić na zielono, czerwono lub niebiesko
# i ma jeden przełącznik, który zmienia jej kolor (z zielonego na czerwony, z czerwonego na niebieski
# i z niebieskiego na zielony). Początkowo wszystkie lampki świecą na zielono. Operacja (a, b) oznacza
# "wciśnięcie przełącznika na każdej z lampek o numerach od a do b". Wykonanych będzie m operacji.
# Proszę napisać funkcję:
# def lamps(n, L):
#     ...
# która mając daną liczbę n lampek oraz listę L operacji (wykonywanych w podanej kolejności) zwraca
# ile maksymalnie lampek świeciło się na niebiesko (lampki są liczone na początku i po wykonaniu
# każdej operacji).
from Exercise_3_tests import runtests


def lamps(n, L):
    m = len(L)
    # if m==20 and n==20:
    #     print(L)
    GREEN = 0
    RED = 1
    BLUE = 2
    F = [0 for _ in range(n)]

    curr_blue = 0
    max_blue = 0
    for i in range(m):
        for j in range(L[i][0], L[i][1]+1):
            if F[j] == BLUE:
                curr_blue -= 1
            F[j] = (F[j]+1) % 3
            if F[j] == BLUE:
                curr_blue += 1

        max_blue = max(max_blue, curr_blue)

    return max_blue


runtests(lamps)
L = [(11, 13), (4, 4), (2, 3), (5, 5),
     (14, 18), (9, 13), (7, 10), (9, 11), (7, 10),
     (9, 11), (14, 14), (5, 9), (16, 19), (6, 10),
     (16, 19), (14, 18), (16, 18), (4, 7), (8, 12), (2, 3)]
n = 20
print(lamps(n, L))
