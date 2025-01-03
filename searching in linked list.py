class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class slingly():
    def __init__(self):
        self.head = None

    def search(self, value):
        head = self.head

        while(head):
            if(head.data == value):
                return True
            else:
                head = head.next
            
        return False

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

print(slingly.search(20))