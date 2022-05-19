class doublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

    def setNextnode(self, node):
        self.nextNode = node

    def setPrevnode(self, node):
        self.prevNode = node

    def getNextnode(self):
        return self.nextNode

    def getPrevnode(self):
        return self.prevNode

    def getNodevalue(self):
        return self.value


ankara = doublyLinkedListNode("06")
bolu = doublyLinkedListNode("14")
istanbul = doublyLinkedListNode("34")



ankara.setNextnode(bolu)

bolu.setPrevnode(ankara)

print(bolu.getPrevnode().getNodevalue())
print(ankara.getNextnode().getNodevalue())


bolu.setNextnode(istanbul)
print(istanbul.getPrevnode)

istanbul.setPrevnode(bolu)
print(istanbul.getPrevnode().getNodevalue())

print(istanbul.getPrevnode().getPrevnode().getNodevalue())