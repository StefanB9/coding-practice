class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = list()
    branch_sums_help(root, result, 0)
    return result


def branch_sums_help(node, result, cur_sum):
    cur_sum += node.value
    if node.left is not None:
        branch_sums_help(node.left, result, cur_sum)
    if node.right is not None:
        branch_sums_help(node.right, result, cur_sum)
    if node.left is None and node.right is None:
        result.append(cur_sum)
