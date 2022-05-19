class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):

        newNode = Node(value)

        newNode.next = self.head

        self.head = newNode

    def insertAfter(self, prevNode, value):
        if prevNode is None:
            return "böyle bir node yok"

        newNode = Node(value)

        newNode.next = prevNode.next

        prevNode.next = newNode

    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    def printLinkList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def delete(self, value):
        temp = self.head

        if temp is not None:
            if temp.value == value:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.value == value:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None


"""linked_list = LinkedList()
linked_list.push("tail")
linked_list.push(15)
linked_list.push(25)
linked_list.push("head")
linked_list.printLinkList()
print("--")
linked_list.insertAfter(linked_list.head,100)
linked_list.printLinkList()
print("--")
linked_list.insertAfter(linked_list.head.next.next,"insert")
linked_list.printLinkList()
print("--")
linked_list.append("sona eklenen eleman")
linked_list.append("en sona node ekle")
linked_list.printLinkList()"""

linked_list = LinkedList()
linked_list.push("ankara")
linked_list.push("bolu")
linked_list.push("istanbul")
linked_list.printLinkList()
print("--")
linked_list.delete("bolu")
linked_list.printLinkList()