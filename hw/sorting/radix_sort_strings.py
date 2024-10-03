def radix_sort(arr:list):
    maxlen = len(max(arr, key=len))
    arr = pad(arr, maxlen)
    bucket = [[] for i in range(128)] # 128 chars in the part of the ASCII table I care about

    for shift in range(maxlen - 1, -1, -1):
        for entry in range(len(arr)):
            bucketNum = ord(arr[entry][shift])
            bucket[bucketNum].append(arr[entry])
        
        arr = combine_buckets(bucket)

    return strip(arr)


def radix_sort_nums(arr:list):
    radix = 10
    keysize = 3
    bucket = [[] for i in range(radix)]
    shift = 1
    for loop in range(keysize):
        for entry in range(len(arr)):
            bucketNum = (arr[entry] // shift) % radix
            bucket[bucketNum].append(arr[entry])
        
        arr = combine_buckets(bucket)
        shift = shift * 10

    return arr

def combine_buckets(bucket):
    comb = []

    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            comb.append(bucket[i][j])
        else:
            bucket[i].clear()

    return comb


def pad(arr:list, maxlen:int):
    for i in range(len(arr)):
        while len(arr[i]) < maxlen:
            arr[i] += '-'

    return arr


def strip(arr:list[str]):
    for i in range(len(arr)):
        while arr[i][len(arr[i]) - 1] == '-':
            arr[i] = arr[i][0:len(arr[i]) - 1]

    return arr


if __name__ == "__main__":
    unsorted = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", 
                "twenty"]
    
    # # numerical test (works)
    # arr = [310, 213, 130, 301, 222, 201, 111, 323, 330, 102, 231, 120]
    # # 102 111 120 130 201 213 222 231 301 310 323 330
    # print(radix_sort_nums(arr))

    sorted = radix_sort(unsorted)

    for e in sorted:
        print(e)