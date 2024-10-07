def is_power_of_two(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0

num = int(input("Enter a number: "))
if is_power_of_two(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is not a power of 2.")