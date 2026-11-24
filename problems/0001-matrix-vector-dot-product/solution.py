def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if not a or len(a[0]) != len(b):
        return -1
    a_rows = len(a)
    a_cols = len(a[0])

    ans = [0]*a_rows
    for i in range(a_rows):
        for j in range(a_cols):
            ans[i] +=a[i][j]*b[j]
    return ans