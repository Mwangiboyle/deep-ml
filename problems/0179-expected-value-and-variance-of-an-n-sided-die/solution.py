def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Your code here
    pass
    expect = float(n+1)/2
    n_squared = n *n
    variance = float((n_squared-1)/12)
    return (expect, variance)