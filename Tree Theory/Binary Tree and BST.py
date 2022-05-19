class Node():
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


n = Node(41)

n.right = Node(65)
n.right.left = Node(50)
n.right.right = Node(91)
n.right.right.left = Node(72)
n.right.right.right = Node(99)

n.left = Node(20)
n.left.left = Node(11)
n.left.right = Node(29)
n.left.right.right = Node(32)

path_list = []

class BST():
    def __init__(self):

        self.path_list = []

    def search(self, root, node):
        self.path_list.append(root.val)
        if root is None or root.val == node.val:
            return root
        else:
            if root.val < node.val:
                return self.search(root.right, node)
            else:
                return self.search(root.left, node)

    def insert(self, root, node):
        if root is None:
            self.root = node
        else:
            if root.val < node.val:
                if root.right is not None:
                    self.insert(root.right, node)
                else:
                    root.right = node
            else:
                if root.left is not None:
                    self.insert(root.left, node)
                else:
                    root.left = node

bst = BST()
bst.insert(n, Node(52))

print(bst.search(n, Node(52)), bst.path_list)