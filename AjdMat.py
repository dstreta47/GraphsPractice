#Graph Representation - Adjacency Matrix

class Graph:
    def __init__(self,V_no):
        self.adjMat = [[-1]*V_no for x in range(V_no)]
        self.V_no = V_no
        self.vertices = {}
        self.verticeslist = [0]*V_no

    def set_vertex(self,vtx,id):
        if 0<=vtx <= self.V_no:
            self.vertices[id] = vtx
            self.verticeslist[vtx] =id

    def set_edge(self,v1,v2,cost=0):
        v1 = self.vertices[v1]
        v2 = self.vertices[v2]
        self.adjMat[v1][v2]=cost
        self.adjMat[v2][v2]=cost   

    def get_vertex(self):
        return self.verticeslist     

    def get_edges(self):
        edges=[]
        for i in range(self.V_no):  
            for j in range(self.V_no):
                if(self.adjMat[i][j]!=-1):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMat[i][j]))
        return edges    

    def get_matrix(self):
        return self.adjMat            


g = Graph(6)
g.set_vertex(0,'a')
g.set_vertex(1,'b')
g.set_vertex(2,'c')
g.set_vertex(3,'d')
g.set_vertex(4,'e')
g.set_vertex(5,'f')
g.set_edge('a','e',10)
g.set_edge('a','c',20)
g.set_edge('c','b',30)
g.set_edge('b','e',40)
g.set_edge('e','d',50)
g.set_edge('f','e',60)


# print(g.adjMat)
# print(g.V_no)
# print(g.vertices)
# print(g.verticeslist)
print("vertics of graph")
print(g.get_vertex())
print("edge of the graph")
print(g.get_edges())
print("matrix")
print(g.get_matrix())

