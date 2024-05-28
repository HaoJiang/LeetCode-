# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        upper = float('inf')
        lower = float('-inf')

        def dfs(root, lower, upper):
            if not root:
                return True
            if not lower < root.val < upper:
                return False

            return dfs(root.left, lower, root.val) or dfs(root.right, root, upper)

        return dfs(root, lower, upper)
