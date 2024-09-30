from misc import *

EXCLUSIVE_I_BOUND = 17

count = 0

# O(n^2)
def mod_bubble_sort(arr: list):
    global count

    N = len(arr) - 1
    sort = True

    iter = 0
    while sort:
        sort = False

        if iter % 2 == 1:
            # large to bottom
            for i in range(N):
                count += 1

                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp

                    sort = True
        else:
            # small to top
            for i in range(N, 0, -1):
                count += 1

                if arr[i - 1] > arr[i]:
                    temp = arr[i - 1]
                    arr[i - 1] = arr[i]
                    arr[i] = temp

                    sort = True
        
        iter += 1
    
    return arr


if __name__ == "__main__":
    # NOTE: Verification
    arr = [6, 2, 4, 7, 1, 3, 8, 5]
    print(arr)
    print("Modified Bubble sort:\n", mod_bubble_sort(arr), sep="")

    # NOTE: Randomized
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]
    #     shuffle(test_arr)

    #     mod_bubble_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Modified Bubble Sort - Randomized Data")

    # NOTE: Sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]

    #     mod_bubble_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Modified Bubble Sort - Sorted Data")

    # NOTE: Reverse sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N - 1, -1, -1)]

    #     mod_bubble_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Modified Bubble Sort - Reverse Sorted Data")