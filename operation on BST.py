class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert (root, data):
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

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=", ")
        in_order(root.right)

obj = Node(50)
obj = insert(obj, 30)
obj = insert(obj, 20)
obj = insert(obj, 40)
obj = insert(obj, 70)
obj = insert(obj, 60)
obj = insert(obj, 80)

in_order(obj)

print()

class BSG:
    @staticmethod
    def main(args):
        k = BST()
        k.insert(10)
        k.insert(20)
        k.insert(50)
        k.insert(40)
        k.insert(30)

        k.in_order_for_BSG()

class Node_for_BSG:
    left = None
    right = None
    root = None
    def __init__(self, data):
        self.data = data

class BST:
    root = None

    def insert(self, data):
        var = Node_for_BSG(data)
        if self.root == None:
            self.root = var
            return var
        else:
            pre = None
            temp = self.root
            while temp != None:
                if temp.data > data:
                    pre = temp
                    temp = temp.left
                elif temp.data < data:
                    pre = temp
                    temp = temp.right
            if pre.data > data:
                pre.left = var
            else:
                pre.right = var

    def in_order_for_BSG(self):
        temp = self.root
        stack = []
        while temp != None or len(stack) != 0:
            if temp != None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(temp.data, end=", ")
                temp = temp.right

BSG.main([])
