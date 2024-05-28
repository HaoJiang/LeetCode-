# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(left, right):
            if left == right:
                return None
            mid = (left + right) >> 1
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums))
if __name__ == '__main__':
    print(Solution().sortedArrayToBST( nums = [-10,-3,0,5,9]))