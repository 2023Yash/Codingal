class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def knapsack(w, List):
    List.sort(key = lambda x:(x.profit / x.weight), reverse = True)
    Final = 0.0

    for item in List:
        if item.weight <= w:
            w -= item.weight
            Final += item.profit
        else:
            Final += item.profit * w / item.weight
            break
    return Final
    

w = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
val = knapsack(w, arr)
print(val)