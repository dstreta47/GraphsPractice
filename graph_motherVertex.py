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
    def dfsutil2(self, s, visited):
        visited[s]= True
        for i in self.graph[s]:
            if visited[i]==False:
                self.dfsutil2(i, visited)
    def dfs(self, s):
        visited= set()
        self.dfsutil(s, visited)

    def mother(self):
        visited= [False] * (self.n)
        v= 0
        for i in range(self.n):
            if visited[i] == False:
                self.dfsutil2(i, visited)
                v= i
        visited= [False]* (self.n)
        self.dfsutil2(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v



g= Graph(7)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(4,1)
g.addedge(6,4)
g.addedge(5,6)
g.addedge(5,2)
g.addedge(6,0)
#print(g.graph)
#g.dfs(0)
print(str(g.mother()))
