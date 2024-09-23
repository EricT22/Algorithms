from plot import plot
import random

EXCLUSIVE_I_BOUND = 11

count = 0

# O(N)
def sequential_search(arr: list, target: int):
    for i in range(len(arr)):
        global count
        count += 1
        if arr[i] == target:
            return i
    
    return -1


def shuffle(arr: list):
    for i in range(len(arr)):
        # both bounds are inclusive
        index = random.randint(0, i)

        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp


if __name__ == "__main__":
    avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    for i in range(EXCLUSIVE_I_BOUND):
        N = 2**i

        n_vals[i] = N

        test_arr = [x + 1 for x in range(N)]
        shuffle(test_arr)

        for j in range(1, N + 1, 1):
            sequential_search(test_arr, j)
            avgs[i] += count
            count = 0
        
        avgs[i] = avgs[i] / N

    plot(x=n_vals, y=avgs, title="Sequential Search")