# def parantheses(s, l, r, p, n):
#     if p == 2 * n:
#         for i in s:
#             print(i, end="")
#         print("\n")
    
#     if (l > r):
#         s[p] = "}"
#         parantheses(s, l, r + 1, p + 1, n)

#     if (l < n):
#         s[p] = "{"
#         parantheses(s, l + 1, r, p + 1, n)

# n = int(input("Enter a number:"))

# s = [""] * 2 * n

# parantheses(s, 0, 0, 0, n)

s = "I like to CODE!"

print(s[7:3:-3])