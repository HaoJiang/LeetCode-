# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return
        res = []

        def dfs(s=s, path=[]):
            if not s:
                res.append(path)
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]])

        def isPalindrome(str):
            return str == str[::-1]

        dfs()
        return res


s = 'aabb'
print(Solution().partition(s))
