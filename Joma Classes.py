def multiply(a, b):
    num_iterations = b
    start_a = abs(a)
    added_a = abs(a)

    if b == 0:
        print(0)
    elif b == 1:
        print(a)
    elif b == -1:
        print(-a)
    else:
        start_iteration = abs(b) - abs(b) + 2

        while start_iteration <= abs(b):
            start_a = start_a + added_a
            start_iteration += 1

        if a and b > 0:
            print(start_a)
        elif a > 0 and b < 0:
            print(-start_a)
        elif b > 0 and a < 0:
            print(-start_a)
        elif a and b < 0:
            print(start_a)


multiply(-4, 5)
