# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.
#
# Input: s = "(abcd)"
# Output: "dcba"
#
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
#
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        stack = ['']

        for i in s:
            if i == '(':
                stack.append('')
            elif i == ')':
                reversestr = stack.pop()[::-1]
                stack[-1] += reversestr
            else:
                stack[-1] += i

        return stack.pop()

