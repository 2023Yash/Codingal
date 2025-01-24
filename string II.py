def reverse_case(string):
    str_len = len(string)
    answer = ""

    for i in range(str_len):
        if string[i].islower():
            answer += string[i].upper()
        else:
            answer += string[i].lower()
    
    print(answer)

def palindrome_check(string):
    if string == string[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    str_len = len(string)
    answer = ""

    for i in range(str_len):
        if string[i] not in vowels:
            answer += string[i]

    print(answer)

string = input("Enter String:")
reverse_case(string)
palindrome_check(string)
remove_vowels(string)

