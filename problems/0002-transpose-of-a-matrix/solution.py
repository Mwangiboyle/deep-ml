def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    rows = len(a)
    cols = len(a[0])
    results = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            results[j][i] = a[i][j]
    return results
