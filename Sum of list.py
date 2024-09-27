def Sum_of_List(l):
    list_length = len(l)

    if(list_length == 1):
        return l[0]
    
    return l[0] +  Sum_of_List(l[1:])

l = (1, 2, 3, 4, 5, 6, 7, 8 ,9, 10)



print(Sum_of_List(l))