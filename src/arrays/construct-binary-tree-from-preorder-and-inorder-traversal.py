from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(preorder: List[int], inorder: List[int]):
    if len(inorder) == 0:
        return None

    if len(inorder) == 1:
        preorder.pop()
        return TreeNode(inorder[0])

    root = preorder.pop()
    split_index = inorder.index(root)
    left = inorder[:split_index]
    right = []
    if split_index + 1 < len(inorder):
        right = inorder[split_index + 1:]

    left_node = solve(preorder, left)
    right_node = solve(preorder, right)

    return TreeNode(root, left_node, right_node)


_preorder = [3, 9, 20, 15, 7]
_inorder = [9, 3, 15, 20, 7]
# taking reverse because I am popping out root from end
tree = solve(_preorder[::-1], _inorder)
print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.right.left.val)
print(tree.right.right.val)
