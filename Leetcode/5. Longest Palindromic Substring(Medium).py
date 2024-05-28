# Given a string s, return the longest palindromic substring in s.


# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #  odd palindrome      **1**
        #  even palindrome       **11**

        def _palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            odd_i, odd_j = _palindrome(i, i)
            even_i, even_j = _palindrome(i, i + 1)

            if end - start < odd_j - odd_i:
                start = odd_i
                end = odd_j
            if end - start < even_j - even_i:
                start = even_i
                end = even_j
        return s[start: end + 1]


if __name__ == "__main__":
    print(Solution().longestPalindrome(s="baad"))
