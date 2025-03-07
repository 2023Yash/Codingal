def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

input_str = "aabbbcdddef"
output = first_non_repeating_char(input_str)
print("The first non-repeating character is:", output)
