import math

def is_prime(num):
    i = 2
     
    while i <= num / 2:
        if num % i == 0:
            return False
        i += 1
    
    return True


def prime_nums_list(length):
    primes = []

    i = 2
    while len(primes) < length:
        if is_prime(i):
            primes.append(i)
        
        i += 1

    return primes

def prime_nums_up_to(num):
    primes = []

    i = 2
    while i <= num:
        if is_prime(i):
            primes.append(i)
        
        i += 1
    
    return primes


def prime_factors(num):
    prime_factors = []

    i = 2
    while i <= math.sqrt(num):
        if is_prime(i):
            while num % i == 0:
                num //= i
                prime_factors.append(i)

        i += 1
    
    if num > 1:
        prime_factors.append(num)



    return prime_factors


def godel_forward(input_arr):
    prime_set = prime_nums_list(len(input_arr))

    godel_num = 1

    for i in range(len(input_arr)):
        godel_num *= prime_set[i]**input_arr[i]

    return godel_num


def godel_backward(factors):
    list_of_primes = prime_nums_up_to(factors[len(factors) - 1])

    count = {prime:0 for prime in list_of_primes}

    for i in factors:
        count[i] += 1

    return list(count.values())


if __name__ == "__main__":
    input_arr = [int(num) for num in input("Input Sequence: ").split()]

    godel_num = godel_forward(input_arr)
    factors = prime_factors(godel_num)
    recreated_seq = godel_backward(factors)

    print("Godel Number: ", godel_num)
    print("Prime Factors of Godel Number: ", factors)
    print("Recreated Sequence: ", recreated_seq)