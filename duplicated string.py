def remove_duplicates(input_string):
  seen = set()
  result = ''
  for char in input_string:
    if char not in seen:
      seen.add(char)
      result += char
  return result

string1 = "programming"
string2 = "hello"
string3 = "aabbccddeeff"

print(f"Original string: {string1}, String after duplicate removal: {remove_duplicates(string1)}")
print(f"Original string: {string2}, String after duplicate removal: {remove_duplicates(string2)}")
print(f"Original string: {string3}, String after duplicate removal: {remove_duplicates(string3)}")