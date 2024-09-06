if __name__ == "__main__":
    c = 1
    n = 100
    sum = 0

    # summation 1
    for i in range(c, n + 1, 1):
        sum += i
    print(sum)

    sum = 0
    for i in range(0, n - c + 1, 1):
        sum += i + c
    print(sum)

    # summation 2
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i * c
    print(sum)

    sum = 0
    for i in range(1, n + 1, 1):
        sum += i
    sum *= c
    print(sum)

    # summation 3
    sum = 0
    for i in range(c, n + 1, 1):
        sum += i
    print(sum)

    sum = 0
    for i in range(0, n + 1, 1):
        sum += i
    for i in range(0, c - 1,  1):
        sum += i
    print(sum)

    # summation 4
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i
    print(sum)

    sum = (n * (n + 1)) // 2
    print(sum)

    # summation 5
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i**2
    print(sum)

    sum = (2 * n**3 + 3 * n**2 + n) // 6
    print(sum)