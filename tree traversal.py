from binarytree import build

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printinorder(root):
    if root:
        printinorder(root.left)

        print(root.val, end=" ")

        printinorder(root.right)

root = Node(1)
root.left = Node(43)
root.right = Node(435)
root.left.right = Node(234)
root.right.left = Node(34)
tree_list = [1, 43, 435,234, 35]
visual_tree  = build(tree_list)
print(visual_tree)
printinorder(root)
print()
print()
print()

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder(root):
    if root:
        print(root.val, end=" ")

        preorder(root.left)

        preorder(root.right)

root = Node(1)
root.left = Node(43)
root.right = Node(435)
root.left.right = Node(234)
root.right.left = Node(34)
tree_list = [1, 43, 435,234, 35]
visual_tree  = build(tree_list)
print(visual_tree)
preorder(root)
print()
print()
print()

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def postorder(root):
    if root:
        postorder(root.left)

        postorder(root.right)

        print(root.val, end=" ")

root = Node(1)
root.left = Node(43)
root.right = Node(435)
root.left.right = Node(234)
root.right.left = Node(34)
tree_list = [1, 43, 435,234, 35]
visual_tree  = build(tree_list)
print(visual_tree)
postorder(root)
print()
print()
print()