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