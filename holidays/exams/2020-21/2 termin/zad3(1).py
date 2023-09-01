from zad3testy import runtests

#part of the sequence of lightbulbs
class potsol:
    def __init__ (self,lb,rb,left_child,right_child):
        self.lights = [1,0,0]
        self.lb = lb
        self.rb = rb
        self.left_child = left_child
        self.right_child = right_child
        self.give_to_lc = 0
        self.give_to_rc = 0


def add_lights (A,B): return [A[0]+B[0],A[1]+B[1],A[2]+B[2]]


def create_an_interval_tree (lightbulbs,left_border,right_border):
    i = 0
    n = len(lightbulbs)
    while True:
        while i+1 < n:
            new_element = potsol (lightbulbs[i].lb,lightbulbs[i+1].rb,lightbulbs[i],lightbulbs[i+1])
            new_element.lights = add_lights (lightbulbs[i].lights,lightbulbs[i+1].lights)
            lightbulbs.append(new_element)
            i += 2
        if i < n:
            new_element = potsol (lightbulbs[i].lb,lightbulbs[i].rb,lightbulbs[i],None)
            new_element.lights = add_lights (lightbulbs[i].lights,[0,0,0])
            lightbulbs.append(new_element)
            i += 1
        if lightbulbs[-1].lb == left_border and lightbulbs[-1].rb == right_border: break
        n = len(lightbulbs)
    return lightbulbs[-1]


def switch_x_times (lights,x):
    green = lights[0]; red = lights[1]; blue = lights[2]
    for i in range(x%3):
        lights[0] = blue
        lights[1] = green
        lights[2] = red


def is_identical (A,B): return A[0] == B[0] and A[1] == B[1]


def find_intersection (X,Y):
    if X[0] <= Y[0] and X[1] >= Y[1]: return Y
    elif X[0] >= Y[0] and X[1] <= Y[1]: return X
    elif X[1] < Y[0] or X[0] > Y[1]: return None
    elif X[0] <= Y[0] and X[1] <= Y[1]: return (Y[0],X[1])
    elif X[0] >= Y[0] and X[1] >= Y[1]: return (X[0],Y[1])


def flip_the_switches (i,sought_interval,x):
    i.give_to_lc += x
    i.give_to_rc += x
    switch_x_times (i.lights,x)

    if is_identical ((i.lb,i.rb),sought_interval) == True:
        i.give_to_lc += 1; i.give_to_rc += 1
        switch_x_times (i.lights,1)
        #print(i.lights)
    else:
        b = [0,0,0]
        A = find_intersection ((i.left_child.lb,i.left_child.rb),sought_interval)
        if A != None:
            xa = i.give_to_lc; i.give_to_lc = 0
            flip_the_switches (i.left_child,A,xa)
        a = i.left_child.lights
        if i.right_child != None:
            B = find_intersection ((i.right_child.lb,i.right_child.rb),sought_interval)
            if B != None:
                xb = i.give_to_rc; i.give_to_rc = 0
                flip_the_switches (i.right_child,B,xb)
            b = i.right_child.lights
        i.lights = add_lights (a,b)
        #print(i.lb,i.rb,i.lights)


def lamps (n,T):
    lightbulbs = [potsol(i,i,None,None) for i in range (0,n)]
    if len(T) <= 25: print(T)

    root = create_an_interval_tree (lightbulbs,0,n-1)

    sought = 0
    for i in range (0,len(T)):
        flip_the_switches (root,T[i],0)
        sought = max (sought, root.lights[2])
        #print(root.lights,root.left_child.lights,root.right_child.lights)

    return sought


runtests (lamps)