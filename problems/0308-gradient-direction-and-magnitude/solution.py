import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    # Your code here
    squares = 0
    unit =[]
    direction =[]
    for i in range(len(gradient)):
        squares +=gradient[i]**2
    magnitude = np.sqrt(squares)
    for _ ,n in enumerate(gradient):
        if n == 0:
            unit.append(0)
        else:

            unit.append(float(n/magnitude))
    direction = np.negative(unit)

    return {
        "magnitude":magnitude,
        "direction":unit,
        "descent_direction":direction
    }