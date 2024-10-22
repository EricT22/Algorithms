def gauss_jordan_elim(mat):
    N = len(mat)

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
        for j in range(N + 1):
            mat[i][j] /= divisor

        row_inds = list(range(N))
        row_inds.remove(i)
        for j in row_inds:
            multiplier = mat[j][i]

            for k in range(N + 1):
                mat[j][k] -= multiplier * mat[i][k]

    sol_set = []
    for i in range(N):
        sol_set.append(mat[i][N])
    
    return sol_set


test_arr = [[2, 3, 4], [5, 1, 7]]
print(gauss_jordan_elim(test_arr))