class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end =" ")
        inorder(root.right)

def binary_search(root, key):
    if root is None:
        return None
    if root.data == key:
        return root
    if root.data > key:
        return binary_search(root.left, key)
    else:
        return binary_search(root.right, key)

obj = Node(50)
obj = insert(obj, 30)
obj = insert(obj, 70)
obj = insert(obj, 20)
obj = insert(obj, 40)
obj = insert(obj, 60)
obj = insert(obj, 80)

inorder(obj)

# 
print()
# 

r = binary_search(obj, 40)
if r:
    print("found")


def binary_search_2(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if root.data > key:
        return binary_search(root.left, key)
    else:
        return binary_search(root.right, key)
    
r = [8, 3, 10, 1, 6, 14]
root = None

for i in r:
    root = insert(root, i)

r = binary_search_2(root, 14)
if r:
    print("found")
