class Btree:
    def __init__(self, tree, leaf = False):
        self.leaf = leaf
        self.tree = tree
        self.children = []
        self.keys = []

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")

        if not self.leaf:
            self.children[len(self.keys)].traverse()

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and k == self.keys[i]:
            return self
        if self.leaf:
            return None
        return self.children[i].search(k)

class Btree1:
    def __init__(self, i):
        self.root = None
        self.i = i 

    def traverse(self):
        if self.root is None:
            pass
        else:
            self.root.traverse()

    def search(self, k):
        if self.root is None:
            return None
        else:
            return self.root.search(k)
        
obj = Btree1(3)
obj.root = Btree([3, False])
obj.root.keys = [5, 20]
obj.root.children = [Btree(3, True), Btree(3, True), Btree(3, True)]
obj.root.children[0].keys = [3, 4]
obj.root.children[1].keys = [2, 6]
obj.root.children[2].keys = [1, 9]
obj.traverse()

sear = obj.search(84)
if sear:
    print("Value found")
else:
    print("Value not found")