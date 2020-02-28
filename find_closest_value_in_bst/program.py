def findClosestValueInBst(tree, target: int):
    return find_closest_value_in_bst_rec(tree, target, float('inf'))


def find_closest_value_in_bst_rec(tree, target: int, closest):
    if tree is None:
        return closest
    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
    if tree.value > target:
        return find_closest_value_in_bst_rec(tree.left, target, closest)
    if tree.value <= target:
        return find_closest_value_in_bst_rec(tree.right, target, closest)
