class Employee():
    def __init__(self,fun):
        self.fun=fun
        self.emp=[]
        self.f=-1
        self.g=-1

def g(v):
    if v.g>=0:
        return v.g
    x=0
    for u in v.emp:
        x+=f(u)
    
    v.g=x
    return v.g

def f(v):
    if v.f>=0:
        return v.f
    x=v.fun
    for u in v.emp:
        x+=g(u)
    v.f=max(g(v),x)
    return v.f
def print_sol(p,pr):    
    if p.g<p.f and pr:
        print(p.fun,p.f,p.g) 
    if len(p.emp)>0:
        if p.g<p.f and pr:
            pr1=False
        else:
            pr1=True  
        for i in p.emp:
        
            print_sol(i,pr1) 
 
def party(p):
    g(p)
    f(p)

    print(max(p.g,p.f)),
    pr=p.g<p.f
    print_sol(p,pr)

t3=Employee(100)
t2=Employee(100)
t1=Employee(100)
s9=Employee(1)
s8=Employee(1)
s7=Employee(1)
s6=Employee(5)
s5=Employee(1)
s4=Employee(18)
s3=Employee(7)
s3.emp=[t1,t2,t3]
s2=Employee(36)
s1=Employee(25)
r7=Employee(2)
r7.emp=[s9]
r6=Employee(1)
r6.emp=[s7,s8]
r5=Employee(17)
r4=Employee(21)
r4.emp=[s4,s5,s6]
r3=Employee(23)
r2=Employee(5)
r1=Employee(18)
r1.emp=[s1,s2,s3]
q3=Employee(1)
q3.emp=[r6,r7]
q2=Employee(20)
q2.emp=[r4,r5]
q1=Employee(10)
q1.emp=[r1,r2,r3]
p=Employee(50)
p.emp=[q1,q2,q3]

    
party(p)