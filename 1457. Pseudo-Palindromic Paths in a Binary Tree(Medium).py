# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
#
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes
#
#
# Input: root = [2,3,1,3,1,null,1]
# Output: 2
# Explanation: The figure above represents the given binary tree.
# There are three paths going from the root node to leaf nodes:
# the red path [2,3,3], the green path [2,1,1], and the path [2,3,1].
# Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3]
# can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
#
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1
# Explanation: The figure above represents the given binary tree.
# There are three paths going from the root node to leaf nodes:
# the green path [2,1,1], the path [2,1,3,1], and the path [2,1].
# Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def pseudoPalindromicPaths(self, root) -> int:
        from collections import defaultdict

        if not root:
            return 0

        mp = defaultdict(int)
        self.res = 0

        def isPseduoPalindromic(mp):
            t = 1
            for i, v in mp.items():
                if v % 2:
                    if t:
                        t -= 1
                    else:
                        return False
            return True

        def preorder(root):
            mp[root.val] += 1
            if not root.left and not root.right:
                if isPseduoPalindromic(mp):
                    self.res += 1
                mp[root.val] -= 1
                return
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
            mp[root.val] -= 1

        preorder(root)

        return self.res
