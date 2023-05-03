adjacency_list = {
    'A': [('B', 2), ('C', 1), ('D', 3)],
    'B': [('E',3),('F',2)],
    'C': [('F',4)],
    'D':[('G',2),('H',1)],
    'E':[('F',1)],
    'F':[('I',3)],
    'G':[('H',1),('I',2)],
    'H':[('I',4)]
}

def h(n):
    H = {
        'A':0,
        'B':6,
        'C':5,
        'D':4,
        'E':7,
        'F':8,
        'G':5,
        'H':4,
        'I':0
    }
    return H[n]

def get_neighbour(v):
    return adjacency_list[v]   

def a_star(start_node, end_node):
    open_list = []
    closed_list = []
    open_list.append(start_node)
    g = {}
    g[start_node] = 0
    parent = {}
    parent[start_node] = start_node
    
    while len(open_list) > 0:
        min = 9999
        for i in open_list:
            if g[i] + h(i) < min:
                n = i
                min = g[i] + h(i)
        
        if n == end_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            
            return path

        for (neighbour, cost) in get_neighbour(n):
            if neighbour not in open_list and neighbour not in closed_list:
                open_list.append(neighbour)
                parent[neighbour] = n
                g[neighbour] = g[n] + cost
            else:
                if g[neighbour] > g[n] + cost:
                    g[neighbour] = g[n] + cost
                    parent[neighbour] = n
        open_list.remove(n)
        closed_list.append(n)
    
print(a_star('A', 'I'))