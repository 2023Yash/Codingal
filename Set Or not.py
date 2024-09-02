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