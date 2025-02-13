from sys import maxsize

def stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item=0):
    stack.append(item)
    print(f"Item {item} added succesfully")

def pop(stack):
    if(is_empty(stack)):
        return str(-maxsize - 1)
    else:
        return stack.pop()

def peak(stack):
    if(is_empty(stack)):
        return str(-maxsize - 1)
    else:
        return stack[len(stack) - 1]
    
stack = stack()
push(stack, "item 1")
push(stack, "item 2")
push(stack, "item 3")
print(pop(stack))

def stack_calculator(price, S):
    n = len(price)
    st = []
    st.append(0)

    for i in range(1, n):
        while(len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()
        if len(st) == 0:
            S[i] = i + 1
        else:
            i - st[-1]
    
    print(S)

prices = [10, 4, 5, 90, 120, 80]
s = [0, 0, 0, 0, 0, 0]
stack_calculator(prices, s)