def matmult(a: list[list], b: list[list]) -> list[list]:
    arows = len(a)
    acols = len(a[0])
    brows = len(b)
    bcols = len(b[0])

    if acols != brows:
        raise ValueError("unmatched matrices")
    
    r = [[0 for x in range(bcols)] for x in range(arows)]

    for i in range(arows):
        for j in range(bcols):
            for k in range(acols): # could also use brows
                r[i][j] += a[i][k] * b[k][j]

    return r

def printmat(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], " ", sep="", end="")
        print(end="\n")


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]

    try:
        c = matmult(a, a)
    except ValueError as e:
        print(e)

    c = matmult(a, b)
    printmat(c)