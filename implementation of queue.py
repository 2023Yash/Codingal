from _collections import deque

class stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, item):
        self.q2.append(item)
        while(self.q1):
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if(self.q1):
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        else:
            return None
        
    def length(self):
        return len(self.q1)
    
stk = stack()
stk.push("1st")
stk.push("2nd")
stk.push("3rd")
stk.push("4th")
stk.push("5th")
print(stk.length())
print(stk.top())
stk.pop()
stk.pop()
print(stk.length())
print(stk.top())