from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.n = n
        self.graph = defaultdict(list)
    def addedge(self,v1,v2):
        self.graph[v1].append(v2)
    def bfs(self,s):
        visited = [s]
        queue = [s]

        while queue:
            a = queue.pop(0)
            print(a)
            for i in self.graph[a]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
    def dfs(self, s):
        visited= [s]
        b= [s]

        while b:
            a= b.pop()
            print(a)
            for i in self.graph[a]:
                if i not in visited:
                    visited.append(i)
                    b.append(i)
g = Graph(6)
g.addedge(0,1)
g.addedge(0,3)
g.addedge(3,4)
g.addedge(3,5)
g.addedge(1,2)
print(g.graph)
g.bfs(0)
print("-------------------dfs below------------")
g.dfs(0)
