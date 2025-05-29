class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def insertion(root, key):
    if root is None:
        return Node(key)
    elif root.data < key:
        root.right = insertion(root.right, key)
    else:
        root.left = insertion(root.left, key)
    return root

def minvalue(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def deletion(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = deletion(root.left, key)
    elif key > root.data:
        root.right = deletion(root.right, key)
    else:
        if root.left is None:
            temporary = root.right
            root = None
            return temporary
        elif root.right is None:
            temporary = root.left
            root = None
            return temporary
        temporary = minvalue(root.right)
        root.data = temporary.data
        root.right = deletion(root.right, temporary.data)

    return root

root = None
root = insertion(root, 50)
root = insertion(root, 30)
root = insertion(root, 20)
root = insertion(root, 60)
root = insertion(root, 70)
root = insertion(root, 80)
inorder(root)
print()
root = deletion(root, 20)
inorder(root)
print()
