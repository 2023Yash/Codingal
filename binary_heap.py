class Heap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def get(self, i):
        return self.items[i]
    
    def getmax(self):
        if self.size() == 0:
            return None
        return self.items[0]
    
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.getmax()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest
    
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l <= self.size() - 1 and self.get(l) > self.get(i):
            largest = l
        if r <= self.size() - 1 and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j],  self.items[i]

    def insert(self, key):
        index = self.size()
        self.items.append(key)
        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p

bheap = Heap()
print("Insert Data")
print("Get Max")
print("Max Extract")
print("Quit")
while True:
    do = input("Write Task:").split()
    operation = do[0].strip().lower()
    if operation == "insert":
        bheap.insert(int(do[1]))
    elif operation == "max":
        if bheap.size() == 0:
            print("heap is empty")
        else:
            print(bheap.getmax())
    elif operation == "extract":
        if bheap.size() == 0:
            print("heap is empty")
        else:
            print(bheap.extract_max())
    elif operation == "quit":
        break        