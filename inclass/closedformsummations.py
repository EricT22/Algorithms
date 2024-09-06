import math

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

    # summation 6
    sum = 0
    for i in range(0, n + 1, 1):
        sum += 2**i
    print(sum)

    sum = 2**(n+1) - 1
    print(sum)

    # summation 7
    a = 3
    sum = 0
    for i in range(0, n + 1, 1):
        sum += a**i
    print(sum)

    sum = (a**(n+1) - 1) // (a - 1)
    print(sum)

    # summation 8
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i * 2**i
    print(sum)

    sum = (n - 1) * 2**(n+1) + 2
    print(sum)

    # summation 9
    sum = 0
    for i in range(1, n + 1, 1):
        sum += 1 / i
    print(sum)

    sum = math.log(n) + 0.57721566 # Euler's Constant
    print(sum)

    # summation 10
    sum = 0
    for i in range(1, n + 1, 1):
        sum += math.log2(i)
    print(sum)

    sum = n * math.log2(n) - 1.5
    print(sum)