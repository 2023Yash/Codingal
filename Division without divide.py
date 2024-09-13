Divident = int(input("Enter Divident:"))
Divisor = int(input("Enter Divisor:"))
Quetiont = 0

for i in range(100):
    if (Divisor * i > Divident):
        Quetiont = i - 1
        break

print(Quetiont)
