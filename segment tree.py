class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.sum = 0
        self.l = l
        self.r = r

class SegmentTree:
    def __init__(self, nums):
        def build(l, r):
            node = Node(l, r)
            if l == r:
                node.sum = nums[1]
            else:
                mid = (l + r) // 2
                node.left = build(l, mid)
                node.right = build(mid + 1, r)
            return node
        self.root = build(0, len(nums) - 1)

    def query(self, l, r):
        def hi(node):
            if not node or node.l > r or node.r < l:
                return 0
            if node.l >= l and node.r <= r:
                return node.sum
            return hi(node.left) + hi(node.right)
        return hi(self.root)
    
    def update(self, i , val):
        def up(node):
            if node.l == node.r == i:
                node.sum = val
                return
            if i <= (node.l + node.r) // 2:
                up(node.left)
            else:
                up(node.right)    
            node.sum = node.left.sum = node.right.sum
        up(self.root)

arr = [1, 3, 5, 7, 9, 11]
obj = SegmentTree(arr)
print(obj.query(0, 5))
obj.update(0, 10)
print(obj.query(0, 5))