from plot import plot

EXCLUSIVE_I_BOUND = 11

count = 0

# O(log2(N))
def binary_search(arr: list, target: int):
    left, right = 0, len(arr) - 1

    while not left > right:
        mid = (right + left) // 2

        global count
        count += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # ignore bottom half
            left = mid + 1
        else:
            # ignore top half
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    for i in range(EXCLUSIVE_I_BOUND):
        N = 2**i

        n_vals[i] = N

        test_arr = [x + 1 for x in range(N)]

        for j in range(1, N + 1, 1):
            binary_search(test_arr, j)
            avgs[i] += count
            count = 0
        
        avgs[i] = avgs[i] / N

    plot(x=n_vals, y=avgs, title="Binary Search")