def gauss_jordan_elim(mat):
    N = len(mat)

    for i in range(N):
        for j in range(i + 1, N):
            if mat[j][i] != 0:
                temp_row = mat[j]
                mat[j] = mat[i]
                mat[i] = temp_row
                break
        else:
            raise ValueError("This is a singular matrix")

        for j in range(N + 1):
            mat[i][j] /= mat[i][i]

        row_inds = list(range(N))
        row_inds.remove(i)
        for j in row_inds:
            multiplier = mat[j][i]

            for k in range(N + 1):
                mat[j][k] -= multiplier * mat[i][k]