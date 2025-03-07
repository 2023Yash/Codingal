def get_ascii_values(input_string):
  ascii_dict = {}
  for char in input_string:
    ascii_dict[char] = ord(char)
  return ascii_dict

def print_ascii_values(input_string):
  """
  Prints the ASCII values of each character in a string.
  """
  for char in input_string:
    print(f"The ASCII value of '{char}' is: {ord(char)}")

my_string = "Hello, World!"

ascii_values = get_ascii_values(my_string)
print("ASCII Values (Dictionary):", ascii_values)

print("\nASCII Values (Printed):")
print_ascii_values(my_string)