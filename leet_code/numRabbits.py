def numRabbits(answers):
    n=len(answers)
    answers.sort()
    a=0
    i=1
    cnt=0
    while i<n:
        cnt=1
        while i<n and answers[i]==answers[i-1] and cnt<answers[i]+1:
            cnt+=1
            i+=1
            
        a+=(answers[i-1]+1)
        i+=1

    if i<=n:
        a+=(answers[i-1]+1)

    return a

T=[1,1,2]
T=[0,0,1,1,1]
print(numRabbits(T))