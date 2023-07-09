#1) problem stacji benzynowych - traktor jedzie z A do B, w baku dokładnie L litrów paliwa - ograniczenie na bak!
#   a) minimalna liczba tankowań - bierzemy ostatnia napotkana stacje i na niej tankujemy
#   b)minimalizujemy koszt tankowań - jeśli w zasięgu lepsza stacja, to tankujemy tyle, ile trzeba, by do niej dojechać, wpp do pełna
#   c)j.w.,ale tankujemy zawsze do pełna - dynamik, a nie zachłanny f(x,i)-koszt jazdy z 0 do i mając x paliwa
#2)v przedziały jednostkowe - sortujemy pkty rosnąco zaczynamy na pierwszym do pokrycia punkcie jednostkowym, kolejny zaczynamy od pierwszego poza przedziałem
#3)v zadania z terminami - zadanie,termin,zysk, każde zadanie zajmuje jednostkę czasu - chcemy znaleźć podzbiór zadań, które można wykonać w terminie i max zysk
#   - bierzemy zadania o największym zysku idąc od najpóźniejszych deadlinów z tych które można jeszcze oddać
#4) jak najmniej monet wydać w reszcie - dynamik: f(N,coins)=min(N-c,coins)+1,c należy do listy nominałów
#                                                 f(0,_)=0
#   czasem można zachłannie -> np w pl systemie monetarnym -> nominały muszą rosnąć szybciej niż wykładniczo - kolejny jest co najmniej 2 razy większy
#5)vładowanie przyczepy - posortować i dodawać od największych

#1) a)
def tank(L,S):
    n=len(S)
    tankowania=0
    stations=[]
    pos=0
    while pos<n:
        i=pos+L
        while i>=pos and S[i]==None:
            i-=1
        tankowania+=1
        stations.append(pos)
        pos=i
#1) b) O(nllogl)
def tankb(L,S):
    pos=0
    n=len(S)
    cheapest=0
    paliwo=0
    koszt=0
    while pos<n:
        cheapest=sorted(list([x for x in enumerate(S)[pos:pos+L] if x[1]!=None]),key=lambda x:x[1])[0]
        if cheapest[0]==pos:
            brakuje=min(L-paliwo,n-pos-paliwo)
            koszt+=brakuje*cheapest[1]
            paliwo+=brakuje
            pos=min(pos+L,n-1)
        else:
            brakuje=max((cheapest[0]-pos)-paliwo,0)
            paliwo+=brakuje
            koszt+=brakuje*S[pos]
            pos+=(cheapest[0]-pos)
def jedn(T):
    n=len(T)
    T.sort(reversed=True)
    licznik=0
    while T:
        start=T[-1]
        while start<=T[-1]<=start+1:
            T.pop()
        licznik+=1
    return licznik

        


