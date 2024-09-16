def longest_consecutive_ones(number):
    binary_rep = bin(number)[2:]
    max_length = 0
    current_length = 0
    
    for bit in binary_rep:
        if bit == '1':
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    
    if current_length > max_length:
        max_length = current_length
    
    return max_length

number = int(input("Enter your number: "))
print(f"Longest consecutive 1’s length : {longest_consecutive_ones(number)}")