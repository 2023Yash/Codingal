def find_substrings(input_string):
    substrings = []
    length = len(input_string)

    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(input_string[i:j])
    
    return substrings

user_input = input("Enter a string: ")
result = find_substrings(user_input)

print("All substrings are:")
for substring in result:
    print(substring)
