# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if d == 1:
            return TreeNode(v, left=root)

        stack = []
        while stack:
            d -= 1
            new_stack = []
            for node in range(len(stack)):
                if d == 1:
                    temp_left = node.left
                    temp_right = node.right
                    node.left = TreeNode(v)
                    node.left.left = temp_left
                    node.right = TreeNode(v)
                    node.right.right = temp_right
                else:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            stack = new_stack
        return root


