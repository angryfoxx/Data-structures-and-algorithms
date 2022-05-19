class Vertex():

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addneighbor(self, neighbor, weight = 0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):
        return f"{self.id} connected to :{[x.id for x in self.connectedTo]}"

class Graph():
    
    def __init__(self):
        self.vertlist = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertlist[key] = new_vertex
        return new_vertex

    def getVertex(self, n):
        if n in self.vertlist:
            return self.vertlist[n]
        return None

    def __contains__(self, item):
        return item in self.vertlist

    def addEdge(self, f, t, cost = 0):
         if f not in self.vertlist:
             nv = self.addVertex(f)
         if t not in self.vertlist:
             nv = self.addVertex(t)

         self.vertlist[f].addneighbor(self.vertlist[t], cost)

    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())



g = Graph()

for i in range(5):
    g.addVertex(i)

print(g.vertlist)

g.addEdge(1, 2, 0)
g.addEdge(3, 4, 0)
g.addEdge(4, 2, 0)
g.addEdge(1, 3, 0)

for v in g:
    print(v)
    print(v.getConnections())

print(g.__contains__(1))

print(g.getVertices())
print(g.getVertex(1))