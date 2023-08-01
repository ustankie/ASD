def maxSatisfaction( S):
    S.sort()
    n=len(S)
    maxi=0
    begin=0
    #print(S)

    while begin<n:
        time=1
        i=begin
        curr=0
        while i<n:
            curr+=time*S[i]
            time+=1
            i+=1
        maxi=max(maxi,curr)
        begin+=1
    return maxi


satisfaction = [4,3,2]
print(maxSatisfaction(satisfaction))