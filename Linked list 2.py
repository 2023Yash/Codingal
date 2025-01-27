class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class slingly():
    def __init__(self):
        self.head = None
        
    def swap(self, n1, n2):
        prev_node = None
        prev_node2 = None
        node = self.head
        node2 = self.head

        if(self.head == None):
            return
        
        if(n1 == n2):
            return
    
        while(node != None and node.data != n1):
            prev_node = node
            node = node.next

        while(node2 != None and node2.data != n2):
            prev_node = node2
            node2 = node2.next

        if(node != None and node2 != None):
            if(prev_node != None):
                prev_node.next = node2
            else:
                self.head = node2

            if(prev_node2 != None):
                prev_node2.next = node
            else:
                self.head = node

            temp = node.next
            node.next = node2.next
            node2.next = temp
        else:
            print("the swapping is not possible")

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

slingly.display()

print()

slingly.swap(20, 10)

slingly.display()
