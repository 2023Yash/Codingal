def Check_Sorted(l):
    list_length = len(l)

    if(list_length == 0 or list_length == 1):
        return True
    
    return l[0] <= l[1] and Check_Sorted(l[1:])

lis = [1, 5, 34, 242, 123]

if(Check_Sorted(lis)):
    print("List is sorted")
else:
    print("List isn't sorted")