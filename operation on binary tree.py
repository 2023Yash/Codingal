class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                print(f"{data} inserted to the left of {self.data}")
            else:
                self.left.insert(data)
            
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                print(f"{data} inserted to the right of {self.data}")
            else:
                self.right.insert(data)
        else:
            print("data is already there")

    def display(self):
        if(self.left):
            self.left.display()
        print(self.data, end=" ")
        if(self.right):
            self.right.display()

    def search()

def delete(root):
    if(root):
        delete(root.left)
        root.left = None
        delete(root.right)
        root.right = None
        print(f"delete root.data {root.data}")
        root.data = None

obj = Node(10)
obj.insert(0)
obj.insert(1)
obj.insert(2)
obj.display()

delete(obj)
obj = None