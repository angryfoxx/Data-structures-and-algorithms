class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.isEmpty())

stack.push("ankara")
print(stack.top())

stack.push("istanbul")
print(stack.top())

stack.push("izmir")
print(stack.top())

print(stack.size())

stack.pop()
print(stack.top())

stack.pop()
print(stack.top())

print(stack.isEmpty())

stack.pop()
print(stack.isEmpty())