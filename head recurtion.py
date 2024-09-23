def printing_number_from_1_to_10(n):
    if (1 > n):
        return
    printing_number_from_1_to_10(n - 1)
    print(n)

printing_number_from_1_to_10(10)