# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring123(self, s):
        from collections import defaultdict
        mp = {}
        left = 0
        maxlen = 0
        for right in range(len(s)):
            if s[right] in mp:
                stop = mp[s[right]]
                while left <= stop:
                    if s[left] in mp:
                        del mp[s[left]]
                    left += 1
            mp[s[right]] = right

            maxlen = max(maxlen, right - left + 1)

        return maxlen

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] in map:
                j = max(map[s[i]] + 1, j)
            res = max(res, i - j + 1)
            map[s[i]] = i
        return res

    def fsdfdfsf(self, s: str) -> int:
        pool = set()
        j = 0
        res = 0
        for i in range(len(s)):
            if s[i] in pool:
                while s[i] in pool:
                    pool.discard(s[j])
                    j += 1
            pool.add(s[i])
            res = max(res, i - j + 1)
        return res


print(Solution().lengthOfLongestSubstring123('abcabcbb'))

print(Solution().fsdfdfsf('abcabcbb'))
