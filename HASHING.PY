class Hash:
    def __init__(self, size = 5):
        self.size = size
        self.hash_table = [[]for i in range(self.size)]

    def hashin(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self.hashin(key)
        for i in self.hash_table[hash_key]:
            if i[0] == key:
                i[1] = value
                return
        else:
            self.hash_table[hash_key].append([key, value])
    
    def get(self, key):
        hash_key = self.hashin(key)
        for i in self.hash_table[hash_key]:
           if i[0] == key:
                return i[1]
        else:
            return None
          
    def deletion(self, key):
        hash_key = self.hashin(key)
        for i, j in enumerate(self.hash_table[hash_key]):
            if j[0] == key:
                del self.hash_table[hash_key][i]
                return True
        else:
            return False
        
    def display(self):
        for i, j in enumerate(self.hash_table):
            print(i, j)

obj = Hash()
obj.insert("a", 1)
obj.insert("b", 2)
obj.insert("c", 3)
obj.insert("d", 4)
obj.insert("e", 5)
obj.insert("f", 6)

print(obj.get("a"))
print()
obj.display()
print()
print(obj.deletion("a"))
print()
obj.display()