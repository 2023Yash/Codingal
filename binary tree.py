from binarytree import Node

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(tree)