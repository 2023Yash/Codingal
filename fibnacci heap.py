class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        node = FibonacciNode(key)
        self._merge_with_root_list(node)
        if self.min_node is None or node.key < self.min_node.key:
            self.min_node = node
        self.total_nodes += 1

    def _merge_with_root_list(self, node):
        if self.min_node is None:
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node

    def display(self):
        if not self.min_node:
            return

        current = self.min_node
        first = True
        while True:
            print(current.key, end=" ")
            current = current.right
            if current == self.min_node and not first:
                break
            first = False

heap = FibonacciHeap()
heap.insert(10)
heap.insert(2)
heap.insert(15)
heap.insert(6)
heap.insert(8)

heap.display()
