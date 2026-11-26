def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []

    if mode == "row":
        for row in matrix:
            row_sum = 0
            for val in row:
                row_sum += val
            means.append(row_sum / len(row))

    elif mode == "column":
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        for col in range(num_cols):      # Outer loop: move across columns
            col_sum = 0
            for row in range(num_rows):  # Inner loop: move down each row
                col_sum += matrix[row][col]
            means.append(col_sum / num_rows)

    return means