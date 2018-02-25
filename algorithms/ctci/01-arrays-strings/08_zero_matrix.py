print('importing zero matrix')


def zero_matrix(matrix):
    """
    If an element in an M x N matrix is 0, set its entire row and column to 0
    Runtime
    O(MN) O(MN)
    """
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(len(row)):
        if row[i]:
            nullify_row(matrix, i)

    for j in range(len(col)):
        if col[j]:
            nullify_column(matrix, j)

    return matrix


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_column(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


if __name__ == "__main__":
    matrix = [[2, 3, 0], [1, 1, 1], [0, 2, 8]]
    print(matrix)
    print(zero_matrix(matrix))
