import matplotlib.pyplot as plt

def plot(x, y, x_label="", y_label="", title=""):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o')
    plt.xlabel(x_label, size=22.5)
    plt.ylabel(y_label, size=22.5)
    plt.title(title, size=22.5)
    plt.grid()
    plt.show()