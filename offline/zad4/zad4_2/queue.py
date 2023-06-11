class queue():
    def __init__(self,n=0):
        self.size=n
        self.q=[0 for _ in range(n)]
        self.p=0
        self.k=0
    def length(self):
        return self.k-self.p
    def put(self,el):
        self.q[self.k]=el
        self.k+=1
    def pop(self):
        a=self.q[self.p]
        self.p+=1
        return a
    def print(self):
        print(self.q[self.p:self.k])
Q=queue(5)
Q.put(4)
Q.put(8)
Q.print()
Q.pop()
Q.print()
print(Q.length())
