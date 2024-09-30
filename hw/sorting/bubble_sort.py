from misc import *

EXCLUSIVE_I_BOUND = 17

count = 0

# O(n^2)
def bubble_sort(arr: list):
    global count

    N = len(arr)
    sort = True

    while sort:
        N = N - 1
        sort = False
        
        for i in range(N):
            count += 1

            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

                sort = True
    
    return arr


if __name__ == "__main__":
    # NOTE: Verification
    arr = [6, 2, 4, 7, 1, 3, 8, 5]
    print(arr)
    print("Bubble sort:\n", bubble_sort(arr), sep="")


    # NOTE: Randomized
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]
    #     shuffle(test_arr)

    #     bubble_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Bubble Sort - Randomized Data")

    # NOTE: Sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]

    #     bubble_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Bubble Sort - Sorted Data")

    # NOTE: Reverse sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N - 1, -1, -1)]

    #     bubble_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Bubble Sort - Reverse Sorted Data")