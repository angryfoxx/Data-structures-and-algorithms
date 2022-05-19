class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def addNeighbor(self, value, weight = 0):
        self.connections[value] = weight

    def __str__(self):
        return f"{self.key} connected to : {[x.key for x in self.connections]}"

    def getConnections(self):
        return self.connections.keys()

    def getId(self):
        return self.key

    def getWeight(self, value):
        return self.connections[value]


class Graph:
    def __init__(self):
        self.vertlist = {}
        self.numofvertices = 1

    def addVertex(self, value):
        self.numofvertices += 1
        newVertex = Vertex(value)
        self.vertlist[value] = newVertex
        return newVertex

    def getVertex(self, value):
         if value in self.vertlist:
             return self.vertlist[value]
         else:
             return None

    def __contains__(self, item):
        return item in self.vertlist

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertlist:
            nv = self.addVertex(f)
        if t not in self.vertlist:
            nv = self.addVertex(t)

        self.vertlist[f].addNeighbor(self.vertlist[t], cost)

    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

g = Graph()

for i in range(5):
    g.addVertex(i)

print(g.vertlist)
print("--")
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
