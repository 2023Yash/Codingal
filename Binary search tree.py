class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def new_node(key):
    temp = Node(key)
    temp.val = key

    temp.left = None
    temp.right = None
    return temp

def insert(node, key):
    if(node is None):
        return new_node(key)
    if(key < node.data):
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

node = Node(50)
insert(node, 30)
insert(node, 20)
insert(node, 40)
insert(node, 70)
insert(node, 60)
insert(node, 80)

preorder(node)
print("\n")
def bst(pre, index = [0], bound = float("inf")):
    if index[0] == len(pre) or pre[index[0]] > bound:
        return None
    root = Node(pre[index[0]])
    index[0] += 1
    root.left = bst(pre, index, root.data)
    root.right = bst(pre, index, bound)
    return root

arr = [50, 30, 20, 40, 70, 60, 80]
BST = bst(arr)
preorder(BST)