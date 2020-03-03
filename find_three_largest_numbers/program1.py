def findThreeLargestNumbers(array):
    if len(array) <= 3:
        return sorted(array)
    three_largest = sorted([array[i] for i in range(3)])
    for i in range(3, len(array)):
        if array[i] > three_largest[0]:
            three_largest[0] = array[i]
            three_largest = sorted(three_largest)
    return three_largest
