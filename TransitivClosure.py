from collections import defaultdict
class Graph:
    def __init__(self, n):
        self.n= n
        self.graph= defaultdict(list)
        self.tc= [[0 for j in range(self.n)] for i in range(self.n)]

    def addedge(self, v1, v2):
        self.graph[v1].append(v2)

    def dfsutil(self, s, v):
        self.tc[s][v]=1

        for i in self.graph[v]:
            if self.tc[s][i]==0:
                self.dfsutil(s,i)
    def trans_closure(self):
        for i in range(self.n):
            self.dfsutil(i,i)
        print(self.tc)    
g= Graph(4)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
g.trans_closure()
#print(g.graph)
