def Reverse_Number(n):
    if (n > 0):
        last = n % 10
        if(n // 10 > 0):
            current_number = Reverse_Number(int(n // 10))
            return last * pow(10, len(str(current_number))) + current_number
        return n
        
print(Reverse_Number(1124))