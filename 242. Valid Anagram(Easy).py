# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter

        return Counter(s) == Counter(t)
        # sea = [0] * 26
        # for i in s:
        #     sea[ord(i) - 97] += 1
        #
        # for j in t:
        #     sea[ord(j) - 97] -= 1
        #
        # return sum(sea) == 0


print(Solution().isAnagram('anagram', 'nagaram'))
