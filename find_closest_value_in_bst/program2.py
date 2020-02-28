def findClosestValueInBst(tree, target: int):
    return find_closest_value_in_bst_rec(tree, target, float('inf'))


def find_closest_value_in_bst_rec(tree, target: int, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest
