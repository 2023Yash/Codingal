def A_Power_Set():
    List = list()
    list_size = int(input("Enter list size:"))
    for i in range(0, list_size):
        inp = int(input(f"Enter {i + 1} element:"))
        List.append(inp)

    inner = 0
    outer = 0

    power_set_size = 2 ** list_size

    for outer in range(0, power_set_size):
        for inner in range(0, list_size):
            if((outer & (1 << inner)) > 0):
                print(List[inner], end = "")
        print()        
    print()

    return A_Power_Set()

A_Power_Set()