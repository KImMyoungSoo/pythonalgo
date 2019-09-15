from collections import defaultdict
class Graph:
    def __init__(self):
        self.p_c_dict = defaultdict(list)

    def add(self, p_node, c_node):
        self.p_c_dict[p_node].append(c_node)
  
    def DFS(self, start):
        visited = []
        to_visit = [start]
        while to_visit:
            n = to_visit.pop()
            visited.append(n)
            for c in reversed(self.p_c_dict[n]): #???
                if c not in visited + to_visit:
                    to_visit.append(c)
        return visited
    
    def BFS(self, start):
        visited = []
        to_visit = [start]
        while to_visit:
            n = to_visit.pop(0)
            visited.append(n)
            for c in self.p_c_dict[n]:
                if c not in visited + to_visit:
                    to_visit.append(c)
        return visited
        
g = Graph()

#ex 1
g.add(1,2)
g.add(1,4)
g.add(1,8)
g.add(2,3)
g.add(4,5)
g.add(4,7)
g.add(5,6)
g.add(8,9)

print(g.DFS(1))
print(g.BFS(1))

#ex2
'''
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)

print(g.DFS(2))
print(g.BFS(2))
'''
#ex3
'''
g.add('A','B')
g.add('A','C')
g.add('B','D')
g.add('B','E')
g.add('C','E')
g.add('D','E')
g.add('D','F')
g.add('F','E')

print(g.DFS('A'))
print(g.BFS('A'))
'''
