test = [1, 2, 3]

def heapPermute(n):
    if n == 0:
        print(test)
    else:
        for i in range(0, n, 1):
            heapPermute(n - 1)
            
            if n % 2 == 1:
                temp = test[0]
                test[0] = test[n - 1]
                test[n - 1] = temp
            else:
                temp = test[i]
                test[i] = test[n - 1]
                test[n - 1] = temp


if __name__ == "__main__":
    n = len(test)

    heapPermute(n)