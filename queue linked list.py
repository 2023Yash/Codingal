class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None
    
    def enqueue(self, item):
        Temp = Node(item)
        if self.rear == None:
            self.front = self.rear = Temp
            return
        else:
            self.rear.next = Temp
            self.rear = Temp

    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.dequeue()
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(234)
    q.enqueue(21)
    q.dequeue()
    print(q.front.data)
    print(q.rear.data)