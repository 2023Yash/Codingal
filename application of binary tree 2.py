class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traversal(root, k):
    if root == None:
        return
    
    if k == 0:
        print(root.data)
        return
    else:
        traversal(root.left, k - 1)
        traversal(root.right, k - 1)

f = Node(1)
f.left = Node(2)
f.right = Node(3)
f.left.left = Node(4)
f.left.right = Node(5)
traversal(f, 2)

def traversal_for_tilt(root, tilt):
    if not root:
        return 0
    else:
        left = traversal_for_tilt(root.left, tilt)
        right = traversal_for_tilt(root.right, tilt)
        tilt[0] += abs(left - right)
        return left + right + root.data

def tilt(root):
    tilt = [0]
    traversal_for_tilt(root, tilt)
    return tilt[0]

def largest_subtree(root):
    def helper(node):
        if not node:
            return(True, 0, float('inf'), float('-inf'))

        left_is_bst, left_size, left_min, left_max = helper(node.left)
        right_is_bst, right_size, right_min, right_max = helper(node.right)

        if left_is_bst and right_is_bst and left_max < node.data < right_min:
            size = 1 + left_size + right_size
            return (True, size, min((left_min, node.data)), max(right_max, node.data))
        else:
            return (False, max(left_size, right_size), 0, 0)
    
    return helper(root)[1]

f = Node(10)
f.left = Node(5)
f.right = Node(15)
f.left.left = Node(1)
f.left.right = Node(8)
f.right.right = Node(7)
print(tilt(f))
print(largest_subtree(f))