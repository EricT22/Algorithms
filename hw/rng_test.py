from rng import RNG
import random
import math

def mean(arr: list[int]):
    sum = 0
    for e in arr:
        sum += e

    return sum / len(arr)


def stdev(arr: list[int]):
    mu = mean(arr)

    summation = 0
    for e in arr:
        summation += (e - mu)**2
    
    return math.sqrt(summation / len(arr))



if __name__ == "__main__":
    random.seed(1)
    rng = RNG(1)

    py_rand = []
    my_rng = []


    N_VALS = [100, 1000, 10000, 100000, 1000000, 10000000]

    for N in N_VALS:
        for i in range(N):
            py_rand.append(random.randint(1, 100))
            my_rng.append(rng.nextInt(100))

        print(f"N: {N}\n{N} Python: ", mean(py_rand), ", ", stdev(py_rand), f"\n{N} Mine: ", mean(my_rng), ", ", stdev(my_rng), sep="")
