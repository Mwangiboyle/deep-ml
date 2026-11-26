def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    count = {}
    total = 0
    for val in samples:
        count[val] = count.get(val,0) + 1
        total+=1
    if total==0:
        return []
    return[(val,count[val]/total) for val in sorted(count)]