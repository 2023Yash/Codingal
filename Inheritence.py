class Maths:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def multiplication(n1, n2):
        print(n1 * n2)

class Other_Maths_Functions(Maths):
    pass

x = Maths(n1, n2)
n = Other_Maths_Functions(2, 4)
n.multiplication(4)