class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linked_list():
    def __init__(self):
        self.head = None

    def insertion(self, value):
        node_var = Node(value)

        node_var.next = self.head

        self.head = node_var

    def insertion_at_last(self, value):
        node_var = Node(value)
        temp = self.head

        while(temp.next):
            temp = temp.next

        temp.next = node_var
        node_var.prev = temp

    def display(self):
        print()
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--> ", end="")
                temp = temp.next

linked_list = linked_list()
node = Node(10)

linked_list.head = node
node2 = Node(69)

node.next = node2
node2.prev = node

node3 = Node(96)

node2.next = node3

linked_list.display()

linked_list.insertion(0)

linked_list.insertion_at_last(100)

linked_list.display()