class sortingFuncts:

    # O(log2(N))
    @staticmethod
    def binary_search(arr: list, target: int):
        left, right = 0, len(arr) - 1

        while not left > right:
            mid = (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                # ignore bottom half
                left = mid + 1
            else:
                # ignore top half
                right = mid - 1
        
        return -1