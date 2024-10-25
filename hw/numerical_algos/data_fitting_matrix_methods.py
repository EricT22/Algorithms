def invmat(mat):
    N = len(mat)

    if N != len(mat[0]):
        raise ValueError("Must be a square matrix")
    
    imat = generate_imat(N)

    for i in range(N):
        for j in range(i, N):
            if mat[j][i] != 0:
                temp_row = mat[j]
                mat[j] = mat[i]
                mat[i] = temp_row
                break
        else:
            raise ValueError("This is a singular matrix")
        
        divisor = mat[i][i]
        for j in range(N):
            mat[i][j] /= divisor

            imat[i][j] /= divisor

        row_inds = list(range(N))
        row_inds.remove(i)
        for j in row_inds:
            multiplier = mat[j][i]

            for k in range(N):
                mat[j][k] -= multiplier * mat[i][k]

                imat[j][k] -= multiplier * imat[i][k]

    return imat


def generate_imat(N):
    return [[0 if i != j else 1 for j in range(N)] for i in range(N)]


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


def horners_method(coefs:list, x:float) -> float:
    deg = len(coefs) - 1
    result = coefs[deg]
    
    for i in range(deg - 1, -1, -1):
        result *= x
        result += coefs[i]

    return result


def unsqueeze2D(mat2d):
    mat1d = []

    for i in range(len(mat2d)):
        for j in range(len(mat2d[i])):
            mat1d.append(mat2d[i][j])

    return mat1d