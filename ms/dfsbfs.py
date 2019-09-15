# DFS, BFS python Study

#DFS
def dfs (graph, head) :
    visit = []
    stack = []

    stack.append(head)

    while stack :
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            stack.extend(graph[node])
    
    return visit

#BFS
def bfs (graph, head) :
    visit = []
    queue = []

    queue.append(head)
    
    while queue :
        node = queue.pop(0)
        if node not in visit :
            visit.append(node)
            queue.extend(graph[node])
    
    return visit

#main
if __name__ == "__main__":
    graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
    }

    print('DFS : ')
    print(dfs(graph,'A'))
    print('BFS : ')
    print(bfs(graph,'A'))