#ZADANIA:
#1) mergesort dla list jednokierunkowych
#a)pomysł - odcinamy serie naturalna, druga, scalamy, przyklejamy na koniec list; wartownik
#2)znajdowanie inwersji w tablicy (zliczanie)
#3)pojemniki z wodą - nie zachodzą na sb, połączone systemem rurek -> woda wypełnia równo do pewnego poziomu - ile pojemnikow w pelni zalanych?
class Node():
    def __init__(self, val,next=None):
        self.val=val
        self.next=next

def wypisz(p):
    p=p.next
    while p!=None:
        print(p.val)
        p=p.next

#odcina serie naturalna
def cut(p):
    q=p
    p=p.next
    if p==None:
        return None, None
    while p.next!=None and p.val<=p.next.val:
        p=p.next
    w=q.next
    q.next=p.next
    p.next=None
    return w,p

def merge(p1,p2):
    t=h=Node(None) #head,tail
    while p1 and p2:
        if p1.val<=p2.val:
            t.next=p1 #w pierwszej iteracji h.next = t.next
            p1=p1.next
        else:
            t.next=p2
            p1=p2.next
        t=t.next

    while p1:
        t.next=p1
        t=t.next
        p1=p1.next

    while p2:
        t.next=p2
        t=t.next
        p2=p2.next

    return h.next,t
def find_tail(p):
    q=p
    while p!=None:
        q=p
        p=p.next
    return q

def MergeSort(h):

    t=find_tail(h)

    while True:
        lh,lt=cut(h)
        rh,rt=cut(h)
        if rh==None:
            h.next=lh
            break
        if t=rt:
            t=h
        mh,mt=merge(lh,rh)
        t.next=mh
        t=mt

    


t=Node(0)
s=Node(9,t)
r=Node(123,s)
q=Node(34,r)
p=Node(12,q)

MergeSort(p)
wypisz(p)