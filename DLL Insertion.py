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

    def insert_at_position(self, position, data):
        new_node = Node(data)
        current = self.head

        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        count = 0
        while current and count < position:
            current = current.next
            count += 1

        if current is None:
            print("The position is out of bounds!")
            return

        new_node.next = current
        new_node.prev = current.prev

        if current.prev:
            current.prev.next = new_node
        current.prev = new_node

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

print("Original list:")
dll.display()
dll.insert_at_position(1, 15)
print("\nList after inserting 15 at position 1:")
dll.display()
dll.insert_at_position(0, 5)
print("\nList after inserting 5 at position 0:")
dll.display()
