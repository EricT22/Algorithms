from misc import *
import sys
sys.setrecursionlimit(10**6)

EXCLUSIVE_I_BOUND = 13

count = 0

pivot_used = "Pivot: Last Location"


# O(NlogN)
def quick_sort(arr: list, first:int=None, last:int=None):
    first = 0 if first is None else first
    last = len(arr) - 1 if last is None else last
    
    if first < last:
        pivot = pivot_last(arr, first, last)
        quick_sort(arr, first, pivot - 1)
        quick_sort(arr, pivot + 1, last)

    return arr


# Default partition function, chooses the first element as pivot
def pivot_list(arr: list, first:int, last:int):
    global count

    pivot_val = arr[first]
    pivot_point = first

    for index in range(first + 1, last + 1, 1):
        if arr[index] < pivot_val:
            pivot_point += 1

            temp = arr[pivot_point]
            arr[pivot_point] = arr[index]
            arr[index] = temp
        
        count += 1
    
    temp = arr[pivot_point]
    arr[pivot_point] = arr[first]
    arr[first] = temp

    return pivot_point


# Chooses a random element as the pivot, swaps it into the first position,
# calls the default partition function
def pivot_rand(arr:list, first:int, last:int):
    random_pivot = random.randint(first, last)

    temp = arr[random_pivot]
    arr[random_pivot] = arr[first]
    arr[first] = temp

    return pivot_list(arr, first, last)


# Chooses the last element as the pivot, swaps it into the first position,
# calls the default partition function 
def pivot_last(arr:list, first:int, last:int):
    temp = arr[last]
    arr[last] = arr[first]
    arr[first] = temp

    return pivot_list(arr, first, last)


if __name__ == "__main__":
    # NOTE: Verification:
    arr = [6, 2, 4, 7, 1, 3, 8, 5]
    print(arr)
    print(f"Quick sort:\n{pivot_used}\n", quick_sort(arr), sep="")


    # NOTE: Randomized
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]
    #     shuffle(test_arr)

    #     quick_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title=f"Quick Sort - {pivot_used} - Randomized Data")

    # NOTE: Sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N)]

    #     quick_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title=f"Quick Sort - {pivot_used} - Sorted Data")

    # NOTE: Reverse sorted
    # avgs = [0 for x in range(EXCLUSIVE_I_BOUND)]
    # n_vals = [0 for x in range(EXCLUSIVE_I_BOUND)]

    # for i in range(EXCLUSIVE_I_BOUND):
    #     N = 2**i

    #     n_vals[i] = N

    #     test_arr = [x for x in range(N - 1, -1, -1)]

    #     quick_sort(test_arr)
    #     avgs[i] += count
    #     count = 0

    # plot(x=n_vals, y=avgs, title=f"Quick Sort - {pivot_used} - Reverse Sorted Data")