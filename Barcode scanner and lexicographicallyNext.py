def price(barcode):
    li = list()

    for i in barcode:
        n = ord(i)
        if n // 10:
            maximum = 0
            while n > 0:
                if n % 10 > maximum:
                    maximum = n % 10
                    n = n // 10
            li.append(maximum)
        else:
            li.append(n)

    return sum(li)

print(price("ea"))

def lexicographicallyNext(string):
    if string == "":
        return "u"
    
    i = len(string) - 1

    while string[i] == "z" and i >= 0:
        i -= 1

    if(i == -1):
        string = string + "u"
    else:
        string = string.replace(string[i], chr(ord(string[i]) + 1), 1)
    
    return string

print(lexicographicallyNext("codingalz"))