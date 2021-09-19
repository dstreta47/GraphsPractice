#using recursion
from collections import defaultdict
class Graph:
    def __init__(self, n):
        self.n= n
        self.graph= defaultdict(list)

    def addedge(self, v1, v2):
        self.graph[v1].append(v2)
    def dfsutil(self, s, visited):
        visited.add(s)
        print(s)
        for i in self.graph[s]:
            if i not in visited:
                self.dfsutil(i, visited)
    def dfs(self, s):
        visited= set()
        self.dfsutil(s, visited)
        
g= Graph(6)
g.addedge(0,1)
g.addedge(0,3)
g.addedge(3,4)
g.addedge(3,5)
g.addedge(1,2)
print(g.graph)
g.dfs(0)
