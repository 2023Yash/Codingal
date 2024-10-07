def Hanoi(a, b, c, n):
    if (n == 1):
        print("Move disk 1 from rode A to rode B")
        return

    Hanoi(a, c, b, n - 1)
    print(f"Move disk {n} from rode A to B")
    Hanoi(c, b, a, n - 1)

Hanoi("a", "b", "c", 3)