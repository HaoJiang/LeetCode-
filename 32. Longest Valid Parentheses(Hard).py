# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# Example 1:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# Output: 0

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen1 = 0
        maxlen2 = 0
        maxcur1 = 0
        maxcur2 = 0
        cur1 = 0
        cur2 = 0
        n = len(s)
        for i in range(n):
            cur1 += 1 if s[i] == "(" else - 1
            cur2 += 1 if s[n - i - 1] == ")" else -1
            maxcur1 += 1
            maxcur2 += 1
            if cur1 == 0:
                maxlen1 = max(maxlen1, maxcur1)
            elif cur1 < 0:
                maxcur1 = 0
                cur1 = 0
            if cur2 == 0:
                maxlen2 = max(maxlen2, maxcur2)
            elif cur2 < 0:
                maxcur2 = 0
                cur2 = 0

        return max(maxlen1, maxlen2)


if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()"))
