from misc import *

EXCLUSIVE_I_BOUND = 17

count = 0

# O(n^2)
def insertion_sort(arr: list):
    global count

    for i in range(1, len(arr), 1):
        curr = arr[i]
        loc = i - 1

        count += 1
        while loc >= 0 and arr[loc] > curr:
            arr[loc + 1] = arr[loc]
            loc -= 1

            count += 1
        
        arr[loc + 1] = curr
    
    return arr


if __name__ == "__main__":
    # NOTE: Verification:
    arr = [6, 2, 4, 7, 1, 3, 8, 5]
    print(arr)
    print("Insertion sort:\n", insertion_sort(arr), sep="")


    # NOTE: Randomized
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]
    #     shuffle(test_arr)

    #     insertion_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Insertion Sort - Randomized Data")

    # NOTE: Sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]

    #     insertion_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Insertion Sort - Sorted Data")

    # NOTE: Reverse sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N - 1, -1, -1)]

    #     insertion_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Insertion Sort - Reverse Sorted Data")