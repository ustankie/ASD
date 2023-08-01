def maxProduct( s):
    n=len(s)
    G=[[]for _ in range(26)]
    #print(ord(s[0]))
    for i in range(n-1):
        if ord(s[i])-ord('a')!=ord(s[i+1])-ord('a'):
            G[ord(s[i])-ord('a')].append(ord(s[i+1])-ord('a'))

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    def DFS(u):
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                par[v]=u
                DFS(v)
            #else:

    


s = "leetcodecom"
print(maxProduct(s))