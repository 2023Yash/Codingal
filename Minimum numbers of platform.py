def find_platform(arrival, departure, n):
    platform_n = 1
    result = 1

    for i in range(n):
        platform_n = 1
        for j in range(n):
            if i != j:
                if (arrival[i] >= arrival[j] and departure[j] >= departure[i]):
                    platform_n += 1
        result = max(result, platform_n)

    return result

arrival = [100, 300, 500]
departure = [900, 400, 600]

n = len(arrival)

print(find_platform(arrival, departure, n))
