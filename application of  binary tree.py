class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

def Kproblems(root, k):
    if root is None:
        return
    elif k == 0:
        print(root.data, end=" ")
    else:
        Kproblems(root.left,k - 1)
        Kproblems(root.right,k - 1)

f = Node(1)
f.left = Node(2)
f.right = Node(3)
f.left.left = Node(4)
f.left.right = Node(5)

k = int(input("Enter a value:"))
Kproblems(f, k)

class Tree_Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def print_nodes_distance(root, k):
    if k == 0:
        print(root.val)
        return
    
    for child in root.children:
        print_nodes_distance(child, k - 1)

def tree_builder():
    root = Tree_Node(1)
    root2 = Tree_Node(2)
    root3 = Tree_Node(3)
    root4 = Tree_Node(4)
    root5 = Tree_Node(5)
    root6 = Tree_Node(6)
    root7 = Tree_Node(7)

    root.children = [root2, root3]
    root.children = [root4, root5]
    root.children = [root6]
    root.children = [root7]

    return root

root = tree_builder()
inp = int(input("Enter distance from k to root:"))
print(inp)
print_nodes_distance(root, inp)
