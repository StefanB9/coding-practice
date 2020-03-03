def twoNumberSum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        cur_sum = array[left] + array[right]
        if cur_sum == target_sum:
            return [array[left], array[right]]
        elif cur_sum < target_sum:
            left += 1
        elif cur_sum > target_sum:
            right -= 1
    return []
