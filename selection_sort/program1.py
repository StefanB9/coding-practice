def selectionSort(array):
    cur_idx = 0
    while cur_idx < len(array) - 1:
        smallest_idx = cur_idx
        for i in range(cur_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        array[cur_idx], array[smallest_idx] = array[smallest_idx], array[cur_idx]
        cur_idx += 1
    return array
