class GFG:
    class Node:
        deta = 0
        prev = None
        next = None

        @staticmethod
        def getnode(data):
            newNode = GFG.Node()
            newNode.data = data
            newNode.prev = None
            newNode.next = None
            return newNode
        
    class dequeue:
        front = None
        rear = None
        Size = 0

        def __init__(self):
            self.front = None
            self.rear = None
            self.Size = 0

        def is_empty(self):
            return self.front == None
        
        def Size(self):
            return self.Size

        def insertFront(self, data):
            newNode = GFG.Node.getnode(data)
            if(newNode == None):
                print("Overflow")
            else:
                if(self.front == None):
                    self.rear = self.front = newNode
                else:
                    newNode.next = self.front
                    self.front.prev = newNode
                    self.front = newNode

                self.size += 1

        def insertRear(self, data):
            newNode == GFG.Node.getnode(data)

            if(newNode == None):
                print("Overflow")
            else:
                if (self.rear == None):
                    self.rear = self.front = newNode
                else:
                    newnode.prev = self.rear
                    self.rear.next = newNode
                    self.rear = newNode
                self.size += 1
                