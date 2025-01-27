class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()
