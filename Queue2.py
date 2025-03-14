ar = [0 for _ in range(10)]
n = 10

front = -1
rear = -1

def enqueue(item):
    global n
    global rear
    global front
    if(rear == n - 1):
        print("Overflow")
        return
    else:
        if(front == -1 and rear == -1):
            front = rear = 0
        else:
            rear += 1

        ar[rear] = item
        print("element inserted")
        
def dequeue():
    global n
    global rear
    global front

    if front == -1 or front > rear:
        print("Underflow")
        return
    else:
        item = ar[front]

        print(f"Element deleted = {item}")
        if(rear == front):
            rear = -1
            front = -1
        else:
            front += 1
        
        front += 1

def display():
    global n
    global rear
    global front

    if front == -1:
        print("Queue is empty")
        return
    else:
        i = front
        while i <= rear:
            print(ar[i], end=" ")
            i += 1

def front_func():
    global n
    global rear
    global front

    if front == -1:
        print("Queue is empty")
        return
    else:
        print(f"Front element is {ar[front]}")

ch = None

print("1: Insertion")
print("2: Deletion")
print("3: Display All")
print("4: Display Front")
condition = True
while condition:
    ch = int(input("Enter funtion's number:"))
    if ch == 1:
        inp = input("Enter Element:")
        enqueue(inp)
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        front_func()
    else:
        print("invalid input")