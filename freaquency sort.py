class data:
    def __init__(self, index, values, count=0):
        self.index = index
        self.values = values
        self.count = count

def freaquencies_to_dictionary(arr):
    if (len(arr) <= 2):
        return 
    
    dictionary = {}

    for i in range(len(arr)):
        dictionary.setdefault(arr[i], data(i, arr[i])).count += 1

    values = [*dictionary.values()]
    values.sort(key = lambda lb: (-lb.count, lb.index))

    zero = 0

    for i in values:
        for j in range(i.count):
            arr[zero] = i.values
            zero += 1

arr = [4, 2, 2, 5, 1, 5, 2, 3, 2, 4, 5, 2, 5, 4, 3, 5, 2, 4, 5, 2, 4, 2, 3, 4, 3, 1, 5, 4, 4, 2, 5, 2, 2, 5, 2, 1, 5, 2, 4, 3, 1, 5, 1, 1, 3, 5, 5, 5, 3, 1, 2, 4, 5, 3, 2, 1, 2, 2, 4, 3, 4, 4, 4, 3, 3, 4, 5, 2, 2, 1, 5, 3, 1, 1, 5, 4, 1, 2, 3, 2, 3, 5, 4, 5, 3, 5, 4, 3, 2, 4, 2, 4, 2, 4, 1, 1, 3, 5, 3, 4]

freaquencies_to_dictionary(arr)

print(arr)