import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    vector1 = np.array(v1)
    vector2 = np.array(v2)
    similiarity = np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return float(similiarity)