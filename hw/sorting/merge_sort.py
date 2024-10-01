from misc import *

EXCLUSIVE_I_BOUND = 13

count = 0

# O(NlogN)
def merge_sort(arr: list, first:int=None, last:int=None):
    first = 0 if first is None else first
    last = len(arr) - 1 if last is None else last
    
    if first < last:
        mid = (first + last) // 2

        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        merge_lists(arr, first, mid, mid + 1, last)

    return arr

def merge_lists(arr: list, start1:int, end1:int, start2:int, end2:int):
    global count
    final_start = start1
    final_end = end2

    result = []

    while start1 <= end1 and start2 <= end2:
        if arr[start1] < arr[start2]:
            result.append(arr[start1])
            start1 += 1
        else:
            result.append(arr[start2])
            start2 += 1
        
        count += 1
    
    if start1 <= end1:
        while start1 <= end1:
            result.append(arr[start1])
            start1 += 1
    else:
        while start2 <= end2:
            result.append(arr[start2])
            start2 += 1

    indC = 0
    for i in range(final_start, final_end + 1, 1):
        arr[i] = result[indC]
        indC += 1



if __name__ == "__main__":
    # NOTE: Verification:
    arr = [6, 2, 4, 7, 1, 3, 8, 5]
    print(arr)
    print("Merge sort:\n", merge_sort(arr), sep="")


    # NOTE: Randomized
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]
    #     shuffle(test_arr)

    #     merge_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Merge Sort - Randomized Data")

    # NOTE: Sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]

    #     merge_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Merge Sort - Sorted Data")

    # NOTE: Reverse sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N - 1, -1, -1)]

    #     merge_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title="Merge Sort - Reverse Sorted Data")