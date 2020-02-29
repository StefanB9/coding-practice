def productSum(array, level=1):
    result = 0
    for el in array:
        if isinstance(el, list):
            result += (productSum(el, level+1)) * level
        else:
            result += el * level
    return result
