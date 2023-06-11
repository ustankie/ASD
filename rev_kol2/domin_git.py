from collections import deque


def directed_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [deque() for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
    return G


def transpose_graph(G: 'directed graph represented using adjacency lists'):
    n = len(G)
    # Store indices of the beginnings of new neighbours added to each vertex
    new_indices = [len(G[u]) for u in range(n)]
    
    # For each vertex remove its all old neighbours (vertices stored before the
    # first new added vertex) and for each of these removed neighbours append 
    # the current vertex to their new neighbours (this will be a reversed edge)
    for u in range(n):
        for _ in range(new_indices[u]):
            v = G[u].popleft()
            G[v].append(u)
        new_indices[u] = 0


def get_process_times(G: 'directed graph represented using adjacency lists'):
    n = len(G)
    times = [0] * n
    visited = [False] * n
    time = 0
    
    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal time
        time += 1
        times[u] = time
        
    for u in range(n):
        if not visited[u]:
            dfs(u)
            
    return times


def get_vertices_order(times):
    n = len(times)
    order = [-1] * n
    for i in range(n):
        order[n - times[i]] = i
    return order


def find_coherent_components(G: 'directed graph represented using adjacency lists'):
    n = len(G)
    # Get processing time of each vertex
    times = get_process_times(G)
    # Transpose a graph (reverse all the edges)
    transpose_graph(G)
    # Get order of vertices in which DFS will be started from such vertices
    order = get_vertices_order(times)
    # Create an array in which a result will be stored (each number will refer
    # to the other coherent component of a graph)
    result = [-1] * n  # This array will also be used to check if a vertex was visited
    num = 0
    
    def dfs(u):
        result[u] = num
        for v in G[u]:
            if result[v] < 0:
                dfs(v)
        
    # Start dfs from vertices of the highest processing time
    for i in range(n):
        u = order[i]
        if result[u] < 0:
            dfs(u)
            num += 1
            
    # Don't transpose it again as we should normally do, because after transforming
    # to coherent components graph we will get the result faster when no transposition
    # is made
            
    return result, num


def map_to_coherent_components_graph(G: 'directed graph represented using adjacency lists',
                                     comp: 'array of components indices which vertices belong to',
                                     m: 'number of unique coherent components'):
    # This array will hold indices of components representatives which will
    # become new indices of a graph (all the vertices from the same coherent
    # component will be merged with this one)
    represent = [None] * m 
    n = len(G)
    
    for u in range(n):
        # If there is no representative of the current coherent component, store the current
        # vertex as its representative
        if represent[comp[u]] is None:
            represent[comp[u]] = u
        # Remove all the edges of the current vertex which connect it with all other
        # vertices in the coherent component
        for _ in range(len(G[u])):
            v = G[u].popleft()
            if comp[v] != comp[u]:
                G[represent[comp[u]]].append(comp[v])
    
    # Remove empty vertices and fix mapped vertices to these of coherent components
    mapped = [None] * m
    for i in range(m):
        mapped[i] = G[represent[i]]
    for i in range(m):
        G[i] = mapped[i]
        
    # Pop all the empty entries remaining
    for _ in range(n - m):
        G.pop()
        
    return represent

        
def get_dominoes_to_knock(E: 'array of dominoes pairs'):
    # Get a number of domino pieces
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    # Create a DAG based on domino pieces
    G = directed_graph_list(E, n)
    # Map a graph to the graph of coherent components (which is transposed)
    components, count = find_coherent_components(G)
    represent = map_to_coherent_components_graph(G, components, count)
    # Find vertices with no outgoing edges (as a graph is transposed, now our
    # problem changed to a problem of finding vertices with no outgoing edges
    # which is much easier as we can immediately check a number of outgoing
    # edges of each vertex)
    n2 = len(G)
    result = []
    for u in range(n2):
        # If has no outgoing edges
        if not G[u]:
            result.append(represent[u])  # Append the original domino index
    return result

E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)]
print(get_dominoes_to_knock(E))