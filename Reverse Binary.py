def reverse_binary(num):
    reversed_num = 0
    while num > 0:
        reversed_num = (reversed_num << 1) | num & 1
        num >>= 1
    return reversed_num

number = 13 
reversed_number = reverse_binary(number)
print(f"Reversed binary of {number} is {reversed_number}")
