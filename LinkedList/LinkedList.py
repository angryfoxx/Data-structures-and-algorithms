class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setNextnode(self, node):
        self.nextNode = node

    def getNextnode(self,):
        return self.nextNode

    def getNodevalue(self):
        return self.value

ankara = Node("06")
bolu = Node("14")
istanbul = Node("34")

ankara.setNextnode(istanbul)
print(ankara.getNextnode().getNodevalue())