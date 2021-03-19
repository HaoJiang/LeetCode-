# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(root, X):
            if root:
                if root.val >= X:
                    self.res += 1
                    X = root.val
                dfs(root.left, X)
                dfs(root.right, X)
            return self.res

        return dfs(root, root.val)
