import matplotlib.pyplot as plt
import random

def plot(x, y, x_label="", y_label="", title=""):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o')
    plt.xlabel(x_label, size=22.5)
    plt.ylabel(y_label, size=22.5)
    plt.title(title, size=22.5)
    plt.grid()
    plt.show()


def shuffle(arr: list):
    # Fisher-Yates algorithm
    for i in range(len(arr) - 1, 0, -1):
        # both bounds are inclusive
        index = random.randint(0, i)

        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
