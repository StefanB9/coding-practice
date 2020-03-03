def twoNumberSum(array, target_sum):
    nums = {}
    for num in array:
        pot_match = target_sum - num
        if pot_match in nums:
            return [pot_match, num]
        else:
            nums[num] = True
    return []
