def longest_word(string):
    longest_word = ""
    last_space = 0
    for i in range(len(string)):
        if string[i] == " " or string[i] == ",":
            word = string[last_space:i]
            last_space = i + 1
            if len(word) > len(longest_word):
                longest_word = word
    word = string[last_space:]
    if len(word) > len(longest_word):
        longest_word = word

    print(longest_word)

string = "Hello People, It's a great day"
longest_word(string)

def sub_string_finder(string, sub_string):
    if sub_string in string:
        print(string.index(sub_string))
    else:
        print("Sub-String not found")

sub_string_finder("Yash", "ash")

def string_sort(string):
    array = []

    for i in string:
        array.append(ord(i))
    array.sort()
    print(array)

string = "edcba"
string_sort(string)