from binarytree import Node

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

print(tree)

def in_order_traversal(tree):
    if(tree):
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)

def pre_order_traversal(tree):
    if(tree):
        print(tree.value, end=" ")
        pre_order_traversal(tree.left)
        pre_order_traversal(tree.right)

def post_order_traversal(tree):
    if(tree):
        post_order_traversal(tree.left)
        post_order_traversal(tree.right)
        print(tree.value, end=" ")

in_order_traversal(tree)
print()
pre_order_traversal(tree)
print()
post_order_traversal(tree)
print()
