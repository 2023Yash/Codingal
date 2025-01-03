class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class slingly():
    def __init__(self):
        self.head = None

    def insetion_start(self, data):
        node = Node(data)
        if self.head is None:
            node.head = node
            return
        else:
            node.next = self.head
            self.head = node

    def index_insetion(self, data):
        node = Node(data)
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = node

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--> ", end="")
                temp = temp.next

slingly = slingly()
node = Node(10)
slingly.head = node

node2 = Node(20)
node.next = node2

print()

slingly.insetion_start(30)

slingly.index_insetion(30)

slingly.display()
