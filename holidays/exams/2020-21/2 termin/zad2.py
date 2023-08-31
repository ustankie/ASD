from zad2testy import runtests

class Node:
  def __init__( self ):   # stwórz węzeł drzewa
    self.edges   = []     # lista węzłów do których są krawędzie
    self.weights = []     # lista wag krawędzi
    self.ids     = []     # lista identyfikatorów krawędzi
      
  def addEdge( self, x, w, id ): # dodaj krawędź z tego węzła do węzła x
    self.edges.append( x )       # o wadze w i identyfikatorze id
    self.weights.append( w ) 
    self.ids.append( id )

def balance( T ):
    p=T

    def DFS2(u):
        count=0
        for v in range(len(u.edges)):
            count+=DFS2(u.edges[v])+u.weights[v]
        u.w_sum=count
        return count
    DFS2(p)

    all_sum=p.w_sum
    best_edge=0
    smallest_diff=float('inf')

    def DFS3(u):
        nonlocal smallest_diff,best_edge

        for v in range(len(u.edges)):
            part1=u.edges[v].w_sum
            part2=all_sum-part1-u.weights[v]
            diff=abs(part1-part2)
            if smallest_diff>diff:
                smallest_diff=diff
                best_edge=u.ids[v]
            DFS3(u.edges[v])
    DFS3(p)
    return best_edge
    
       
runtests( balance )

A=Node()
B=Node()
C=Node()
D=Node()
E=Node()

A.addEdge(B,6,1)
A.addEdge(C,10,2)
B.addEdge(D,5,3)
B.addEdge(E,4,4)


   
print(balance(A))