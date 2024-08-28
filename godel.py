def prime_nums(i):
    return []

def godel_forward(input_arr):
    prime_set = prime_nums(len(input_arr))

    godel_num = 1

    for i in range(len(input_arr)):
        godel_num *= prime_set**input_arr[i]

    return godel_num

def godel_backward(godel_num):
    prime_factors = []

    

    return prime_factors