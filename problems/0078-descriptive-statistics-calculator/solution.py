import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    arr = np.asarray(data, dtype=float)
    
    
    mean = float(np.mean(arr))
    median = float(np.median(arr))
    
    
    values, counts = np.unique(arr, return_counts=True)
    mode = float(values[np.argmax(counts)])
    
    
    variance = float(np.var(arr))
    standard_deviation = float(np.std(arr))
    
    # 4. Percentiles (25th, 50th, 75th) & Interquartile Range (IQR)
    p25, p50, p75 = np.percentile(arr, [25, 50, 75])
    iqr = float(p75 - p25)
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": float(p25),
        "50th_percentile": float(p50),
        "75th_percentile": float(p75),
        "interquartile_range": iqr
    }