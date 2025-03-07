class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head == None:
            return "Stack is empty"
        
    def push(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            node_value = Node(data)
            node_value.next = self.head
            self.head = node_value

    def head_data(self):
        if not(self.is_empty()):
            return self.head.data

    def pop(self):
        if not(self.is_empty()):
            popped = self.head
            self.head = self.head.next
            popped.next = None
        
stack = Stack()
stack.push("a")
print(stack.head_data())
stack.push("b")
print(stack.head_data())
stack.pop()
print(stack.head_data(), "poped")
print(stack.head_data())
