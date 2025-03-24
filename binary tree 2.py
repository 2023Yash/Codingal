class Node:
    def __init__(self, size):
        self.size = size
        self.tree = [None] * size
    def insert(self, position, value):
        if (position < self.size):
            self.tree[position] = value
        else:
            print("out of bounds")
    def display(self, index=0, indent=0):
        if(index < self.size and self.tree[index] != None):
            self.display(2 * index + 2, indent + 4)
            print(" " * indent, self.tree[index])
            self.display(2 * index + 1, indent + 4)

size = 10
obj = Node(10)
obj.insert(0, 1)
obj.insert(1, 2)
obj.insert(2, 3)
obj.display()