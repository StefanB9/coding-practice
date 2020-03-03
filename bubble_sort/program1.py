def bubbleSort(array):
    for _ in range(len(array)):
        change_made = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                t = array[i]
                array[i] = array[i+1]
                array[i+1] = t
                change_made = True
        if not change_made:
            break
    return array
