class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def recursion(root):
   if root is None:
       return 0
   return recursion(root.left) + recursion(root.right) + 1

def return_size(root):
    if root is None:
        return 0
    count = 0
    array = list()
    array.append(root)
    while array:
        temp = array.pop()
        count += 1
        if temp.left is not None:
            array.append(temp.left)
        if temp.right is not None:
            array.append(temp.right)
    return count

def sum_root(root):
    if root is None:
        return 0
    return sum_root(root.left) + sum_root(root.right) + root.data

root = Node(11)
root.left = Node(12)
root.right = Node(13)
root.left.left = Node(14)
root.left.right = Node(15)
print(return_size(root), recursion(root), sum_root(root))