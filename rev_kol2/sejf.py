from collections import deque

def sejf(pin,cur,buttons):
    n=len(buttons)

    d=[0 for _ in range(10000)]
    vis=[False for _ in range(10000)]
    par=[None for _ in range(10000)]

    d[cur]=0

    Q=deque()
    Q.append(cur)

    while len(Q)>0:
        u=Q.popleft()
        for v in buttons:
            h=(u+v)%10000
            if not vis[h]:           
                d[h]=d[u]+1
                vis[h]=True
                par[h]=u
                Q.append(h)
                if h==pin:
                    T=[]
                    p=pin
                    while p!=cur:
                        T.append((p-par[p])%10000)
                        p=par[p]
                    return T[::-1]
    return None

def test():
    from random import randint

    PIN = randint(0, 9999)  # Unlock PIN number
    NUM = randint(0, 9999)  # Currently displayed number

    buttons = tuple(randint(0, 9999) for _ in range(4))
    b = [str(button).zfill(4) for button in buttons]

    steps = sejf(PIN, NUM, buttons)
    print('PIN:', PIN)
    print(f'''
+--------------------+
|        {str(NUM).zfill(4)}        |
+--------------------+
|{b[0]}|{b[1]}||{b[2]}|{b[3]}|
+--------------------+
''')
    if not steps:
        print('Locked forever !!!')
    else:
        n = NUM
        for step in steps:
            n = (n + step) % 10_000
            print(f'Pressed: {step}  --->  Number: {n}')
        print(f'''
+--------------------+
|      UNLOCKED      |
+--------------------+
|{b[0]}|{b[1]}||{b[2]}|{b[3]}|
+--------------------+
''')


PIN = 3264 
NUM = 1703  

buttons = (6206,179,6044,9752)

print(sejf(PIN, NUM, buttons))
test()

