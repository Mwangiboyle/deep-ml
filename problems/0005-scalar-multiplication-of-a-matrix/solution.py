def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    cols = len(matrix[0])
    rows = len(matrix)

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = matrix[i][j]*scalar
    return matrix 