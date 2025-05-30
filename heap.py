class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def leftchild(self, i):
        return 2 * i + 1
    
    def rightchild(self, i):
        return 2 * i + 2
    
    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
         while i > 0:
            parent = self.parent(i)
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_max(self):
        if not self.heap:
           return None
        if len(self.heap) == 1:
            return self.heap.pop()
        pos = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return pos
    
    def heapify_down(self, i):
        largest = i
        left = self.leftchild(i)
        right = self.rightchild(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)
    
    def display(self):
        print(self.heap)

    def peek(self):
        if self.heap is not None:
            return self.heap[0]
        
obj = Heap()
obj.insert(70)
obj.insert(20)
obj.insert(80)
obj.insert(30)
obj.display()
print(obj.peek(), obj.extract_max())