class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class slingly():
    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--> ", end="")
                temp = temp.next

    def reverse(self):
        if self.head is None:
            print("List is empty, nothing to reverse.")
            return

        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev 

sll = slingly()

sll.head = Node(1)
sll.head.next = Node(2)
sll.head.next.next = Node(3)
sll.head.next.next.next = Node(4)


sll.reverse()

sll.display()