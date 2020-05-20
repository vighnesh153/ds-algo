from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(inorder: List[int], postorder: List[int]):
    if len(inorder) == 0:
        return None

    if len(inorder) == 1:
        postorder.pop()
        return TreeNode(inorder[0])

    root = postorder.pop()
    split_index = inorder.index(root)
    right = []
    if split_index + 1 < len(inorder):
        right = inorder[split_index + 1:]
    left = inorder[:split_index]

    right_node = solve(right, postorder)
    left_node = solve(left, postorder)

    return TreeNode(root, left_node, right_node)


_inorder = [9, 3, 15, 20, 7]
_postorder = [9, 15, 7, 20, 3]
tree = solve(_inorder, _postorder)
print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.right.left.val)
print(tree.right.right.val)
