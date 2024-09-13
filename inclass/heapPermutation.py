test = [1, 2, 3]
N = len(test)


def heapPermute(n):
    if n == 0:
        # direct solution is to print results, which will be one permutation
        print(test)
    else:
        for i in range(0, n, 1):
            # subdivision is reducing n by 1
            # heapPermute call is the recurrence
            heapPermute(n - 1)
            
            # recombination is swapping values
            if n % 2 == 1:
                temp = test[0]
                test[0] = test[n - 1]
                test[n - 1] = temp
            else:
                temp = test[i]
                test[i] = test[n - 1]
                test[n - 1] = temp


if __name__ == "__main__":
    heapPermute(N)