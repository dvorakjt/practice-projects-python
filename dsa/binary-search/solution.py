def binary_search(x, arr, start = 0, end = None):
    """Finds the index of an item in a sorted list"""
    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1

    midpoint = start + (end - start) // 2

    if arr[midpoint] == x:
        return midpoint

    if arr[midpoint] < x:
        return binary_search(x, arr, midpoint + 1, end)
    return binary_search(x, arr, start, midpoint -1)
