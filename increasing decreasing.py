# def Increasing_decreasing(n, num):
#     if(n < 1 or n > num):
#         return
    
#     print(n)
#     Increasing_decreasing(n - 1, num)
#     print(n)

# Increasing_decreasing(10, 10)














Email_Inp = "yashnaudiyal268@gmail.com"
email = Email_Inp.lower()

Letters_List = {
    "a": "vowel",
    "b": "consonant",
    "c": "consonant",
    "d": "consonant",
    "e": "vowel",
    "f": "consonant",
    "g": "consonant",
    "h": "consonant",
    "i": "vowel",
    "j": "consonant",
    "k": "consonant",
    "l": "consonant",
    "m": "consonant",
    "n": "consonant",
    "o": "vowel",
    "p": "consonant",
    "q": "consonant",
    "r": "consonant",
    "s": "consonant",
    "t": "consonant",
    "u": "vowel",
    "v": "consonant",
    "w": "consonant",
    "x": "consonant",
    "y": "consonant",
    "z": "consonant",
    "0": "number",
    "1": "number",
    "2": "number",
    "3": "number",
    "4": "number",
    "5": "number",
    "6": "number",
    "7": "number",
    "8": "number",
    "9": "number"
}

Total_Length = len(email)
vowels = 0
consonants = 0
numbers = 0
special_characters = 0

for i in range(0, len(email)):
    if (email[i] == "@" or email[i] == "."):
        special_characters += 1
    elif (Letters_List[email[i]] == "consonant"):
        consonants += 1
    elif (Letters_List[email[i]] == "vowel"):
        vowels += 1
    elif (Letters_List[email[i]] == "number"):
        numbers += 1



print(f"Total Length = {Total_Length}")
print(f"vowels = {vowels}")
print(f"consonsnts = {consonants}")
print(f"number = {numbers}")
print(f"special_characters = {special_characters}")