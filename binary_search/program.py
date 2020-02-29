def binarySearch(array, target):
    return binary_search_helper(array, 0, len(array)-1, target)


def binary_search_helper(array, start, end, target):
    if start > end:
        return -1
    middle = (start + end) // 2
    pot_match = array[middle]
    if target == pot_match:
        return middle
    elif target < pot_match:
        return binary_search_helper(array, start, middle-1, target)
    else:
        return binary_search_helper(array, middle+1, end, target)
