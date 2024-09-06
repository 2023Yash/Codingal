def Set_Or_Not():
    n = int(input("Enter a number:"))
    position = int(input("Enter a number for position:"))

    if (n & 1 << (position -1)):
        print("Set")
    else:
        print("Not set")

    print()
    
    return Set_Or_Not()

Set_Or_Not()


# inp = input("Enter a string:")

# ans = ""

# ans += inp[0]
# ans += inp[len(inp) // 2]
# ans += inp[-1]

# print(ans)

# for i in range(1000, 3200):
#     i_str = str(i)

#     if(
#         int(i_str[0]) % 2 == 0 
#         and
#         int(i_str[1]) % 2 == 0 
#         and
#         int(i_str[2]) % 2 == 0 
#         and
#         int(i_str[3]) % 2 == 0 
#     ):
#         print(i)

# for i in range(1000, 3200):
#     i_str = str(i)
#     check = 0
#     for j in range(len(i_str)):
#         if(int(i_str[j]) % 2 == 0):
#             check = 1
#         else:
#             check = 0
#             break

#     if (check == 1):
#         print(i)