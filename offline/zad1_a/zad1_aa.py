#Urszula Stankiewicz, nr albumu: 415668
#Program wykorzystuje symetrię palindromu. Iterując i od 0 do n, sprawdzamy długość promienia maksymalnego palindromu o środku w i.
#Następnie w każdym kroku 


from zad1testy import runtests

def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    def pal_count(s,mid): #zwraca promien najdluzszego z palindromow o srodku mid
        R=1
        n=len(s)
        while (R+mid)<n and R<=mid and s[mid+R]==s[mid-R]:
            R+=1
        return R-1
    
    n=len(s)
    max_r=0
    r=[-1 for _ in range(n)]
    r[0]=0
    r[n-1]=0
    #print(r[0])
    i=1
    while i<n:
        if r[i]==(-1):
            #print("i: ",i,"\n")
            r[i]=pal_count(s,i)
            max_r=max(max_r,r[i])
            j=1
            while j<=r[i]:
                #print(i-j)
                if r[i-j]>(r[i]-j):
                    r[i+j]=r[i]-j
                    max_r=max(max_r,r[i-j])
                elif r[i-j]<(r[i]-j):
                    r[i+j]=r[i-j]
                j+=1
            #print("\n")
        i+=1
    return max_r*2+1
    # Python program to implement Manacher's Algorithm
    # text=s
    # N = len(text)
    # if N == 0:
    #     return
    # N = 2*N+1    # Position count
    # L = [0] * N
    # L[0] = 0
    # L[1] = 1
    # C = 1     # centerPosition
    # R = 2     # centerRightPosition
    # i = 0    # currentRightPosition
    # iMirror = 0     # currentLeftPosition
    # maxLPSLength = 0
    # maxLPSCenterPosition = 0
    # start = -1
    # end = -1
    # diff = -1
    # for i in range(2,N):
    # # get currentLeftPosition iMirror for currentRightPosition i
    #     iMirror = 2*C-i
    #     L[i] = 0
    #     diff = R - i
    #     # If currentRightPosition i is within centerRightPosition R
    #     if diff > 0:
    #         L[i] = min(L[iMirror], diff)

    #     try:
    #         while ((i+L[i]) < N and (i-L[i]) > 0) and \
    #                 (((i+L[i]+1) % 2 == 0) or \
    #                 (text[(i+L[i]+1)//2] == text[(i-L[i]-1)//2])):
    #             L[i]+=1
    #     except Exception as e:
    #         pass
    #     if L[i] > maxLPSLength:        # Track maxLPSLength
    #         maxLPSLength = L[i]
    #         maxLPSCenterPosition = i

    # # If palindrome centered at currentRightPosition i
    # # expand beyond centerRightPosition R,
    # # adjust centerPosition C based on expanded palindrome.
    #     if i + L[i] > R:
    #         C = i
    #         R = i + L[i]

    # return maxLPSLength



        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True)
#print(ceasar("akontnoknonabcddcba"))