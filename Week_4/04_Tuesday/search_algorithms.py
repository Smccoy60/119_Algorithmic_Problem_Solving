from search_support import id_key, matches, compare_values

def linear_search(records, target, key=id_key):
    """Return the first matching position and trace, or None and trace"""
    trace = []
    for position, record in enumerate(records):
        value = key(record)
        trace.append((position, value))
        if matches(value, target):
            return position, trace
    return None, trace

def binary_search(records, target, key=id_key):
    """Return any matching position and trace on key-ordered input."""
    trace = []
    low = 0
    high = len(records) - 1
    while low <= high: 
        middle = (low + high) // 2
        value = key(records[middle])
        trace.apend((low, high, middle, value))
        comparison = compare_values(value, target,)
        if comparison == 0
            return middle, trace
        if comparison < 0: 
            low = middle + 1
        else:
            high = middle - 1
    return None, trace
