import csv
import matplotlib.pyplot as plt
from data_fitting_matrix_methods import *

DATA_FILE_PATH = 'C:\\Users\\Eric\\OneDrive\\Documents\\Algorithms\\hw\\numerical_algos\\NoisyPolynomialData.csv'

STARTING_DEG = 1
HIGHEST_DEG = 7
DEGREES = [x for x in range(STARTING_DEG, HIGHEST_DEG + 1)]


def plot_two_curves(x, y, z, x_label="", y_label="", title=""):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o')
    plt.plot(x, z, color='r', marker='o')
    plt.xlabel(x_label, size=22.5)
    plt.ylabel(y_label, size=22.5)
    plt.title(title, size=22.5)
    plt.grid()
    plt.show()


def read_data(path):
    with open(path, newline='') as datafile:
        reader = csv.reader(datafile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)

        data = []
        for row in reader:
            data.append(row[:])

        return data


def buildQ(degree, x_vals):
    q = []

    for k in range(0, degree + 1):
        row = []
        for j in range(k, k + degree + 1):
            sum = 0
            for i in range(0, len(x_vals)):
                sum += x_vals[i]**j

            row.append(sum)

        q.append(row)

    return q


def buildU(degree, x_vals, y_vals):
    u = []

    for k in range(0, degree + 1):
        sum = 0
        for i in range(0, len(x_vals)):
            sum += y_vals[i] * x_vals[i]**k
        
        u.append([sum])
    
    return u


if __name__ == "__main__":
    data = []
    for col in zip(*read_data(DATA_FILE_PATH)):
        data.append(list(col))
    
    x_vals = data[0]
    y_vals = data[1]

    for deg in DEGREES:
        coefs = unsqueeze2D(matmult(invmat(buildQ(deg, x_vals)), buildU(deg, x_vals, y_vals)))

        fitted_curve_y_vals = []
        for x in x_vals:
            fitted_curve_y_vals.append(horners_method(coefs, x))

        # have to close one graph to open the next one
        plot_two_curves(x=x_vals, y=y_vals, z=fitted_curve_y_vals, title=f"Degree {deg} Polynomial Fit")