def Odd_Even():
    n = int(input("Enter a number:"))

    if (n ^ 1 == n + 1):
        print("The Number is Even.")
    else:
        print("The Number is Odd")

    return Odd_Even()

Odd_Even()