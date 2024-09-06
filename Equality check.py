def Equality_check():
    n_1 = int(input("Enter 1st number:"))
    n_2 = int(input("Enter 2nd number:"))

    if ((n_1 ^ n_2) == 0):
        print(f"{n_1} and {n_2} are same.")
    else:
        print(f"{n_1} and {n_2} are not same.")
    print()

    return Equality_check()

Equality_check()