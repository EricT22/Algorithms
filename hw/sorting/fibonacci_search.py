from plot import plot
import numpy as np

EXCLUSIVE_I_BOUND = 11

count = 0

# O(log2(N))
def fibonacci_search(arr: list, target: int):
    n = len(arr)
    
    fmin2 = 0
    fmin1 = 1
    f = fmin1 + fmin2

    while f <= n:
        fmin2 = fmin1
        fmin1 = f
        f = fmin1 + fmin2
    
    offset = -1
    while fmin2 >= 0:
        index = min(offset + fmin2, n - 1)

        global count
        count += 1
        if arr[index] < target:

            # search to the left
            f = fmin1
            fmin1 = fmin2
            fmin2 = f - fmin1
            offset = index
        elif arr[index] > target:
            count += 1
            
            # search to the right
            f = fmin2
            fmin1 = fmin1 - fmin2
            fmin2 = f - fmin1
        else:
            count += 1
            return index
    
    return -1

if __name__ == "__main__":
    avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]
    
    for i in range(EXCLUSIVE_I_BOUND):
        N = 2**i

        n_vals[i] = N

        test_arr = [x + 1 for x in range(N)]

        for j in range(1, N + 1, 1):
            fibonacci_search(test_arr, j)
            avgs[i] += count
            count = 0
        
        avgs[i] = avgs[i] / N

    plot(x=n_vals, y=avgs, title="Fibonacci Search")