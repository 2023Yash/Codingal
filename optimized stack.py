import math
class twostack:
    def __init__(self, n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.array[self.top1] = x
        else:
            print("Overflow because of: ", x)

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.array[self.top2] = x
        else:
            print("Overflow because of: ", x)

    def popl(self):
        if self.top1>=0:
            x=self.array[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Underflow error")

    def pop2(self):
        if(self.top2 < self.size):
            x = self.array[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Underflow error")

stack = twostack(4)
stack.push1(242)
stack.push2(45)
stack.push1(3242242)
stack.push2(4554)
print(stack.pop2())
print(stack.pop2())
