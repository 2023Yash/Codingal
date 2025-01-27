class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None

    def searching(self, data):
        t = 0
        temp = self.head
        count = 0
        while temp:
            if(temp.data == data):
                t = 1
                break
            temp = temp.next
            count += 1
        if(t == 1):
            print(f"found at {count}")
        else:
            print("not found")

    def display(self):
        if(self.head == None):
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
                temp = temp.next

linked_list = linked_list()
ten = Node(10)
linked_list.head = ten
twenty = Node(20)
ten.next = twenty
thirty = Node(30)
thirty.prev = twenty
twenty.next = thirty
linked_list.display()
linked_list.searching(20)