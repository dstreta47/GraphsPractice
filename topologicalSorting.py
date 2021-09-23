from collections import defaultdict

class Graph:
  def __init__(self,no):
    self.no = no
    self.graph = defaultdict(list)
   def add_edge(self,v1,v2):
    self.graph[v1].append(v2)
    
   def topological_util(self,s,visited,stack):
      visited[s] = True
      for i in self.graph[s]:
        if visted[i] == False:
          self.topological_util(i,visited,stack)
      stack.append(s)    
   
   def topologicalSort(self):
    visited = [False]*self.no
    stack = []
    
    for i in range(self.no):
      if visited[i] == False:
        topological_util(i,visited,stack)
        
    print(stack[::-1]    
          
g = Graph(6)
g.add_edge(5,2)
g.add_edge(5,0)
g.add_edge(4,0)    
g.add_edge(4,3)
g.topologicalSort()          
