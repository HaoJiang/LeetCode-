#
# 917. Palindrome Permutation II
#
# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
#
# Example
# Example1
#
# Input: s = "aabb"
# Output: ["abba","baab"]
# Example2
#
# Input: "abc"
# Output: []


class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """

    def canPermutePalindrome(self, s):
        # write your code here
        from collections import Counter

        if not s:
            return

        s = Counter(s)
        res = []

        def isPalindrome(s):
            t = 1
            for i, v in s.items():
                if v % 2:
                    if not t:
                        return False
                    else:
                        t -= 1
            return True

        def dfs(nums, path, mid):
            if not nums:
                res.append(path + mid + path[::-1])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    dfs(nums[:i] + nums[i + 1:], path + nums[i], mid)

        if isPalindrome(s):
            nums = ''
            even = ""
            for i, v in s.items():
                if v % 2:
                    even = i
                    if v // 2:
                        nums += i * (v // 2)
                else:
                    nums += i * (v // 2)
            dfs(nums, '', even)
            return res
        else:
            return []


print(Solution().canPermutePalindrome("aaaabbbbcdddd"))
